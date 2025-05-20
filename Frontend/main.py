from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = 'submissions.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "datetime": request.form.get("datetime"),
        "location": request.form.get("location"),
        "constellation": request.form.get("constellation"),
        "star_count": int(request.form.get("star_count")),
        "weather": request.form.get("weather")
    }

    # Load existing data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            submissions = json.load(f)
    else:
        submissions = []

    # Add new data
    submissions.append(data)

    # Save back to file
    with open(DATA_FILE, 'w') as f:
        json.dump(submissions, f, indent=2)

    return jsonify({"message": "Observation submitted successfully!"}), 200

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            submissions = json.load(f)
    else:
        submissions = []

    return render_template('data.html', submissions=submissions)


if __name__ == '__main__':
    app.run(debug=True)
