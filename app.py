import os
import heroku3

from flask import Flask, render_template, request, redirect

DEBUG = "NO_DEBUG" not in os.environ
PORT = int(os.environ.get("PORT", 5000))
HKEY = os.environ.get("API_TOKEN")

app = Flask(__name__)


def run_one_off():
    heroku_conn = heroku3.from_key(HKEY)
    app = app = heroku_conn.apps()['one-off-demo']
    dyno = app.run_command_detached('python run_one_off.py', size="standard-1x")
    return dyno


@app.route('/')
def index():
    """Landing page."""
    return render_template("hello.html")


@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    """Read the file and put upload in worker queue."""
    if request.method == "POST":
        run_one_off()
        return render_template('success.html')
    else:
        return render_template('success.html')
        # return redirect('/bucketlist')


if __name__ == '__main__':
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
