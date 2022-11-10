import pickle
from flask import Flask
from flask import request
from flask import request
from flask import jsonify
from sklearn.ensemble import RandomForestRegressor

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
	dv, model = pickle.load(f_in)

app = Flask('water_potability')

@app.route('/predict', methods=['POST'])
def predict():
	water = request.get_json()
	
	X = dv.transform([water])

	features = dv.get_feature_names_out()
	DMatrixPred = RandomForestRegressor.predict(X, feature_names=features)

	y_pred = model.predict(DMatrixPred)
	water_potability = y_pred
	
	result = {
		'water_potability': float(water_potability),
	}
	
	return jsonify(result)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9090)

