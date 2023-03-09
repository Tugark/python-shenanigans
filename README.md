# python-shenanigans

This repository showcases how you get setup with a basic development environment for python in WSL and how to work with WSL-based python environments.

You can access databases, dockerized services like redis and anything else you're used to doing with pure Windows-based development environments, but with the added benefit of native support for many packages (especially if they are dependent on system libraries).

It is based on using pyenv and pipenv for a smooth developer experience. While you might setup these tools on Windows as well, it is easier to do this on *nix systems as these tools (and a lot of python packages) are optimized for *nix environments (ever had to fix missing system dependencies when running `pip install my-very-obscure-but-important-package`?).

## Basic Setup

1. Install WSL
2. Install [pyenv](https://github.com/pyenv/pyenv); I prefer the GIT checkout way.
    1. Make sure to follow *all* steps, especially the dependency part (!)
    2. Run `pyenv install 3.11.2` and `pyenv global 3.11.2` to install your first python version and set it as a default
    3. Run `python --version` to check whether it all worked
3. Install [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) by running `pip install pipenv` - this will install pipenv as a global extension attached to your previously defined python version.


## Creating a new project

1. Navigate to your project folder
2. Run `pipenv --python 3.11.2` to create a new (empty) venv with a specific version or run `pipenv install` directly, using your current global python version (alternatively, install needed packages directly)
3. Run `pipenv install requests` to install the requests package from pypi, or use `pipenv install requests==2.28.*` to pin-down versions.
4. You're good to go! To check whether all worked, you can run a shell (`pipenv shell`) or run any commands like `pipenv run python`, and check whether it worked:
```
>>> import requests
>>> result = requests.get('https://api.chucknorris.io/jokes/random')
>>> result.text
'{"categories":[],"created_at":"2020-01-05 13:42:26.766831","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"XwAvSG6cTl2uOC3wAEWF0g","updated_at":"2020-01-05 13:42:26.766831","url":"https://api.chucknorris.io/jokes/XwAvSG6cTl2uOC3wAEWF0g","value":"Chuck Norris sank the Titanic because it was his nickname."}'
```

## Using a legacy project

Given the fact that you might have to develop projects other colleagues made during times where dinosaurs still roamed the earth, you might not be able to use your bleeding-edge nightly python build.

If they were using pipenv, however, your current setup is so clever it automagically invokes pyenv to install the python version specified in your Pipfile whenever you run `pipenv install`.

Try it - clone the repository and run `pipenv install` in the `./legacy-project` folder - it uses an older (and oddly specific) Python version, which you can again verify by running the following command:
```
Python 3.9.4 (default, Mar  5 2023, 17:52:58)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> import pandas
>>> result = requests.get('https://api.chucknorris.io/jokes/random')
>>> result.text
'{"categories":[],"created_at":"2020-01-05 13:42:29.569033","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"mkTmoSv1Q2mQFmcgu1keMA","updated_at":"2020-01-05 13:42:29.569033","url":"https://api.chucknorris.io/jokes/mkTmoSv1Q2mQFmcgu1keMA","value":"Most experts are not entirely sure Chuck Norris has yet achieved self-awareness."}'
>>> df = pandas.DataFrame()
>>> df
Empty DataFrame
Columns: []
Index: []
```
As you can see, the correct python version was installed as well as the `pandas` and `requests` package.

## Developing apps in WSL

Now that your setup is complete, you can begin to develop all your applications, using any IDE on your host such as VSCode. You can, for example, use the Django project in the `./web-project` folder. To start it, run `pipenv run python manage.py runserver` and it will launch your application on http://127.0.0.1:8000/ :)

Any changes made in your IDE (even if it's on the windows host) will be directly applied, without any delay. As an example, you can edit the `./web-project/awesomewebsite/views.py` file to change the output displayed when accessing http://127.0.0.1:8000/test or http://127.0.0.1:8000/.

### Setting up your IDE

As with node applications, you have to specify the python interpreter. Because we're creating virtual environments in python that work a bit differently from the node concept (with its `node_modules` folder), you have to specify the path to the python interpreter.

Luckily, VSCode works nicely with WSL, so it finds all virtual environments directly. Just choose the correct interpreter by selecting the python version in the tab at the bottom.

After that, your IDE will have full autocomplete set up.

TODO: pycharm, add images
