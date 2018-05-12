# coding=utf-8
from flask import Flask, jsonify

import os
import update

base_dir = os.getcwd()
app = Flask(__name__)
app.config['DEBUG'] = False

update_dir = base_dir + '/updates'


@app.route('/')
def index():
    return 'Матрица Доступа - rSafe Update Server'


@app.route('/api/updates', methods=['GET'])
def get_updates():
    updates = update.check_for_update(update_dir)
    return jsonify(updates)


if __name__ == '__main__':
    app.run(debug=False)
