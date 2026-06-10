from flask import Flask

app = Flask(__name__)

@app.route("/")
def portfolio():
    return """
    <h1>Brindha's Portfolio</h1>

    <h2>About Me</h2>
    <p>Python Developer and Technology Enthusiast</p>

    <h2>Skills</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>SQL</li>
        <li>Git & GitHub</li>
    </ul>

    <h2>Projects</h2>
    <ul>
        <li>Attendance Management System</li>
        <li>Library Management System</li>
        <li>Weather App</li>
    </ul>

    <h2>Contact</h2>
    <p>Email: example@email.com</p>
    """

if __name__ == "__main__":
    app.run(debug=True)