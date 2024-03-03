# Requirements
_Group 10 - "Super Simple Ticketing System"\
Date and location: Feb 16, 2024\
Group Members: Olivia Vester, Dallon Jarman, Charles Descamps, Hannah Penado, Sam Cain, Jared Kaige_

## **1. Positioning**

### 1.1 Problem statement


<table>
  <tr>
   <td><strong>The problem of</strong>
   </td>
   <td> low-quality help ticket tracking systems for IT needs
   </td>
  </tr>
  <tr>
   <td><strong>affects</strong>
   </td>
   <td> employees working on solving issues submitted via ticket and the people who are submitting the tickets
   </td>
  </tr>
  <tr>
   <td><strong>the impact of which is</strong>
   </td>
   <td> low quality customer service and slow production of results
   </td>
  </tr>
</table>


### 1.2. Product Position Statement


<table>
  <tr>
   <td><strong>For</strong>
   </td>
   <td> employees, primarily 
   </td>
  </tr>
  <tr>
   <td><strong>Who</strong>
   </td>
   <td> want a more efficient work environment for tracking IT requests
   </td>
  </tr>
  <tr>
   <td><strong>The (product name)</strong>
   </td>
   <td> Super Simple Ticketing System
   </td>
  </tr>
  <tr>
   <td><strong>That</strong>
   </td>
   <td>you tracks and organizes IT tickets that can be accessed
   </td>
  </tr>
  <tr>
   <td><strong>Unlike</strong>
   </td>
   <td> OSTicket, ServiceNow, Peppermint, and Request Tracker
   </td>
  </tr>
  <tr>
   <td><strong>Our product</strong>
   </td>
   <td> will be quick, user friendly, and effective
   </td>
  </tr>
</table>


### 1.3. Value proposition and customer segment


```
Value proposition: Super Simple Ticketing System is an IT ticket tracking app for employees to efficiently manage their client's issues, by providing a simple yet efficient method of tracking and solving issues.
Consumer segment: IT Professionals who have to manage many issues at the same time
```



## 2. Stakeholders



* IT Employees - 
* Companies with an IT division
    * They will need a user friendly app that is easy to use and to understand for their non IT Employees
* Users submitting help requests that want a streamlined way to do so


## 3. Functional requirements (features)



1. Create tickets
2. Close tickets
3. Ability to sign in
4. Add comments to tickets
5. Assign tickets to different departments
6. Find tickets given email or ticket id
7. A knowledge base to look up common internal issues


## 4. Non-functional requirements



1. Response time
    * Having back end database functions that are able to quickly access queried information to the user
2. Reliability
* Our app needs to consistently be able to input data into the database from 


## 5. MVP

Our minimum viable product would be a ticketing system where users can add tickets, employees can respond to tickets, and employees can close tickets. These will be tested based on the ability of different user’s ability to use these features.

## 6. Use cases

### 6.1. Use case diagram
![Use case diagram](/Deliverables/img/D2/Use%20Case%20Diagram.png)

### 6.2. Use case description
---
### Olivia:

**Use case**: User submits a ticket\
**Actor**: User\
**Trigger**: The user hits the submit button for their ticket submission\
**Pre-Condition**: The user is logged into the system\
**Post-Condition**: The ticket enters the request pool\
**Success scenario**:
1. An employee is assigned the ticket and able to do what is requested
2. An employee completes the ticket 

**Alternative Flows**:
1. The ticket request is too broad to be filled
2. The user must resubmit their request 

