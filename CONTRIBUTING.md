# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email or any other method with the owners of this repository before making a change.

After contributing, please submit a request in order to be added to the [contributors](Contributors.csv) list. The request should take the form of an appropriately titled issue and include a reference to your contribution.

## Table of contents
>### 1. [General rules](#general-rules)
>>### a. [Language](#1-language)
>>### b. [Issues](#2-issues)
>>### c. [Commits](#3-commits)
>>### d. [Pull Requests](#4-pull-requests)
>### 2. [Git Workflow](#git-workflow)
>>### a. [Initial Setup](#initial-setup)
>>### b. [Issue Creation Process](#issue-creation-process)
>>### c. [Development Process](#development-process)
>>### d. [Pull Request Process](#pull-request-process)
>>### e. [Black workflow - linting python code](#black-workflow---linting-python-code)
>>### f. [Testing](#testing)

# General rules

## 1. Language

### English (required in)
* writing **commit messages**
* **naming** and **describing Issues**
* writing **code**
* **commenting** your **code**
* **naming branches**
* creating **labels**
* writing **documentation**

### Polish (allowed in)

* **discussions** - commenting under Pull Requests

## 2. Issues

### Each Issue has to have:
* title
* description of the problem (if Bug)
* detailed minimum requirenments for Pull Request approval process

## 3. Commits

### Messages

* Use the **present tense** ("Add feature" not "Added feature")
* Use the **imperative mood** ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to **50 characters or less**
* Reference all issues, branches, pull requests by preceding their names with '#'

Example: `Remove redundant code added in #234`

### Good practise

* commit frequently to not lose yourself in all the changes
* commit should be concise and regard single fix/change

Bad example: `Change passwd hashing algorithm and fix naming issue`

## 4. Pull Requests

### Naming

* name starts with Issue/branch category label and number in square brackets followed by
* next follows the relevant Issue name

Example: `[Bug #253] Email validation does not require '@' sign`

# Git Workflow
 
*See [AGILE_WORKFLOW](AGILE_WORKFLOW.md) file for details of working in agile methodology.*

## Initial Setup

### 1. Clone the repository on your local machine (you need to have [git](https://git-scm.com/downloads) installed)

```
git clone https://github.com/AGH-IT-tools-Group-1/meshi.git
```

## Issue Creation Process

1. Create an issue describing a task you want to work on. See the [AGILE_WORKFLOW](AGILE_WORKFLOW.md) file for Issue creation details.  

2. Tag the issue with a relevant tag (eg. **#Bug**, **#Task**, **#User Story**)

3. Get the issue **approved** and **scored/evaluated** (assign story points) by the rest of the team members.

## Development Process

### 1. Work on the issue using the corresponding branch

```sh
# create a new branch named #issue-number from #dev branch
# (eg. **Issue #235** -> **Branch #235**)
# to do so, checkout (swith) to #dev branch
$ git checkout dev

# now create the specific new branch (git automatically will base the new branch on #dev)
# switches you to the specific branch and creates it
$ git checkout -b 235

# publish the newly created branch, and track it remotely
$ git push -u origin 235

# do some changes to the files
```

### 2. After finishing a part of the job commit changes

```sh
# when finished doing a particular bit of work
# stage the files destined for commit
# eg. stage all the changed files:
$ git add .
# eg. stage specific file
$ git add example.html
# eg. stage specific folder (replace with folder path)
$ git add exampleFolder

# unstage accidentaly staged file
$ git reset HEAD example.html

# you can check the status of files using
$ git status
```

Before commiting see [committing rules](#2-commits)

```sh
# commit changed files
$ git commit -m "Short message describing done changes"
```

### 3. Pull possible changes to your branch from remote repository and resolve all the merge conflicts (fix conflicting commits before pushing changes)

```sh
$ git pull origin 235
# or simply
$ git pull
```

### 4. Send your changes from your local machine to the remote repository (everybody will be able to get them)

```sh
$ git push
```

### 5. When finished working on the Issue open a new Pull Request. (See [Pull Request Process Section](#pull-request-process))

## Pull Request Process

### 1. Open a new Pull Request with the **#dev** as the destination branch. (__Never__ merge directly to **#main** branch!)

### 2. Ensure any install or build dependencies are removed before the end of the layer when doing a build.

### 3. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.

### 4. Rerquest reviews from at least two other team members.

### 5. Resolve possible emerging issues highlighted by the reviewers.

### 6. You may merge the Pull Request in once you have the sign-off of **two other developers**, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### 7. Resolve merge conflicts with destination branch

```sh
# get the lastest changes from destination branch
$ git pull origin dev

# resolve all the merge conflicts localy before merging
# commit resolved merge conflicts
```

### 8. Merge branches

```sh
# change branch to your destination branch
$ git checkout dev

# merge your branch into destination branch
$ git merge 235
```

## Black workflow - linting python code  
### 1. Usage
Execute the following command in the project root directory if you are planning to commit the changed python files.
```sh
$ black -q */*.py
```

## Testing  
### 1. When developing with Django, you must create adequate tests

### 2. Before pushing your code to the repository, check if all tests are passed, otherwise resolve problems locally first

### 3. pull request *will not* be merged without tests

###  Command example
Execute the following command ...
```sh
...
```
