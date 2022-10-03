# Project setup
This project has a frontend using `npm` as package manager, [Vue](https://vuejs.org/) as the javascript framework and [Tailwind](https://tailwindcss.com/) as the CSS framework. The backend is written in Python with [Django](https://www.djangoproject.com/) as the Python framework. 

In order to get everything up and running we'll need to install the latest node version together with `npm`, `npm` will then care about all other dependencies. 
For the backend, we'll need to create a virtual python environment in which we'll then install all backend dependencies.

## Clone the repository
In order to start, you'll need to clone the repository first, you can do so either by using the https or the ssh link to the repository

```shell
# here we use the commonly used https link
git clone https://github.com/TheInspiredConjurer/Online-Questionnaire-System.git
```

For all other commands you can find below, it is expected that you are in the `Online-Questionnaire-System` directory, so make sure to go their first
```shell
cd /path/to/Online-Questionnaire-System
```

## Node & npm for the frontend
in case you don't have node installed already, I can recommend using [nvm](https://github.com/nvm-sh/nvm) a Node Version Manager. It allows installing and switching between node version quite easily. 

Install it by executing the command mentioned in [Installing and updating](https://github.com/nvm-sh/nvm#installing-and-updating).

After that installing the latest version is as easy as executing
```shell
nvm install
```

You can verify the successful installation by asking 
```shell
node --version
# -> should equal the latest node version, v18.10.0 when this document was created

npm --version
# -> should equal the latest npm version, 8.19.2 when this document was created
```

## Virtual python environment and pg_config for the backend
### Python 3
First make sure you have Python 3 installed, you can do so by executing
```shell
python3 --version
# -> Python 3.*.* (the currently latest is 3.10.7, but any LTS is ok as well)
```

In case this fails, please make sure to install Python first. Here are some possibilities for Mac OS, Ubuntu/Windows WSL and Windows

#### macOS
[Homebrew](https://brew.sh/index_de) is a powerful package manager for macOS. Once installed one can install the latest python version by simply executing

```shell
brew install python
```

#### Ubuntu / Windows WSL
For Ubuntu it is recommended to use the "advanded packaging tool" `apt` and add an additional "personal package archive" `ppa` that holds the latest python release

```shell
# 1. it's recommended to update and upgrade the current packages and their archives
sudo apt update && sudo apt upgrade

# 2. allow adding additional ppas
sudo apt install software-properties-common -y

# 3. add the deadsnake ppa, that holds the newest python releases
sudo add-apt-repository ppa:deadsnakes/ppa -y

# 4. install python 3.10 via apt
sudo apt install python3.10
```

#### Windows & default
You can install and download Python from their [download website](https://www.python.org/downloads/)

### Virtual environment
Once python is installed, we can progress with setting up a virtual environment and using it for the backend

```shell
# create the virtual environment
python3 -m venv .venv

# activate it
source .venv/bin/activate
```

### pg_config
In order to build some backend dependencies, we need `pg_config`. Depending on the OS there are different installation ways

#### macOS
One can install it via [Homebrew](https://brew.sh/index_de) as it is part of postgres

```shell
brew install postgresql
```

#### Ubuntu / Windows WSL
In Ubuntu, it is part of the `libpq-dev` library. One can install it via 

```shell
sudo apt install libpq-dev
```

## install the dependencies
### frontend
The frontend dependencies are all mentioned in `frontend/package.json`. In order to install them, we need `npm`

```shell
# go into the frontend directory
cd frontend

# install the dependencies
npm install
```

### backend
The backend dependencies are all mentioned in `backend/requirements.txt`. In order to install we first need to make sure to use our created environment, and then we can use `pip` (the package installer for python)

```shell
# activate the virtual environment
source .venv/bin/activate

# go into the backend directory
cd backend

# install the dependencies
pip3 install -r requirements.txt
```

## run the application
### backend
First you'll need to apply the most recent migrations, and then you can start the server

```shell
# make sure to use the correct environment
source .venv/bin/activate

# go into the backend directory
cd backend

# migrate the local database
python3 manage.py migrate

# start the server
python3 manage.py runserver
```

The output will tell you on which port you can find your server.

### frontend
The available `npm run` scripts are mentioned in `frontend/package.json`. In order to run a local development server, we need to execute the `dev` script

```shell
# go into the frontend directory
cd frontend

# run the dev server
npm run dev
```

The output will tell you on which port you can find the website on your local machine.

