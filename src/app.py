from flask import Flask, jsonify, request

app=Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    aux = jsonify(todos)
    return aux

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)  # Elimina el elemento en la posición especificada
        return jsonify(todos)  # Devuelve la lista actualizada
    else:
        return jsonify({"error": "Position out of range"}), 404







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)