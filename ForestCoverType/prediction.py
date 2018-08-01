import os
import pandas as pd
import numpy as np
import scipy as sc

PATH = 'C:\MachineLearning\Internship\Forest Cover Type Prediction'
os.chdir(PATH)
del PATH
os.getcwd()

population_train = pd.read_csv("mytrain.csv", 
                    na_values=['NA','?',''], 
                    sep=',', 
                    header=0)
population_test = pd.read_csv("mytest.csv", 
                    na_values=['NA','?',''], 
                    sep=',', 
                    header=0)

population_train.head()
population_train.dtypes
population_train.shape
population_train.columns
population_test.columns
population_train.describe(include='all')
population_train.isnull().sum()
#train.fillna()

# 'del col_Length' for removing 'col_length' from python

# adding a new variable type= trrain test to determine train and test
population_test['Cover_Type'] = 1
population_train['type'] = "train"
population_test['type'] = 'test'

# combining both train and test (row bind)
combine = population_train.append(population_test,sort=False)
del population_train,population_test
combine.head()
combine.tail()

#To delete the column without having to reassign df you can do:
combine.drop('Id', axis=1, inplace=True)

#factorising Variables
combine['Wilderness_Area'] = combine['Wilderness_Area'].astype('category')
combine['Cover_Type'] = combine['Cover_Type'].astype('category')
combine['Soil_Type'] = combine['Soil_Type'].astype('category')
combine['type'] = combine['type'].astype('category')
combine.dtypes

#renaming columns
combine.columns
nameslist =['Elevation', 'Aspect', 'Slope', 'HD_Hydro', 'VD_Hydro','HD_Road', 'Hillshade_9am', 'Hillshade_Noon',
            'Hillshade_3pm','HD_Fire_Points', 'Wilderness_Area', 'Soil_Type', 'Cover_Type', 'type']
combine.set_axis(nameslist, axis=1, inplace=True)
del nameslist

# Normalising the data
df_num = combine.select_dtypes(include=[np.number])
df_norm = (df_num - df_num.min()) / (df_num.max() - df_num.min())
combine[df_norm.columns] = df_norm
del df_num,df_norm

#Sepereting Population train / test 
population_train = combine[combine['type'] == 'train']
population_test = combine[combine['type'] == 'test']
population_train.drop('type', axis=1, inplace=True)
population_test.drop(['type','Cover_Type'], axis=1, inplace=True)
del combine

# Splitting data into train and test
y=population_train.iloc[:,12]
X = population_train.iloc[:,0:11]
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


