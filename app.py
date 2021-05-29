import numpy as np
from flask import Flask, jsonify, request

## __name__ é definido por padrão. Poderiamos usar outra string qualquer aqui, porém,
## não recomendo, pois, isso poderia causar problemas em aplicações maiores.
app = Flask(__name__)

# definimos aqui uma rota, no caso criamos a rota localhost:5000/
@app.route("/")
def primeiro_endpoint_get():
  return ("Tudo Funcionando Corretamente !", 200) 

@app.route("/predict", methods=["POST"])
def segundo_endpoint():

  body = request.get_json()

  print(body)

  return (body, 200)

if __name__ == "__main__":
  debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
  app.run(host='0.0.0.0', port=5000, debug=debug)