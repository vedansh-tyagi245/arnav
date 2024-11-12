from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list of tasks (in memory)
tasks = []

# Home route
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        # Each task is now a dictionary with 'content' and 'completed' fields
        tasks.append({"content": task_content, "completed": False})
    return redirect(url_for('index'))

# Route to remove a task
@app.route('/remove/<int:task_index>')
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

# Route to toggle task completion
@app.route('/toggle_complete/<int:task_index>')
def toggle_complete(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = not tasks[task_index]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
