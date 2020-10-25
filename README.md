# Meshi

Personal meal planner

## Initial setup

1. ### Install **PostgreSQL v12.04** database

```sh
# for debian based linux system
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get -y install postgresql-12
```
For other operating systems see the official [download website](https://www.postgresql.org/download/) for PostgreSQL.

2. ### Install Python v3.8.5 
```sh
# for debian based linux system
$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt-get update

$ sudo apt install python3.8 

$ python3.8 -V
# last command sholud yeald "Python 3.8.5"
```

For other operating systems see the official [download website](https://www.python.org/downloads/release/python-385/) for Python.

3. ### Install **pip** - a package manager for Python

```sh
# for debian based linux system
$ apt install python3-pip
```

4. ### Install necesary python packages using pip

```sh
# in repository root
$ pip3 install -r requirements.txt
```

5. ### Run the test server

```sh
# run the test server to verify correct instalation
$ python3 meshi/manage.py runserver
```

## Project [licence](meshi/LICENSE) - MIT

## How to contribute

For contributing guidelines & steps checkout [CONTRIBUTING](meshi/CONTRIBUTING.md) file.

To check the list of project contributors view the [contributors list](Contributors.csv).

## Technologies used

| Resource link      | Description | License |
| :------------- | :----------: | -----------: |
|  [Python v3.8.5](https://www.python.org/) | The main programming language used in the project | [ZERO-CLAUSE BSD LICENSE](https://docs.python.org/3/license.html#zero-clause-bsd-license-for-code-in-the-python-release-documentation) |
|    [Django v3.1](https://www.djangoproject.com/) | Python Framework | [Corporate Contributor License Agreement](https://media.djangoproject.com/foundation/ccla.pdf) |   
|    [HTML](https://html.spec.whatwg.org/) | Defines website pages structure | Open Web |
|    [CSS](https://www.w3.org/Style/CSS/Overview.en.html) | Website stylization tool | Open Web |
|   [PostgreSQL](https://www.postgresql.org/) | The project database | [The PostgreSQL Licence (PostgreSQL)](https://opensource.org/licenses/postgresql) |
