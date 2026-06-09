from flask import Flask, render_template_string
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>API Integration Demo</title>
</head>
<body>
    <h1>Random User Information</h1>

    {% if user %}
        <p><b>Name:</b> {{ user['name']['first'] }} {{ user['name']['last'] }}</p>
        <p><b>Email:</b> {{ user['email'] }}</p>
        <p><b>Country:</b> {{ user['location']['country'] }}</p>
        <img src="{{ user['picture']['large'] }}" alt="User Photo">
    {% else %}
        <p>Unable to fetch data.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    try:
        response = requests.get("https://randomuser.me/api/", timeout=10)
        data = response.json()
        user = data["results"][0]
        return render_template_string(HTML, user=user)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)