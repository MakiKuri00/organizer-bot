from datetime import datetime as dt
import Tasks as T
import serial
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = T.TaskList()

# ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
# ser.flush()

@app.route('/')
def index():
    current_tasks = tasks.get_all()
    return render_template('index.html', tasks=current_tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    name = request.form.get('task_name')
    date = request.form.get('task_date')
    time = request.form.get('task_time')

    full_deadline = f"{date} {time}:00" 
    tasks.add(name, full_deadline)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks.delete(task_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)