# This is the essentially package that holds the project together.
# The routes and relevant configuration information is held in here.
import os

import pymongo
from flask import Flask, url_for, request, render_template, redirect, jsonify, session
import uuid
from markupsafe import escape
from ssts.backendDB import dbClasses as db
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

WORKERS = db.WorkerCollection()
TICKETS = db.TicketCollection()
IDS = db.ID()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="4d2a6ccee35ad5d8cc7f64b521b2e4200e1ce2d5e019ba56010e6bcb6769b00e",
        DATABASE="mongodb+srv://root:o3JSG2Y9ciqU9G8P@cluster0.zusbpwn.mongodb.net/?retryWrites=true&w=majority",
    )
    pymongo.MongoClient(
        "mongodb+srv://root:o3JSG2Y9ciqU9G8P@cluster0.zusbpwn.mongodb.net/?retryWrites=true&w=majority")
    # pull out the ID number of ticket
    # check database for last number used, if any
    try:
        id_number = IDS.get_current_id('tickets')
        # do database stuff we expect to work here
        # like pulling last ID number
        # if this errors, then move to except

        print("working database stuff here")

        # use the get_ticket_collection function
        # if empty, throw error
        # otherwise, get the last ticket from the list.
    except:
        id_number = "001"
        # then this is where we set the first ID number for initialization
        # note to programmer: use str.zfill(3) to get three digit integer numbers

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # all application routes
    @app.route('/')
    def homepage(page_name="Homepage"):
        if 'name' not in session:
            return redirect('/login')
        username = session['name']
        return render_template("base.html", page_name=page_name, username=username)

    @app.route('/login', methods=['GET', 'POST'])
    def agent_login_page(page_name="Agent Login"):

        if request.method == 'POST':
            email = str(request.form.get('email'))
            password = str(request.form.get('password'))
            password = password.encode('utf-8')
            password = hashlib.sha256(password).hexdigest()

            found_user = WORKERS.get_worker(email)

            if (found_user.email == email) and (found_user.password == password):
                session['name'] = found_user.name
                return redirect('/')
            else:
                print("User not found")
                return redirect('/login')

        return render_template("auth/login.html", page_name=page_name)

    @app.route('/logout')
    def logout():
        session.pop('name', None)
        return redirect('/login')

    @app.route('/signup', methods=['GET', 'POST'])
    def agent_signup_page(page_name="Agent Signup", self=None):

        if request.method == 'POST':
            firstname = str(request.form.get('firstname')).capitalize()
            lastname = str(request.form.get('lastname')).capitalize()
            email = str(request.form.get('email'))
            password = str(request.form.get('password'))
            password1 = str(request.form.get('password1'))
            employee_type = str(request.form.get('employee_type'))

            print(f"POST Request completed here! ")
            print(f"{firstname, lastname, email, password, password1}")
            # found_user = USERS.find_user(email)

            if password != password1:
                print(f"Passwords do not match")
                message = "Passwords do not match"
                return redirect('/signup')

            # if found_user is not None:
            #     message = "User already exists"
            #     return redirect('/signup', message=message)
            else:
                name = f"{firstname} {lastname}"
                password = password.encode('utf-8')
                hashed_pass = hashlib.sha256(password).hexdigest()
                worker = db.Worker(name, email, hashed_pass, employee_type, None, None)
                WORKERS.add_worker(worker)
                return redirect('/login')

        return render_template("auth/signup.html", page_name=page_name)

    @app.route('/new/ticket', methods=['GET', 'POST'])
    def new_ticket(page_name=f"New Ticket {id_number}"):
        if 'name' not in session:
            return redirect('/login')
        id_number = IDS.get_current_id('tickets')

        username = session['name']

        if request.method == 'POST':
            # title
            ticket_title = str(request.form.get('title'))
            # description
            ticket_descript = str(request.form.get('description'))
            # device OS
            ticket_os = str(request.form.get('os'))
            # worker
            ticket_worker = str(request.form.get('worker'))
            # device
            ticket_device = str(request.form.get('device'))
            # device ID
            device_id = str(request.form.get('device_id'))

            ticket = db.Ticket(ticket_descript, ticket_title, ticket_worker, ticket_os, ticket_device, 'open', None)
            TICKETS.add_ticket(ticket)
            IDS.inc_id_count('tickets')  # update the ID number
            return redirect('/view/ticket')

        return render_template("new/create_ticket.html", page_name=page_name, id_number=id_number, username=username)

    @app.route('/view/ticket', methods=['GET'])
    def view_ticket_list(page_name="View Tickets"):
        if 'name' not in session:
            return redirect('/login')

        username = session['name']

        incidents = TICKETS.get_all_tickets()
        incidents = [incident for incident in incidents if incident.status != "closed"]
        incidents.reverse()
        return render_template("view/ticket.html", page_name=page_name, incidents=incidents, username=username)

    @app.route('/edit-incident/<incident_id>', methods=['POST'])
    def edit_incident(incident_id):
        if 'name' not in session:
            return redirect('/login')

        data = request.get_json()

        # ticket id
        ticket_id = data.get('id')

        # status
        ticket_status = data.get('status')

        print(ticket_id)
        # name
        ticket_name = data.get('name')
        # description
        ticket_descript = data.get('description')
        # os
        ticket_os = data.get('os')
        # worker
        ticket_worker = data.get('worker')
        # device
        ticket_device = data.get('device')

        ticket = db.Ticket(ticket_descript, ticket_name, ticket_worker, ticket_os, ticket_device, ticket_status, ticket_id)
        TICKETS.update_ticket(ticket)
        return redirect('/view/ticket')






    @app.route('/settings')
    def settings(page_name="Settings"):
        if 'name' not in session:
            return redirect('/login')

        username = session['name']

        return render_template("settings/settings.html", page_name=page_name, username=username)

    @app.route('/view/kb')
    def knowledgebase(page_name="Knowledge Base"):
        if 'name' not in session:
            return redirect('/login')

        username = session['name']

        incidents = TICKETS.get_all_tickets()
        incidents = [incident for incident in incidents if incident.status != "open"]
        incidents.reverse()

        return render_template("view/knowledgebase.html", page_name=page_name, username=username, incidents=incidents)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('error/404.html'), 500

    return app
