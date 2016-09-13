import os


from flask import Flask, render_template, request, redirect

DEBUG = "NO_DEBUG" not in os.environ
PORT = int(os.environ.get("PORT", 5000))

app = Flask(__name__)


@app.route('/')
def index():
    """Landing page."""
    return render_template("hello.html")


@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    """Read the file and put upload in worker queue."""
    if request.method == "POST":
        return render_template('success.html')
    else:
        return render_template('success.html')
        # return redirect('/bucketlist')


if __name__ == '__main__':
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
