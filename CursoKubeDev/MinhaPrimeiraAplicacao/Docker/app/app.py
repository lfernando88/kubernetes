from flask import Flask, request, jsonify
import db
import json

app = Flask(__name__)

@app.route('/star', methods=['GET'])
def get_all_peoples():
  star = db.collection
  output = []
  for s in star.find():
    output.append(
        {
            'nome': s['nome'],
            'sobrenome': s['sobrenome'],
            'idade': s['idade'],
            'endereço': s['endereço']
        }
    )
  return jsonify({'result': output})


# @app.route('/star', methods=['GET'])
# def get_star(nome):
#     star = db.collection
#     s = star.find_one({'nome': nome})
#     if s:
#         output = {
#             'nome': s['nome'],
#             'sobrenome': s['sobrenome'],
#             'idade': s['idade'],
#             'endereco': s['endereco']
#         }
#     else:
#         output = "No such name"
#     return jsonify({'result': output})


@app.route('/star', methods=['POST'])
def add_star():
  star = db.collection
  nome = request.json['nome']
  sobrenome = request.json['sobrenome']
  idade = request.json['idade']
  endereco = request.json['endereco']
  star_id = star.insert(
      {
          'nome': nome,
          'sobrenome': sobrenome,
          'idade': idade,
          'endereço': endereco
      }
  )
  new_star = star.find_one({'_id': star_id})
  output = {
      'nome': nome,
      'sobrenome': sobrenome,
      'idade': idade,
      'endereço': endereco
  }
  return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
