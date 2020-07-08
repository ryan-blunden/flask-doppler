# Flask with Doppler

Simple Flask app using the [Doppler Universal Secrets Manager](https://doppler.com/) for fetching application configuration and secrets.

## Setting up Doppler

1. [Install Doppler](https://docs.doppler.com/docs/enclave-installation)
1. From a terminal, run:

``` sh
doppler login
```

1. Once logged in, open a new browser window and [sign in to Doppler](https://dashboard.doppler.com/)
1. In the Doppler Web UI, create a workspace
1. Then [create a project](https://docs.doppler.com/docs/enclave-project-setup)
1. Manually add 4 secrets to the development environment of the project with the following names and values:

``` sh
FLASK_APP: hello.py
FLASK_APP_VERSION: 0.0.1-DEV
FLASK_ENV: development
FLASK_SECRET:  #$$haio3%4425jf029-=!
```

1. In a terminal, cd into the `flask-doppler` directory, then run:

``` sh
# Configure Doppler fetch secrets to use for our project at this directory path on our machine
doppler enclave setup 
```

To check that the Doppler CLI can access the project and retrieve its secrets, run:

``` sh
doppler run env | grep FLASK
```

If you can see the 4 secrets output to the terminal, Doppler is ready to go!

## Setting up Flask

This app requires Python 3 and presumes knowledge about using Python virtual environments and installing packages.

``` sh
python3 -m venv ~/.virtualenvs/flask-doppler
source ~/.virtualenvs/flask-doppler/bin/activate
pip install pip -r requirements.txt --upgrade
```

1. [Install Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)

That's it!

## Running the app

Now lets use `doppler run` to call the `flask run` command which will inject our secrets as environment variables that Flask to access.

> NOTE: The environment variables retrieved by Doppler are **not** injected into the shell context in which you are running `doppler run` from.

``` sh
doppler run -- flask run
```

Now you should be able to access the app from [http://localhost:5000](http://localhost:5000)

## If you can't get the app working

Create a GitHub issue, including your OS, OS version, and Python version and I'll help you get things sorted.
