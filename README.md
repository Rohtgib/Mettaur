# Mettaur
A multipurpose, self hosted Discord bot written in Python.

## Features (WIP)

### Moderation
- **Clean messages in a channel**  `m!wipe`
- **Kick users** `m!kick`
- **Ban users** `m!ban`

## Installation and Usage

### On your machine

Creating a Python virtual environment is optional, but recommended, click [here](https://docs.python.org/3/library/venv.html#venv-def) to learn how to make your own.

Install all the necessary requirements from the **requirements.txt** file.

```
pip install -r requirements.txt
```

Make a copy of the **.env.template** file and name it **.env**, this is where you'll place your Discord bot token. (If you don't have one, go [here](https://discord.com/developers/docs/intro) for Discord's developer portal documentation)

Your **.env** file should look like this:

```.env
BOT_TOKEN = Your token goes here
```

Lastly, run the **main.py** script located in the **src** directory

```
python main.py
```

### Using a Docker image

TBD

## Contributing

I'm currently working on this project by myself, and I intend to keep it that way for now. Feel free to fork the repo and make changes as you see fit. 
