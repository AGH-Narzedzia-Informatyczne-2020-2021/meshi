# Meshi

Personal meal planner

## Table of contents:  
### 1. [Initial setup](#id1)  
### 2. [Project documentation on Overleaf](#id2)  
### 3. [Project licence - MIT](#id3)
### 4. [How to contribute](#id4)
### 5. [Technologies used](#id5)  

    
## Initial setup<a id="id1"></a>

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

## Project documentation on [Overleaf](https://www.overleaf.com/project/5f952cfe700e1900017792fb)<a id="id2"></a>

## Project [licence](meshi/LICENSE) - MIT<a id="id3"></a>

## How to contribute<a id="id4"></a>

For contributing guidelines & steps checkout [CONTRIBUTING](CONTRIBUTING.md) file.

To check the list of project contributors view the [contributors list](Contributors.csv).

## Technologies used<a id="id5"></a>

| Resource link                                        |                    Description                    |                                                                                                                                License |
| :--------------------------------------------------- | :-----------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------: |
| [Python v3.8.5](https://www.python.org/)             | The main programming language used in the project | [ZERO-CLAUSE BSD LICENSE](https://docs.python.org/3/license.html#zero-clause-bsd-license-for-code-in-the-python-release-documentation) |
| [Django v3.1](https://www.djangoproject.com/)        |                 Python Framework                  |                                         [Corporate Contributor License Agreement](https://media.djangoproject.com/foundation/ccla.pdf) |
| [HTML](https://html.spec.whatwg.org/)                |          Defines website pages structure          |                                                                                                                               Open Web |
| [CSS](https://www.w3.org/Style/CSS/Overview.en.html) |             Website stylization tool              |                                                                                                                               Open Web |
| [PostgreSQL](https://www.postgresql.org/)            |               The project database                |                                                      [The PostgreSQL Licence (PostgreSQL)](https://opensource.org/licenses/postgresql) |
