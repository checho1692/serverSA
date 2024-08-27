from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Datos de ejemplo
todos = [
    { "id": 1, "Nombre": "Poncho Suleta", "edad": 80 },
    { "id": 2, "Nombre": "Pablo picapiedra", "edad": 99 }
]

# Endpoints
@app.route('/personas', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    todos.append(new_todo)
    return jsonify(new_todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Tarea no encontrada"}), 404
    todo.update(request.json)
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

