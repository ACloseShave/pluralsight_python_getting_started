# Importing Flask to convert to webapp
# Part of "Python - Getting Started" on Pluralsight.com


rom flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__.":
    app.run()
