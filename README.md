# Heroku + webapp2 + python 2.7 starter

This is a sample repository to help you get started
with `heroku` and `webapp2` framework.

## Instructions

### 1. Prerequisites

Make sure you have `git`, `python v2.7.16` and `pip` installed on your system.
* [Git installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python installation instructions](https://wiki.python.org/moin/BeginnersGuide/Download)
* [Pip installation instructions](https://pip.pypa.io/en/stable/installing/)

<details>
  <summary>Why?</summary>

  *Git* is a widely used "version control" system. In short, it helps organise
  changes that you make to your project and makes it possible for
  several people to work on one codebase.  
  *Pip* is a "package installer" for python libraries.
  With it you can install popular python libs (like `webapp2`) to your system from the command line.
</details>

### 2. Fork this repo
If you need help on forking repositories,
see [this article](https://help.github.com/en/articles/fork-a-repo)

### 3. Using git, clone the the forked repo to your computer

Assuming you forked this repo to `<your-github-account>`, open your terminal and run this command

<pre><code>git clone git@github.com:<b>&lt;your-github-account&gt;</b>/heroku-webapp2-python2-starter.git
</code></pre>

### 4. Install project dependencies

<!-- *(TODO: Describe how to use virtualenv (for python2) or venv (for python3))* -->
In your terminal, make sure to navigate to this project's
folder (`cd heroku-webapp2-python2-starter`).  
Then, run this command:

```
pip install -r requirements.txt
```

### 5. Install heroku

<details>
  <summary>Why?</summary>

  *Heroku* is a platform that allows you to deploy your web application
  at `<your-app-name>.herokuapp.com`
</details>

First, create a Heroku account on https://heroku.com  
Then, see [heroku installation instructions](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
After installing heroku, you need *login* to heroku in your terminal by
running `heroku login` command. See
[this page for more help](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)


<!-- This repository already has a "heroku app" associated with it.
For new repositories, you need to "create" a heroku app first:
https://devcenter.heroku.com/articles/creating-apps -->

### Run locally

#### Mac and Linux

Now that you have `heroku` installed, run this command in the terminal
from your project's folder:

```
heroku local
```

#### Windows

On windows, you need to run a different command:
```
heroku local -f Procfile.dev-windows
```

#### Check if it works

You should now be able to open your browser and navigate to
`localhost:5000`

🎉 If you see the "hello" message, then congratulations! You have a working
web application on your computer!

#### Stopping the server
`heroku local` command launches a local "server" which accepts http requests.  
To stop this server, press <kbd>ctrl + c</kbd> (<kbd>command + c</kbd> on Mac).

### Deploy

<details>
  <summary>Why?</summary>

  So far we have made the web application available on your computer.
  But we want to share the app with the world and make it available on
  the internet.
  Here's where `heroku` comes in. It has a couple of commands that make it
  quite easy to "copy" your web application code to the heroku servers.
</details>

#### Create a heroku app

First, make sure you have successfully
[installed heroku and logged in](#5-Install-heroku).

Then, think of a name for your web app. Run this command:

```
heroku create <your-app-name>
```

If the name is not taken and all goes well, run this command next:
```
git push heroku master
```

When you run this command for the first time, it might take some time.
But once it's done, your web application should be available on
`https://<your-app-name>.herokuapp.com`.

🎉 Congratulations! Now you can share your web application with other by giving
them a link to your herokuapp!

#### How to deploy future changes

After you work on your web application and make some changes that you are
satisfied with, you would want to deploy those changes ("update" your live
herokuapp).

Here's what you need to do:

1. Commit changes to git  
    ```
    git add .
    git commit -m "description of changes"
    ```
2. Run the command:
    ```
    git push heroku master
    ```

🎉 All done! Have a happy time developing your app!
