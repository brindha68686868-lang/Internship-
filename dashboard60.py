from flask import Flask, render_template_string

app = Flask(__name__)

dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: auto;
        }
        .card {
            display: inline-block;
            width: 200px;
            margin: 20px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        h1 {
            color: #333;
        }
        .value {
            font-size: 30px;
            color: blue;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flask Dashboard</h1>

        <div class="card">
            <h3>Users</h3>
            <div class="value">{{ users }}</div>
        </div>

        <div class="card">
            <h3>Orders</h3>
            <div class="value">{{ orders }}</div>
        </div>

        <div class="card">
            <h3>Revenue</h3>
            <div class="value">₹{{ revenue }}</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    data = {
        "users": 1250,
        "orders": 350,
        "revenue": 75000
    }
    return render_template_string(dashboard_html, **data)

if __name__ == '__main__':
    app.run(debug=True)