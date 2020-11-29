# Meshi

Personal meal planner

## Table of contents  

> ### 1. [Initial setup](#initial-setup)
> ### 2. [Project documentation on Overleaf](#project-documentation-on-overleaf)  
> ### 3. [Project licence - MIT](#project-licence---mit)
> ### 4. [How to contribute](#how-to-contribute)
> ### 5. [Our gists](#our-gists)  
> ### 6. [Technologies used](#technologies-used) 
> ### 7. [Assets used](#assets-used) 




        
## Initial setup

### 1. Install **PostgreSQL v12.04** database

```sh
# for debian based linux system
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get -y install postgresql-12
```

For other operating systems see the official [download website](https://www.postgresql.org/download/) for PostgreSQL.

### 2. Create a PostgreSQL User and Database

```sh
# enter posrgresql cli as postgres user (adminn access)
$ sudo -u postgres psql
```

```sql
# create the project database named 'meshi_db'
CREATE DATABASE meshi_db;
```

For the SECRETS.py file containing true database password contact a [Meshi developers](https://github.com/orgs/AGH-Narzedzia-Informatyczne/teams/meshi-developers) team member.

```sql
# create database user named 'meshi_user' with password
CREATE USER meshi_user WITH ENCRYPTED PASSWORD 'not_the_right_password';
```

```sql
# modify connection parameters
ALTER ROLE meshi_user SET client_encoding TO 'utf8';
ALTER ROLE meshi_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE meshi_user SET timezone TO 'UTC';
```

```sql
# grant permissions to the user
GRANT ALL PRIVILEGES ON DATABASE meshi_db TO meshi_user;
```

```sh
# exit the SQL prompt
\q
```

### 3. Install Python v3.8.5

```sh
# for debian based linux system
$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt-get update

$ sudo apt install python3.8

$ python3.8 -V
# last command sholud yeald "Python 3.8.5"
```

For other operating systems see the official [download website](https://www.python.org/downloads/release/python-385/) for Python.

### 4. Install **pip** - a package manager for Python

```sh
# for debian based linux system
$ apt install python3-pip
```

### 5. Install necessary python packages using pip

```sh
# in repository root
$ pip3 install -r meshi/requirements.txt
```

### 6. Install [Black](https://github.com/psf/black) - Python linter

```sh
#Black can be installed by running  
$ pip3 install black
#It requires Python 3.6.0+ to run but you can reformat Python 2 code with it, too.
```

### 7. Create .env file in project_root/meshi

```sh
# move to directory containing manage.py file
$ cd /meshi
# create .env file containing project secrets
$ touch .env
```

Write secrets to file. For correct file content contact [Meshi developers](https://github.com/orgs/AGH-Narzedzia-Informatyczne/teams/meshi-developers) team member.

### 8. Apply migrations

```sh
# apply all migrations
$ python3 meshi/manage.py migrate
```

### 9. Create superuser (django admin)

```sh
# provide: username, email, password
# any credentials will do in development environment, e.g.
# username: admin
# email - blank
# password: admin
$ python3 meshi/manage.py createsuperuser
```

### 10. Run the test server

```sh
# run the test server to verify correct setup
$ python3 meshi/manage.py runserver
```

## Project documentation on [Overleaf](https://www.overleaf.com/project/5f952cfe700e1900017792fb)

## Project [licence](meshi/LICENSE) - MIT

## How to contribute

For contributing guidelines & steps checkout [CONTRIBUTING](CONTRIBUTING.md) file.

To check the list of project contributors view the [contributors list](Contributors.csv).

## Our gists

| Developer        |                                                 Gist #1                                                 |                                                       Gist #2                                                       |
| :--------------- | :-----------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| Mazur Aleksander |        [kolko_krzyzyk3x3](https://gist.github.com/Aleksander2a/b701448e05cc69c24070870e083476da)        |             [kolko_krzyzyk10x10](https://gist.github.com/Aleksander2a/6cce0ed5f621989691415f796fff3875)             |
| Karpiuk Jan      |            [python_calc.py](https://gist.github.com/Laronk/b973296a4c4292e11fc3e5f4f83a1622)            |               [python_try_except.py](https://gist.github.com/Laronk/3caea800b8766f2a7f9631fcfd266549)               |
| Henel Daniel     |                [add_item](https://gist.github.com/danielhenel/d651fff7476fe61fae9ee729d2d1779d)                                                                                         |     [copy_list](https://gist.github.com/danielhenel/106d7982e495533e3c32271fff25bf80)                                                                                                                |
| Gacek Piotr      |        [ciag_fibonacciego](https://gist.github.com/piotrekg35/1c4ca47814d7a80a980a121123ac980e)         |                     [str](https://gist.github.com/piotrekg35/cf06897c09441e63ba327a004dbbc2ba)                      |
| Szpunar Jakub    | [account_model_v1](https://gist.github.com/YgLK/27ab4f06ab80e0c3195ac52a5bd84e75#file-account_model_v1) | [custom_passw_validator](https://gist.github.com/YgLK/b6d818cdd23b1ab0be983b2166c48655#file-custom_passw_validator) |

## Technologies used

| Resource link                                        |                    Description                    |                                                                                                                                License |
| :--------------------------------------------------- | :-----------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------: |
| [Python v3.8.5](https://www.python.org/)             | The main programming language used in the project | [ZERO-CLAUSE BSD LICENSE](https://docs.python.org/3/license.html#zero-clause-bsd-license-for-code-in-the-python-release-documentation) |
| [Django v3.1](https://www.djangoproject.com/)        |                 Python Framework                  |                                         [Corporate Contributor License Agreement](https://media.djangoproject.com/foundation/ccla.pdf) |
| [HTML](https://html.spec.whatwg.org/)                |          Defines website pages structure          |                                                                                                                               Open Web |
| [CSS](https://www.w3.org/Style/CSS/Overview.en.html) |             Website stylization tool              |                                                                                                                               Open Web |
| [PostgreSQL](https://www.postgresql.org/)            |               The project database                |                                                      [The PostgreSQL Licence (PostgreSQL)](https://opensource.org/licenses/postgresql) |

## Assets used  

| Description | Author |  License |
| :-----: | :-----: | :-----: |
| Repository social media image | [Freepik](http://www.freepik.com) | Free Freepik License(https://www.freepikcompany.com/legal#nav-freepik) |
