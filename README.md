# Mettaur
A multipurpose, self hosted Discord bot written in Python.

## Features (WIP)

At the moment there are too many commands to list them all, I'll eventually make a website with all the commands with their usage and examples. For the time being, I'm working on making a proper help command.

## Installation and Usage

### On your machine

Creating a Python virtual environment is optional, but recommended, click [here](https://docs.python.org/3/library/venv.html#venv-def) to learn how to make your own.

Install all the necessary requirements from the **requirements.txt** file.

```
pip install -r requirements.txt
```

Make a copy of the **.env.template** file and name it **.env**, this is where you'll place your Discord bot token and other default variables. (If you don't have one, go [here](https://discord.com/developers/docs/intro) for Discord's developer portal documentation)

Your **.env** file should look like this:

```.env
BOT_TOKEN = Your token goes here
BOT_PREFIX = Your prefix goes here
BOT_STATUS = The status the bot will display
```

Lastly, run the **main.py** script located in the **src** directory

```
python main.py
```

Once you run the script, you'll be asked whether you want to run the bot in **normal** mode or **debug** mode. If you don't plan on working with the bot's code just use normal mode, if you're experiencing errors with any of the bot's functionalities, run it on debug mode and open a new issue, attaching the console output.

### Using a Docker image

TBD

## Contributing

I'm currently working on this project by myself, and I intend to keep it that way for now. Feel free to fork the repo and make changes as you see fit. Do remember that I won't be able to help as much if you're working with a modified version of the bot.
