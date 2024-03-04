# This is the essentially package that holds the project together. the routes and relevant configuration information is held in here.
import os

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ssts.mongodb'),
    )
    # pull out the ID number of ticket
    # check database for last number used, if any
    try:
        # do database stuff we expect to work here
        # like pulling last ID number
        # if this errors, then move to except
        print("working database stuff here")
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
        return render_template("base.html", page_name=page_name)

    @app.route('/login')
    def agent_login_page(page_name="Agent Login"):
        return render_template("auth/login.html", page_name=page_name)

    @app.route('/service')
    def service_portal(page_name="Service Portal"):
        return render_template("service_portal/portal.html", page_name=page_name)

    @app.route('/sp/schedule')
    def service_portal_schedule(page_name="Service Portal Scheduler"):
        return render_template("service_portal/schedule.html", page_name=page_name)

    @app.route('/new')
    def new_ticket_home(page_name="New Ticket Home"):
        # will essentially redirect to the ticketing page

        # render template will need to be changed in a later revision.

        return render_template("new/ticket.html", page_name=page_name, id_number=id_number)

    @app.route('/new/ticket', methods=['GET','POST'])
    def new_ticket(page_name="New Ticket {id_number}"):
        # will need to save the DB information from the webpage
        # probably using an API request template once the submit button was hit.
        # will need to get the information from front-end about what information
        # was on the page.
        # this function will need to increment the ID Number of the ticket
        # and render it with the page as immutable.

        # if POST is used, then grab the information from the webpage and then
        # use DB functions to then make and store the information.

        # otherwise, when GET is used, just render the new ticket html template

        return render_template("new/ticket.html", page_name=page_name, id_number=id_number)

    @app.route('/view')
    def view_ticket_home(page_name="Ticket Home"):
        # this will render a page for the user to click between
        # either using the list view or the ID number directly.

        return render_template("view/ticket", page_name=page_name)

    @app.route('/view/ticket')
    def view_ticket_list(page_name="View Tickets"):
        # this will return a list of the past X tickets and render to user

        return render_template("view/ticket", page_name=page_name)

    @app.route('/view/ticket/<string:id_number>')
    def view_ticket(page_name="View Ticket {id_number}"):
        # may need to be modifed, flask might do something with this
        # that may be unforeseeable without a bit of testing...
        # will need a template base for ticket displaying from the frontend.
        # the rest of the function will take DB functions to get the information.

        # get relevant information on the ticket
            # includes id number, client email(s), worker email(s)
            # work notes in reverse order timestamped (last comment first)

        return render_template("view/ticket/{id_number}.html", page_name=page_name)

    return app
