# Naive Bayes Training Example (Python) 
# using data from the interactive training module

# program revised by Thomas W. Milller (2017/09/25)

# prepare for Python version 3x features and functions
# comment out for Python 3.x execution
# from __future__ import division, print_function
# from future_builtins import ascii, filter, hex, map, oct, zip

# import packages into the namespace for this program
import os
import numpy as np
import pandas as pd

# BernoulliNB is designed for binary/boolean features
from sklearn.naive_bayes import BernoulliNB

path_home = "C:\\Projects\\"
path_work = "E:\\GitHub\\"

def get_data_path():
	path_root = ( os.path.exists( path_home ) and path_home ) or path_work
	project_path = os.path.join( path_root, "Python-Playground\src\Classes\MSDS422\Module_02" )
	return os.path.join( project_path, "data")

input_data = pd.read_csv(os.path.join(get_data_path(), "naive-bayes-training-example.csv"))
input_data.set_index('Patient', drop = True, inplace = True)

X = input_data.loc['Alice':'Paul','A':'C']  # training explanatory variables
Y = input_data.loc['Alice':'Paul','Disease'] # training response variable

# priors can be adjusted to conform to the prevalence of the disease
# using an argument such as these: 
# class_prior = [0.5, 0.5] # half the population has the disease (default)
# class_prior = [0.9, 0.1] # 10 percent of the population has the disease
clf = BernoulliNB()
clf.fit(X, Y)

# set up array for storing training set predictions
results = input_data.loc['Alice':'Paul',:]
# add predicted probabilities to the training sample
results['Prob_NO'] = clf.predict_proba(X)[:,0]
results['Prob_YES'] = clf.predict_proba(X)[:,1]
results['Prediction'] = clf.predict(X)
print('\nTraining set predictions from Naive Bayes model\n',results)
print('\n\nOverall training set accuracy:', clf.score(X, Y))

print('\nDisease prediction for Walter:',
    clf.predict(input_data.loc['Walter','A':'C'].values.reshape(1,-1)))

# Naive Bayes in sklearn does not support predictions with missing values
# So set up a new model for Susan's data with only A and C symptoms present
X = input_data.loc['Alice':'Paul',['A','C']]
Y = input_data.loc['Alice':'Paul','Disease']
clf.fit(X, Y)
print('\nDisease prediction for Susan:',
    clf.predict(input_data.loc['Susan',['A','C']].values.reshape(1,-1)))