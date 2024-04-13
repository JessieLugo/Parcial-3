from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"Kakas", "enable":False},
    {"id":2, "Nombre":"Chancho", "enable":True},
    {"id":3, "nombre":"Juanchulu", "enable":False},
    {"id":4, "nombre":"Dante", "enable":True}
]

@app.route("/task", methods=['GET'])
def get_taska():
        return jsonify(tasks)
if __name__ == '__main__':
        app.run(debug=True)