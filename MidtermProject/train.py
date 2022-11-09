# Dataset of Water Quality
# 
# This dataset for beginners for practice
# 
# https://www.kaggle.com/datasets/adityakadiwal/water-potability
# 
# The ml could be used classify if water is potable.
# 

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
import pickle

# VARIABLES
random_state_value=42
output_file = f'model.bin'


# LOAD THE DATA
path = os.getcwd()
df = pd.read_csv(path+'\data\water_potability.csv')


# CLEAN COLUMNS
df.columns = df.columns.str.lower().str.replace(' ', '_')


# CLEAN DATA


# PREPARE DATASETS (60-20-20)
categorical = df.select_dtypes(include="object").columns.tolist()
numerical = df.select_dtypes(exclude="object").columns.tolist()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=random_state_value)

df_full_train = df_full_train.reset_index(drop=True)

y_full_train = df_full_train.potability.values

del df_full_train['potability']
numerical.pop()

full_train_dicts = df_full_train[categorical + numerical].to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_full_train = dv.fit_transform(full_train_dicts)

features = dv.get_feature_names_out()
dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)


# TRAIN THE MODEL

xgb_params = {
    'eta': 0.3,
    'max_depth': 1,
    'min_child_weight': 1,
    'objective': 'reg:squarederror',
    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dfulltrain, num_boost_round=10)


# SAVE THE MODEL TO FILE

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The Model is saved to {output_file}')



