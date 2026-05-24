# ════════════════════════════════════════════════
# IMPORTS
# ════════════════════════════════════════════════

# The standard library module for interacting with your operating system.
import os

# Imports the function that reads your .env file.
from dotenv import load_dotenv

# Standard library module for reading/writing JSON files.
# JSON (JavaScript Object Notation) is just a text format that looks like
# Python dicts/lists
import json

# Imports the OpenAI *client class* from the openai package.
# This is the object you'll use to talk to the API.
from openai import OpenAI

# ════════════════════════════════════════════════
# FUNCTIONS
# ════════════════════════════════════════════════

def configure():
    """
    Reads your .env file and loads every line into os.environ (a dict of
    environment variables your whole process can see).

    os.getenv("OPENAI_API_KEY") would return the key string
    """
    # Looks for a file called .env in the current directory
    load_dotenv() 

def load(prompt_path,model):
    """
    Loads the .json file containing the prompt and model parameters.

    The `with` keyword is a context manager — it automatically closes the file
    when the indented block ends, even if an error occurs.
    `f` is the file object (a handle to read from).   
    """

    # Opens the file "default.json" in read mode ("r").
    with open(prompt_path, "r") as f: 

        # Reads the entire file and parses it from JSON text into a Python dict
        config = json.load(f) 

        # Can assign the model
        config["model"] = model

    return config

def run(config):
    """
    For a given config dict, makes an API call and returns the response
    """

    # Creates an instance of the OpenAI client. This will read your API key from the environment variable OPENAI_API_KEY.
    client = OpenAI() 
    
    # The API call 
    response = client.chat.completions.create(
        model=config["model"],
        messages=config["messages"],
        temperature=config["temperature"],
        max_completion_tokens=config["max_completion_tokens"],
        frequency_penalty=config["frequency_penalty"],
        presence_penalty=config["presence_penalty"],
    )

    # Extract the response text
    reply_text = response.choices[0].message.content

    output = config["messages"] + [{"role": "assistant", "content": reply_text}]

    return {
        "model": config["model"],
        "messages": output,
        "temperature": config["temperature"],
        "max_completion_tokens": config["max_completion_tokens"],
        "frequency_penalty": config["frequency_penalty"],
        "presence_penalty": config["presence_penalty"],
        "LING_buy_string": config["LING_buy_string"],
        "prompt_path": config["prompt_path"],
        "canary": config["canary"],
    }

def save(output_path,result):
    """
    Saves the result dict to a .json file at the specified path.
    """
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)