import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, classification_report, mean_absolute_error, mean_squared_error

model = pickle.load(open('model_rcf', 'rb'))

print(model)

new = np.array([0.0, 0.0, 0.0, 0.0, 2.0, 2.666667, 0.050000, 0.140000, 0.0, 0.0, 2.0, 3.0, 2.0, 2.0, 4.0, 2.0, 0.0]).reshape( 1, -1)
pred = model.predict(new)
print(pred)

pred_proba = model.predict_proba(new)
print(pred_proba)
