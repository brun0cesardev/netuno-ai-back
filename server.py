from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from bardapi import Bard

app = Flask(__name__)
CORS(app)

os.environ['_BARD_API_KEY']="Ywh5Q_RMQHgda1IBxzTty6SdrIcLBED1LVleDraDhhfIigsw_BF6qTVbp_p1H5tccD5AJw."


@app.route('/api/getanswer', methods=['POST'])
def get_answers():
    data = request.json
    pergunta = data.get('question')
    resposta = Bard().get_answer(pergunta)['content']
    return jsonify(resposta)

@app.route('/api/newconversation', methods=['POST'])
def get_user():
    return jsonify({"message": "CAIU NA SEGUNDA ROTA"})

@app.route('/api/users', methods=['POST'])
def add_user():
    return jsonify({"message": "CAIU NO TERCEIRO ROTA"})

if __name__ == '__main__':
    app.run(debug=True)