![Olivia's Diagram](/Deliverables/img/D2/OliviaDiagram.png)

---
### Charles:

**Use Case**: Support Agent closes a ticket\
**Actor**: IT Employee\
**Trigger**: Employee switches the status of the ticket to closed\
**Pre-Condition**: Employee is logged into the system\
**Success Scenario**:
1. Ticket is completed, employee can close the ticket
2. Employee switches the status of the ticket from open to closed 

**Alternative Flows**:
1. Ticket is a duplicate of another ticket, mark as closed
2. Ticket is out of scope for the department, mark as closed 
---
### Sam:

**Use Case**: The administrator assigns tickets\
**Actor**: Administrator\
**Trigger**: Administrator assigns tickets to employees \
**Pre-Condition**: Administrator logged in\
**Success Scenario**:
1. Ticket is assigned to a designated employee
2. The employee is able to see the tickets assigned to them 

**Alternative Flows**:
1. Employee has too many tickets sent to them, can't assign 
2. Employee does not exist, can't assign 
---
### Dallon:

**Use case**: IT employee signs into the web application\
**Actor**: IT employee\
**Trigger**: The IT employee wants to sign into their account to access their tickets\
**Pre-Condition**: The user has previously made an account associated with the organization\
**Post-Condition**: The employee is in their account and it able to see a list of their tickets\
**Success scenario**:
1. The IT employee successfully signs in
2. The IT employee is able to see all their open and closed tickets. 

**Alternative Flows**:
1. The app rejects the user sign in
2. The app prompts the user to enter the correct password. 

---
### Hannah:

**Use case**: Update ticket progress\
**Actor**: IT employee\
**Trigger**: The IT employee updates the progress on a ticket.\
**Pre-Condition**: The IT employee has an account and is logged in.\
**Post-Condition**: The ticket information shows the progress progression of the ticket\
**Success scenario**:
1. The IT employee accesses an existing ticket in our system
2. The IT employee selects to update the ticket progress
3. The ticket progression shows what has been done to fix the ticket’s problem for future reference 
4. The ticket progression can be viewed by the client, manager, or other employees

**Alternative Flows**:
1. The application rejects the update request for incomplete information
2. The application informs the user of the incomplete info error
3. The application asks the user to input additional information. 

![Hannah's Diagram](/Deliverables/img/D2/Hannah%20Diagram.png)

---
### Jared:

**Use Case**: User searches for specific ticket\
**Actor**: Client/IT Employee\
**Trigger**: User wishes to see the details of a specific ticket\
**Pre-Conditions**: User is already logged in.\
**Post-Condition**: User receives the requested ticket\
**Success Scenario**: 
1. User signs into their account
2. User searches for a specific ticket
3. System verifies user has access to the ticket
4. System returns the ticket to the user 

**Alternative Scenario: 
1. System finds that user does not have access to the ticket
2. System informs the user of an error
3. System prompts the user to try again 

![Jared's Diagram](/Deliverables/img/D2/JaredDiagram.png)




# 7. User stories

**Priority Level Scale:** 0-12 (0 is highest priority, 12 is lowest)

**Hours Spent estimate**: A sum of all group members hours spend estimates to complete the user story

Olivia:

1. As a user, I want to get help on my IT requests in a timely manner, so that I can get my devices functioning for my projects.
    - Priority Level: 0
    - Hours Spent Estimate: 650 hours (basically our whole app)
2. As an employee, I want to be able to examine quickly and efficiently, so that I can maximize problem solving time.
    - Priority Level: 8
    - Hours Spent Estimate: 20 hours


Sam:

1. As an employee, I want to be able to respond to tickets in a timely manner, so that customers can get their questions answered quickly.
    - Priority level: 5
    - Hours spent estimate: 60 hours
2. As a customer, I want to be able to navigate the website easily, so that I can have a better and more enjoyable experience.
    - Priority level: 9
    - Hours spent estimate: 30 hours


Charles:

1. As a support agent, I want to be able to fulfill support requests, so that I can better assist a customer.
    - Priority Level: 2
    - Hours Spent Estimate: 60 hours
2. As a customer, I want to be able to see the support requests, so that I can see how an agent resolved my issue last time.
    - Priority Level: 6
    - Hours Spent Estimate: 45 hours

Dallon:

1. As a new employee, I want the ability to be able to find common issues, so I can quickly and efficiently assist the customer.
    - Priority Level: 10
    - Hours Spent Estimate: 8 hours
2. As a manager, I want the ability to see what tickets are being worked on, so that I can see what tickets are being worked on.
    - Priority Level: 7
    - Hours Spent Estimate: 12 hours


Jared:

1. As an employee, I want to be able to search for specific issues, so that I can easily find any issue.
    - Priority Level: 1
    - Time Estimate: 40 hours (total group estimated hours)
2. As an employee, I want to comment on issues, so that I can clarify any possible problems.
    - Priority Level: 4
    - Time Estimate: 40 hours


Hannah:

1. As an employee, I want to feel accomplished when I complete a ticket, so I can feel more motivated to complete them
    - Priority Level: 11
    - Hours Spend Estimate: 10 hours
2. As a user, I want to understand how to be able to see the progress on my ticket, so I know what is being done to fix it.
    - Priority Level: 3
    - Hours Spend Estimate: 100 hours




#### **8. Issue Tracker**
![D2IssueTracker](/Deliverables/img/D2/issueTrackerD2.png)