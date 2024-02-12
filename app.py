from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "blue": "#2980b9",      # v1
    "green": "#16a085",     # v2
    "red": "#e74c3c",       # v3
    "pink": "#be2edd",      # v4
    "yellow": "#ffff00",    # v5
    "orange": "#ffa500",    # v6
    "darkblue": "#30336b",  # v7
    "dark": "#000000"       # v7
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# with open('APP_VERSION', 'r') as file:
#     APP_VERSION = file.read().replace('\n', '')

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
VERSION_FROM_ENV = os.environ.get('APP_VERSION') or "v1"

# Generate a random color
COLOR = random.choice(["red", "green", "blue", "darkblue", "pink", "yellow", "dark", "orange"])


@app.route("/")
def main():
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[COLOR], version=VERSION_FROM_ENV)


@app.route("/color")
def color():
    return COLOR


@app.route("/version")
def version():
    return "Hello, Application Version: {}".format(VERSION_FROM_ENV)


@app.route("/hostname")
def hostname():
    return "Hello, Application Hostname: {}".format(socket.gethostname())


@app.route("/info")
def info():
    return "Hello, Application Version: {} ; Color: {}".format(VERSION_FROM_ENV, COLOR)


@app.route("/all")
def all():
    return "Hello, Application Version: {} ; Color: {} ; Hostname: {} ".format(VERSION_FROM_ENV, COLOR, socket.gethostname())


if __name__ == "__main__":

    print(" This is a sample web application that displays a colored background. \n"
          " A color can be specified in two ways. \n"
          "\n"
          " 1. As a command line argument with --color as the argument. Accepts one of " + SUPPORTED_COLORS + " \n"
          " 2. As an Environment variable APP_COLOR. Accepts one of " + SUPPORTED_COLORS + " \n"
          " 3. If none of the above then a random color is picked from the above list. \n"
          " Note: Command line argument precedes over environment variable.\n"
          "\n"
          "")

    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    if args.color:
        print("Color from command line argument =" + args.color)
        COLOR = args.color
        if COLOR_FROM_ENV:
            print("A color was set through environment variable -" + COLOR_FROM_ENV + ". However, color from command line argument takes precendence.")
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + COLOR_FROM_ENV)
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + COLOR)

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    # Run Flask Application
    app.run(host="0.0.0.0", port=9000)
