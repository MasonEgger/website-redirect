import os
import logging
from flask import Flask,redirect


app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(os.environ.get("REDIRECT_TO", "https://www.google.com"), code=301)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    app.run(host='0.0.0.0', port=8080)
