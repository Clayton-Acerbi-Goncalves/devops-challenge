from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
        <head>
            <title>DevOps Challenge</title>
        </head>
        <body>
            <h1>Clayton Goncalves</h1>
            <h2>DevOps Challenge Completed!</h2>
            <p>Current date and time: {current_time}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
