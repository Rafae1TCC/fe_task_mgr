from flask import  (Flask, render_template)
import requests as pyrequests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)
@app.get("/")
def index():
    return render_template("index.html") 

@app.get("/tasks")
def list_tasks():
    response = pyrequests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("task")
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", code=response.status_code, message="Failed to fetch tasks from backend"),
        response.status_code
    )