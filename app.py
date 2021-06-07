import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, classification_report, mean_absolute_error, mean_squared_error
from flask import Flask, jsonify, request
from flask_cors import CORS

## __name__ é definido por padrão. Poderiamos usar outra string qualquer aqui, porém,
## não recomendo, pois, isso poderia causar problemas em aplicações maiores.
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

# definimos aqui uma rota, no caso criamos a rota localhost:5000/
@app.route("/")
def primeiro_endpoint_get():
  return ("Tudo Funcionando Corretamente !", 200) 

@app.route("/predict", methods=["POST"])
def segundo_endpoint():

  body = request.get_json()
  # test = request.form['test']

  #print("Body:", body)
  adm = float(body["administrativeAccess"])
  admDur = float(body["administrativeDuration"])
  info = float(body["informationalAccess"])
  infoDur = float(body["informationalDuration"])
  prod = float(body["productRelatedAccess"])
  prodDur = float(body["productRelatedDuration"])
  bounce = float(body["bounceRates"])
  _exits = float(body["exitRates"])
  pageVal = float(body["pageValues"])
  specialDay = float(body["specialDay"])
  # month = body["month"]
  # operatingSystems = body["operatingSystems"]
  # browser = body["browser"]
  # region = body["region"]
  # trafficType = body["trafficType"]
  # visitorType = body["visitorType"]
  # weekend = body["weekend"]

  # print("Param: ", administrativeAccess, administrativeDuration, informationalAccess, informationalDuration,
  #       productRelatedAccess, productRelatedDuration, bounceRates, exitRates,
  #       pageValues, specialDay, month, operatingSystems, browser, region, 
  #       trafficType, visitorType, weekend)

  # print("Exam: 0.0, 0.0, 0.0, 0.0, 2.0, 2.666667, 0.050000, 0.140000, 0.0, 0.0, 2.0, 3.0, 2.0, 2.0, 4.0, 2.0, 0.0")

  model = pickle.load(open('model_rcf', 'rb'))

  new = np.array([adm, admDur, info, infoDur, prod, prodDur, bounce, _exits, pageVal, specialDay, 2.0, 3.0, 2.0, 2.0, 4.0, 2.0, 0.0]).reshape( 1, -1)
  pred = model.predict(new)
  pred_proba = model.predict_proba(new)

  json = '{"revenue": ' + ('True' if pred[0] else 'False') + ', "correct": '

  correct = 0.0
  incorrect = 0.0

  if len(pred_proba) > 0:
    l = len(pred_proba[0])
    if l > 0:
      correct = pred_proba[0][0]*100
      if l > 1:
        incorrect = pred_proba[0][1]*100

  json += str(correct) + ', "incorrect": ' + str(incorrect) + '}'

  # return ({ "message": "Nao gera receita com 99,40% de acuracidade."}, 200) 
  return (json, 200) 

if __name__ == "__main__":
  debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
  app.run(host='0.0.0.0', port=5000, debug=debug)