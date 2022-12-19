# ML Midterm Project - Water Potabilty Prediction

# Summary
1. Problem Description
2. EDA
3. Model Training
4. Exporting notebook to script
5. Model deployment
6. Dependency and enviroment management
7. Containerization

## Package Files description
This package contain the following files:
1. notebook.ipynb: The jupiter notebook with the Analysis, EDA, best model determination etc.
2. Pipfile and Pipfile.lock: Pipenv files
3. Dockerfile: Docker configuration file
4. train.py: the notebook exported file in python and transformed in order to generate ai model
5. model.bin: model and DictVectorize
6. predict.py: the service which receive the request of price prediction
7. request: the request of price determination. Invoke the service and sent the POST request.
8. water_potabilty.csv: the dataset from Kaggle
9. README.md: this file with instruction.
10. Screenshots Folder: contain the screenshot included in README.md file


## 1. Problem Description

Access to clean and safe drinking water is a major problem in many developing countries. Many people in these countries do not have access to clean water sources and are forced to use water from lakes, rivers, or other surface water sources, which can be contaminated with bacteria, parasites, and other harmful substances. These contaminants can cause a range of health problems, including diarrhea, cholera, typhoid fever, and other waterborne diseases.

In addition to being contaminated, the water in many developing countries is also often scarce and difficult to access. Many people living in these countries must travel long distances to collect water, and the water they do collect may be polluted or unsafe to drink.

The lack of clean and safe drinking water is a major contributor to poor health and high mortality rates in many developing countries. It is also a significant barrier to economic development, as it can hinder the ability of people to work and contribute to the economy.

Determining water potability from fewer metrics can help reduce costs for detection of drinkable water sources and using different methods to detect and clean hazaredous
water sources.

This dataset for practice:
	https://www.kaggle.com/datasets/adityakadiwal/water-potability

I used this dataset data in order to build a model for water drinkabilty predictions.
Dataset Columns Decription:
1. pH value (numerical variable 1.0-14.0) acidic or basic.
2. Hardnessnumerical variable
3. Solids (Total dissolved solids - TDS) (numerical variable)
4. Chloramines (numerical variable)
5. Sulfate (numerical variable) mg/L
6. Conductivity (numerical variable) μS/cm.
7. Organic_carbon (numerical variable) mg/L
8. Trihalomethanes:(numerical variable) ppm
9. Turbidity (numerical variable) NTU.
10. Potability (boolean 1 or 0)

## 2. EDA
I did the following steps:
1. Check Columns types
2. Check null and duplicated values
3. Check and clean format
4. Convert Potability to boolean
5. Numerical feature correlation (Heatmap)
6. Locate and Trim outliers where needed
7. Feature importance analysis

## 3. Model Training
1. Subdivide the dataset to 60-20-20 (train, val, test) using scikit-learn libraries
2. Prepare target value arrays
3. Remove target value 'Potability' from the datasets
4. Train the following models on train and finally full_train dataset (train + val datasets):
	* Linear Regression
	* Ridge Regression (for some alpha values)
	* SGD Regressor
	* SVR Regressor
	* Random Forest Regressor
	* Decision Tree Regressor
	* Xgboost Tree Regressor (Tuning eta, max_depth and max_child_weight parameters)
5. For each models, I check the best RMSE values:
	* 'Linear Regression RMSE=': 0.4836550843248386,
 	* 'Ridge Regression (alpha 3) RMSE=': 0.48378218440309473,
 	*  'SGDRegressor RMSE=': 1.777009303346633e+17,
 	*  'SVR RMSE=': 0.5540011794330868,
 	*  'RandomForestRegressor RMSE=': 0.45799037427311645,
 	*  'DecisionTreeRegressor RMSE=': 0.6331782009405736,
 	*  'DecisionTreeRegressor GridCV RMSE=': 0.48144680319178135,
 	*  'xgboostRegressor RMSE=': 0.4795955086004447,
 	*  'xgboostDARTRegressor RMSE=': 0.49959644873498155
  
	DecisionTreeRegressor was the model with the best RMSE

## 4. Exporting notebook to script
The Jupiter Notebook was exported in Python.
Prepare the train.py script.
Train.py script read the dataset csv file, train the selected model with full_train dataset and export model and dv in .bin file.

## 5. Model deployment
Once the model.bin is exported and ready to be used, I prepare two scripts and tested it with flask.
The scripts are:
* request.py
* predict.py

#### Request.py

<!-- url = 'http://localhost:9090/predict'

water_id = 'water_potability'
water = {'ph':'5.400301780729467',
    'hardness':'198.76735125945606',
    'solids':'21167.500098968772',
    'chloramines':'10.056852484033495',
    'sulfate':'323.5963490101317',
    'conductivity':'444.47888250689795',
    'organic_carbon':'11.256381166909478',
    'trihalomethanes':'79.84784281372556',
    'turbidity':'4.528522696326911'}

response = requests.post(url, json=water).json()
print('Water potability predicted : %f' % response['water_potability'])
 -->
Data are encapsulated with json and sent to the service (predict.py)

#### Predict.py 
Manage the service (/predict) and use the model to predict the pizza (sent by POST method and encapsulate with json) price.

#### Flask test
1. Run predict.py script

![Flask_Predict_py](Screenshots/flask_predict_py.png)

2. Run request.py script

![Flask_Request_py](Screenshots/flask_request_py.png)

## 6. Dependency and enviroment management
#### Prepare the Virtual Environment with Anaconda3

1. Download the file midprojenv.yml

2. In shell run Command: conda env create –file midprojenv.yml

3. Activate the new environment: conda activate myenv

4. Verify that the new environment was installed correctly:

conda env list


#### Access or execute scripts from the Virtual Env

1. Command to access: pipenv shell

![PipEnv_Access](Screenshots/pipenv_access.png) 

2. Command to execute a command: pipenv cmd

Example launch predict.py from pipenv

pipenv run python predict.py

![PipEnv_Predict_py](Screenshots/pipenv_predict_py.png) 

Example launch request.py from pipenv

pipenv run python request.py

![PipEnv_Predict_Request_py](Screenshots/pipenv_predict_request_py.png) 

## 7. Containerization
Create a Docker container with the following steps:

1. sudo docker pull python:3.8.12-slim -> This command download a Docker container with python version 3.8 slim

2. sudo docker run -it --rm --entrypoint=bash python:3.8.12-slim -> This command allow to access to the docker container vm

3. mkdir app -> create the app directory in the docker vm. This folder will contain the model.bin

4. sudo docker build -t midtermproj . -> This command build the docker vm (called midtermproj) with the docker file

	The dockerfile copy the pipfiles, predict.py script and the model.bin into the app folder, install the necessary package using pipfiles, starts the service with gunicorn on port 9090

![Dockerfile](Screenshots/Dockerfile.png)

5. sudo docker run -it --rm -p 9090:9090 midtermproj -> This command starts the service

6. python request.py -> You can test the services sending a pizza price evaluation

![DockerService](Screenshots/Dockerservice.png)
 

 
