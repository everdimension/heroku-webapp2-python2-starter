# Heroku + webapp2 + python 2.7 starter

This is a sample repository to help you get started
with `heroku` and `webapp2` framework.

## Development

This repository already has a "heroku app" associated with it.
For new repositories, you need to "create" a heroku app first:
https://devcenter.heroku.com/articles/creating-apps

### Install heroku

```
brew update
brew install heroku
```

### Install dependencies

*(TODO: Describe how to use virtualenv (for python2) or venv (for python3))*

```
pip install -r requirements.txt
```

### Run locally

```
heroku local
```

### Deploy

1. Commit changes to git
2. Run the command:
```
git push heroku master
```

## Project specifics

The following files are required by heroku:
```
- Procfile
- requirements.txt
- runtime.txt
```

Dependency `psycopg2==2.7` is not needed for the projects, but heroku fails
to deploy if you don't list it, because by default it tries to install `psycopg2==2.6`,
which breaks the build ¯\\\_(ツ)\_/¯
