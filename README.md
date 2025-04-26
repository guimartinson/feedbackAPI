# User Feedback API

Simple web application where users can submit feedback using a form.  
Feedbacks are stored in a JSON file and can be retrieved as JSON data.

## Features
- Submit feedback with name, comment, and rating
- View all feedbacks (JSON output)
- Data is saved in a simple JSON file
- Basic form validation
- Basic routing (GET and POST)

## Tech Stack
- Python 3
- Flask
- HTML5

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/guimartinson/feedbackAPI
   cd feedback_api
Install Flask:

bash
Copy
Edit
pip install flask
Run the app:

bash
Copy
Edit
python app.py
Open your browser and go to:

arduino
Copy
Edit
http://localhost:5000/
Project Structure
bash
Copy
Edit
feedback_api/
│
├── app.py           # Main Flask app
├── templates/
│   └── form.html    # Feedback form (HTML)
├── feedbacks.json   # Storage for feedbacks (created after first feedback)
API Endpoints
GET /feedbacks → Returns all feedbacks as JSON

POST /submit → Submit a feedback through form# feedbackAPI
