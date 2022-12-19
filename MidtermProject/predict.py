import pickle
from flask import Flask
from flask import request
from flask import request
from flask import jsonify
from sklearn.tree import DecisionTreeRegressor

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
	dv, model = pickle.load(f_in)

app = Flask('water_potability')

@app.route('/predict', methods=['POST'])
def predict():
	water = request.get_json()
	
	X = dv.transform([water])

	y_pred = model.predict(X)
	water_potability = y_pred
	
	result = {
		'water_potability': float(water_potability),
	}
	
	return jsonify(result)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)

