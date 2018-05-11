# coding=utf-8
from flask import Flask, jsonify
import update

app = Flask(__name__)
app.config['DEBUG'] = False


@app.route('/')
def index():
    return 'Матрица Доступа - rSafe Update Server'


@app.route('/api/updates', methods=['GET'])
def get_updates():
    updates = update.check_for_update()
    return jsonify(updates)


if __name__ == '__main__':
    app.run(debug=True)
