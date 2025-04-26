Here’s your full **README.md** you can copy and use right now:

---

# User Feedback API

Simple web application where users can submit feedback through a form.  
Feedbacks are saved in a JSON file and can be retrieved as a JSON list.

---

## Features
- Submit feedback with **name**, **comment**, and **rating**.
- View all submitted feedbacks as **JSON**.
- Store feedbacks in a simple **JSON file**.
- Basic form validation and error handling.

---

## Tech Stack
- Python 3
- Flask
- HTML5

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/guimartinson/feedbackAPI.git
   cd feedback_api
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000/
   ```

---

## Project Structure
```
feedback_api/
│
├── app.py           # Flask backend
├── templates/
│   └── form.html    # HTML form for submitting feedback
├── feedbacks.json   # (auto-created) to store feedbacks
```

---

## Available Routes
- `GET /` → Show the feedback form.
- `POST /submit` → Submit feedback from the form.
- `GET /feedbacks` → View all feedbacks in JSON format.

---

## Example Usage
1. User fills the form with name, comment, and rating.
2. Backend receives and stores the feedback.
3. User can view all feedbacks through `/feedbacks`.

---
