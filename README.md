# Sample Discord Bot written in Python
Sample Discord Bot template written in Python using Discord.py, with the configurations to host on Heroku platform.

<br />

Description
======
Discord bot written in Python to act as a chat bot in Discord application. This repo is using the old version of Discord.py (1.3.4) so some of the stuffs may not be compatible with the latest version. Uploaded here for reference purposes.

Requirements
======
Python 3.6 or later

Notable Packages and Dependencies used
======
* discord.py - API wrapper for Discord in Python

* Create an application for Discord bot in Discord Developer platform.

* A heroku account (optional, can run locally)

How to Run
======
Fill up the credentials in config/config.json file, install the necessary requirements using pip and run the app file

### `python app.py`

Hosting on Heroku
======
To host on Heroku, these are needed as prerequisite:

* Install Heroku

* Procfile - To specify the dyno worker

* runtime.txt - To specify the Python version

<br />

After that, follow the steps in [Official Documentation] (https://devcenter.heroku.com/articles/git) for Heroku to deploy with Git and it will handle the rest of the deployments.