# Agile workflow in Meshi project development
## Table of contents
>### 1. [Issue types](#issue-types)
>>### a. [User Story](#user-story)
>>### b. [Task](#task)
>>### c. [Bug](#bug)
>### 2. [Writing Issues](#writing-issues)
>>### a. [KISS rule](#1.-**KISS**-rule)
>>### b. [Issue types writing examples](#2-issue-types-writing-**examples**)
>### 3. [Team meetings](#team-meetings)
>>### a. [Standups](#Standups)
>>### b. [Sprint Planning](#sprint-planning)
>>### c. [Sprint Review](#sprint-review)
>### 4. [Task estimating](#task-estimating-**Story-Points**)
>### 5. [Additional definitions](#additional-definitions)



## Issue types

* ### **User Story**

  * is comprised of **subtasks**
  * describes a **larger** piece of system's **functionality**
  * describes a piece of system functionality from a **user's perspective**
  * sum of work from multiple people

  Needs to specify:

  * title providing a short description
  * minimal **functional requirements** for User Story completion

* ### **Task**

  * is a basic building block of other, larger issues (**User Stories**) in the project
  * the smallest individual piece of work in the project
  * usually done by one person
  * are about implementation of the problem
  
  Needs to specify:
  
  * minimal requirements for task completion

* ### **Bug**

  * technically a type of **Task**
  * details **occurrence conditions** of a specified bug
  
  Needs to specify:
  
  * **unwanted, unexpected behaviour** of the system (images, screenshots are welcomed)
  * **desired, correct behaviour** of the system

## Writing Issues

### 1. **KISS** rule

  **K**eep **I**t **S**imple **S**illy\
  Be straight up and to the point. As mentioned above, i.e. code this, design that, create test data for this, validate test assumptions for that etc.

### 2. Issue types writing **examples**

* ## **User Story**

    Heading:

      [User Story #123] Add user login form

    Description:

      **As a user, I should** be able to log in to the service using login and password combination.

      ## Acceptance Criteria:
      *  A new login form is added to the website
        - [ ] form contains a login field
        - [ ] form contains a password field
        - [ ] form contains login button
      (...)

      ## Notes:
      can be various, loose ideas as to implementation, technologies (non essential stuff)
      (...)

* ## **Task**

    Heading:

      [Task #324] Add password validaton to the login form

    Description:

      Add a password validation for login form. Restrict: length, characters.

      ## Acceptance Criteria:
      *  Password should have these restictions
        - [ ] at leat one special character
        - [ ] at least one digit
        - [ ] at least 12 characters long 
      (...)

      ## Notes:
      * use regular expression to validate a password against criteria 
      
      can be various, loose ideas as to implementation, technologies (non essential stuff)
      (...)

* ## **Bug**

    Heading:

      [Bug #482] Password is not required during sign in process

    Description:

      ## Steps to reproduce:
      1. register a new user with valid login and password
      2. sign in using only user login

      ## Undesired behaviour: 
      * The registered user is able to login successfuly without providing a password  
      
      ## Desired behaviour:
      *  User is required to provide a password, user can not authenticate without a password 
      (...)

      ## Notes:
      an image showcasing the bug "in the field" would be welcome 
      can be various, loose ideas as to implementation, technologies (non essential stuff)
      (...)

## Team meetings

* ### Standups
  
  * frequency: idealy every day (daily standups), for Meshi project **every other day**
  * duration: **~15 minutes**
  * purpose: status report from every team member, current work, plan for the day

* ### Sprint Planning
  
  * frequency: once each Sprint
  * duration: **30~45 minutes**
  * purpose: sore new tasks, choose task for realisation in the next Sprint

* ### Sprint Review

  * frequency: once each Sprint
  * duration: **30~45 minutes**
  * purpose: analize the progress done during last Sprint, highlight problems

## Task estimating (**Story Points**)

System for group evaluating task difficulty.

| Story Points      | Time | Description |
| :------------- | :----------: | -----------: |
| 1 | ~1h | trivial **Tasks**, quick fixes, small **Bugs** |
| 2 | ~3h | small **Tasks**, **Bugs** |
| 3 | <=1d | regular **Tasks**, tricky **Bugs** |
| 5 | 2~5d | small **User Stories** |
| 8 | ~7d | regular **User Stories** |
| 13 | ~11d | mostly complex **User Stories** |


## Additional definitions

* **Sprint**
: usually **a two week period** started by Sprint Planning session and ended by Sprint Review, logical organisation of work into time intervals, establishes a clear, intermediate deadline

* **Agile**
: iterative approach to project management and software development that helps teams deliver value to their customers faster and with fewer headaches. Instead of betting everything on a "big bang" launch, an agile team delivers work in small, but consumable, increments. Requirements, plans, and results are evaluated continuously so teams have a natural mechanism for responding to change quickly.
