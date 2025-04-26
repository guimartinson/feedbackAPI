from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os

app = Flask(__name__)


if os.path.exists('feedbacks.json'):
    with open('feedbacks.json', 'r') as f:
        feedbacks = json.load(f)
else:
    feedbacks = []

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    comment = request.form.get('comment')
    rating = request.form.get('rating')

    if not name or not comment or not rating:
        return "Missing fields", 400

    feedback = {
        'id': len(feedbacks) + 1,
        'name': name,
        'comment': comment,
        'rating': rating
    }
    feedbacks.append(feedback)

    with open('feedbacks.json', 'w') as f:
        json.dump(feedbacks, f, indent=2)

    return redirect(url_for('index'))

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify(feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
