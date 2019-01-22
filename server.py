"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

SHADINESS = [
    'ashy', 'dumb', 'slow', 'tacky', 'messy', 'uninteresting',
    'meh', 'stingy', 'thirsty', 'needy']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        <body>
            <a href="http://localhost:5000/hello">Form Page</a></html>
            <br>
            <br>Hi! This is the home page.
        </body>
    </html>
    """
@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
        <a href="http://localhost:5000">Home</a>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <input type="radio" name="nice_thing" value="awesome">awesome
          <input type="radio" name="nice_thing" value="terrific">terrific
          <input type="radio" name="nice_thing" value="fantastic">fantastic
          <input type="radio" name="nice_thing" value="neato">neato
          <input type="radio" name="nice_thing" value="fantabulous">fantabulous
          <input type="radio" name="nice_thing" value="wowza">wowza
          <input type="radio" name="nice_thing" value="oh-so-not-meh">oh-so-not-meh
          <input type="radio" name="nice_thing" value="brilliant">brilliant
          <input type="radio" name="nice_thing" value="ducky">ducky
          <input type="radio" name="nice_thing" value="coolio">coolio
          <input type="radio" name="nice_thing" value="incredible">incredible
          <input type="radio" name="nice_thing" value="wonderful">wonderful
          <input type="radio" name="nice_thing" value="smashing">smashing
          <input type="radio" name="nice_thing" value="lovely">lovely
          <br><br>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss"><input type="text" name="person">
          <br>
          <input type="radio" name="insult" value="ashy">ashy
          <input type="radio" name="insult" value="dumb">dumb
          <input type="radio" name="insult" value="slow">slow
          <input type="radio" name="insult" value="tacky">tacky
          <input type="radio" name="insult" value="messy">messy
          <input type="radio" name="insult" value="uninteresting">uninteresting
          <input type="radio" name="insult" value="meh">meh
          <input type="radio" name="insult" value="stingy">stingy
          <input type="radio" name="insult" value="thirsty">thirsty
          <input type="radio" name="insult" value="needy">needy
          <br><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("nice_thing")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss", methods = ["GET"])
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
