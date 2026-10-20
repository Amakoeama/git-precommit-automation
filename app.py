from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CI/CD Calculator Application</title>
    </head>
    <body>
        <h1>CI/CD Calculator Application</h1>
        <p>Welcome to the ITSD-4350 Midterm Project.</p>
        <p>This application demonstrates automated builds,
        testing, and continuous integration using GitHub Actions.</p>
        <p>Status: Application Running Successfully</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
