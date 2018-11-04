# Exploring MNIST with Binary Classification (Python SciKit Learn)

# program revised by Thomas W. Milller (2017/10/18)

# Using data from the MNIST dataset from Scikit Learn and
# beginning with code from chapter 3 of Géron, A. 2017. 
# Hands-On Machine Learning with Scikit-Learn & TensorFlow: 
# Concepts, Tools, and Techniques to Build Intelligent Systems. 
# Sebastopol, Calif.: O'Reilly. [ISBN-13 978-1-491-96229-9] 
# Source code available at https://github.com/ageron/handson-ml 
# Relevant code examples in the Python notebook 03_classification.ipynb

# Data from MNIST may be used to evaluate machine learning classifiers.
# Here we will use a subset of the MNIST data to study binary classifiers.
# In particular, after exploring the entire MNIST data set, we will 
# select a subset of the data... just the digits 0 and 6

# Scikit Learn documentation for this assignment:
# http://scikit-learn.org/stable/modules/model_evaluation.html 
# http://scikit-learn.org/stable/modules/generated/
#   sklearn.model_selection.KFold.html

# prepare for Python version 3x features and functions
# comment out for Python 3.x execution
# from __future__ import division, print_function, unicode_literals
# from future_builtins import ascii, filter, hex, map, oct, zip

# to obtain a listing of the results of this program, 
# locate yourself in the working direcotry and
# execute the following command in a terminal or commands window
# python exploring-mnist-v001.py > listing-exploring-mnist-v001.txt

# Scikit Learn documentation for this assignment:
# http://scikit-learn.org/stable/auto_examples/classification/
#   plot_classifier_comparison.html
# http://scikit-learn.org/stable/modules/generated/
#   sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.score
# http://scikit-learn.org/stable/modules/generated/
#   sklearn.linear_model.LogisticRegression.html
# http://scikit-learn.org/stable/modules/model_evaluation.html 
# http://scikit-learn.org/stable/modules/generated/
#  sklearn.model_selection.KFold.html

# seed value for random number generators to obtain reproducible results
RANDOM_SEED = 1
RANDOM_SEED_MODEL = 9999

# import base packages into the namespace for this program
import numpy as np
import pandas as pd

# visualization utilities
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages  # plot to pdf files

# user-defined function for displaying observations/handwritten digits
# adapted from Géron (2017) Python notebook code (default 10 images per row)
def plot_digits(instances, images_per_row = 10, **options):
    size = 28
    images_per_row = min(len(instances), images_per_row)
    images = [instance.reshape(size,size) for instance in instances]
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_images = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((size, size * n_empty)))
    for row in range(n_rows):
        rimages = images[row * images_per_row : (row + 1) * images_per_row]
        row_images.append(np.concatenate(rimages, axis=1))
    image = np.concatenate(row_images, axis=0)
    plt.imshow(image, cmap = matplotlib.cm.binary, **options)
    plt.axis('off')

# --------------------------------------------------------
# cross-validation scoring code adapted from Scikit Learn documentation
from sklearn.metrics import roc_auc_score

# specify the set of classifiers being evaluated
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

names = ["Naive_Bayes", "Logistic_Regression", 
         "Linear_SVM_C=0.1"]
classifiers = [BernoulliNB(alpha=1.0, binarize=0.5, 
                           class_prior = [0.5, 0.5], fit_prior=False), 
               LogisticRegression(),
               Pipeline((
                       ("scaler", StandardScaler()),
                       ("svc", SVC(kernel = 'linear', 
                                          probability = True, C = 0.1,
                                          random_state = RANDOM_SEED_MODEL)),
                       ))]

# --------------------------------------------------------
# import data from Scikit Learn and explore the data
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
mnist  # show structure of datasets Bunch object from Scikit Learn

# define arrays from the complete data set
mnist_X, mnist_y = mnist['data'], mnist['target']

# show stucture of numpy arrays
# 70,000 observations, 784 explanatory variables/features
# features come from 28x28 pixel displays
# response is a single digit 0 through 9
print('\n Structure of explanatory variable array:', mnist_X.shape)
print('\n Structure of response array:', mnist_y.shape)

# note the sequential organization of the MNIST data with index plot
# route plot to external pdf file

with PdfPages('plot-mnist-index-plot.pdf') as pdf:
    fig, axis = plt.subplots()
    axis.set_xlabel('Sequence/Index number within MNIST Data Set')
    axis.set_ylabel('MNIST Digit')
    plt.title('Index Plot of MNIST Data Set')
    plt.plot(mnist_y[:,])
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

# summarize the sequential structure of the MNIST data
# target/label and index values for the observations
# the first 60 thousand observations are often used as training data        
# they cover the ten digits... aranged in order... that is, zeros come
# before ones, ones before twos, and so on
# but the observed digit frequencies are unequal    
# examine the frequency distributions for the digits using pandas DataFrame
# the first 60 thousand observations are often used as training data    
mnist_y_0_59999_df = pd.DataFrame({'label': mnist_y[0:59999,]}) 
print('\nFrequency distribution for 60,000 observations (for model building)')
print(mnist_y_0_59999_df['label'].value_counts(ascending = True))   

# the last 10000 observations cover the ten digits
# these are often used as test data
# digits are arranged in order but the frequencies are unequal     
mnist_y_60000_69999_df = pd.DataFrame({'label': mnist_y[60000:69999,]}) 
print('\nFrequency distribution for last 10,000 observations (holdout sample)')
print(mnist_y_60000_69999_df['label'].value_counts(ascending = True))   

# in selecting handwritten digits to represent,
# we will randomly sample from digit representations
from sklearn.utils import resample

# display example data from the 28x28 pixel displays 
# ten-page pdf file, 100 digit realizations on each page
# using examples from the full MNIST data set
# 
# we customize the location within the subplot for each page using GridSpec
# see matplotlib documentation: http://matplotlib.org/users/gridspec.html  
# begin by showing samples from the model building data (first 60000 observations)  
with PdfPages('plot-mnist-handwritten-digits-model-building-data.pdf') as pdf:
    for idigit in range(0,10):
        # print('\nworking on digit', idigit)
        
        # identify the index values from the first 60000 observations
        # that have the label equal to a specific digit (idigit)
        idigit_indices = \
            mnist_y_0_59999_df.index[mnist_y_0_59999_df.label == idigit]
        # obtain indices for 100 randomly sampled observations for this digit    
        show_indices = resample(idigit_indices, n_samples=100, 
                                replace = False, 
                                random_state = RANDOM_SEED).sort_values()       
        plt.figure(0)
        plt.suptitle('Examples of MNIST Data for Digit ' + str(idigit))
        # define beginning and ending row index for this digit
        # generate ten rows of ten digits each
        for j in range(0,10):
            row_begin_index = j * 10
            row_end_index = row_begin_index + 10
            # print('row begin',row_begin_index, 'row_end', row_end_index)
            this_row_indices = show_indices[row_begin_index:row_end_index]
            
            example_images = np.r_[mnist_X[this_row_indices]]
            # print(mnist_y[this_row_indices,])
            plt.subplot2grid((10,1), (j,0), colspan=1)
            # plot ten digits per row using user-defined function
            plot_digits(example_images, images_per_row=10)
            row_begin_index = row_end_index + 1
        pdf.savefig()  
        plt.close()   

# also show samples from the holdout data (last 10000 observations)  
with PdfPages('plot-mnist-handwritten-digits-holdout-data.pdf') as pdf:
    for idigit in range(0,10):
        # print('\nworking on digit', idigit)
        
        # identify the index values from the first 60000 observations
        # that have the label equal to a specific digit (idigit)
        idigit_indices = 60000 + \
        mnist_y_60000_69999_df.index[mnist_y_60000_69999_df.label == idigit]
        # obtain indices for 100 randomly sampled observations for this digit    
        show_indices = resample(idigit_indices, n_samples=100, 
                                replace = False, 
                                random_state = RANDOM_SEED).sort_values()       
        plt.figure(0)
        plt.suptitle('Examples of MNIST Data for Digit ' + str(idigit))
        # define beginning and ending row index for this digit
        # generate ten rows of ten digits each
        for j in range(0,10):
            row_begin_index = j * 10
            row_end_index = row_begin_index + 10
            # print('row begin',row_begin_index, 'row_end', row_end_index)
            this_row_indices = show_indices[row_begin_index:row_end_index]
            
            example_images = np.r_[mnist_X[this_row_indices]]
            # print(mnist_y[this_row_indices,])
            plt.subplot2grid((10,1), (j,0), colspan=1)
            # plot ten digits per row using user-defined function
            plot_digits(example_images, images_per_row=10)
            row_begin_index = row_end_index + 1
        pdf.savefig()  
        plt.close()    
        
# ------------------------------------------------------------------------
# select a subset of the model building data... observations for digits 0 and 1 
# these will comprise the data we use in model development/building
# and to select "best" modeling methods within a cross-validation design        
model_indices_for_zeros = \
            mnist_y_0_59999_df.index[mnist_y_0_59999_df.label == 0]
model_indices_for_ones = \
            mnist_y_0_59999_df.index[mnist_y_0_59999_df.label == 1]
model_indices = np.append(model_indices_for_zeros, 
                          model_indices_for_ones)

model_y = np.r_[mnist_y[model_indices]]
model_X = np.r_[mnist_X[model_indices]]
model_data = np.concatenate((model_y.reshape(-1, 1), model_X), axis = 1)

# check on shape of the model_data array
print('\nShape of model_data:', model_data.shape)

# set up model_data for modeling work consisting of selected X and y rows
# let's put the y values in the first column and X values in remainng columns


# we are setting aside the zeros and ones from the last 10000 observations
# these will compose a hold-out sample for final testing of the selected model
# select a subset of the hold-out test data... observations for digits 0 and 1       
holdout_indices_for_zeros = 60000 + \
            mnist_y_60000_69999_df.index[mnist_y_60000_69999_df.label == 0]
holdout_indices_for_ones = 60000 + \
            mnist_y_60000_69999_df.index[mnist_y_60000_69999_df.label == 1]
holdout_indices = np.append(holdout_indices_for_zeros, 
                            holdout_indices_for_ones)

holdout_y = np.r_[mnist_y[holdout_indices]]
holdout_X = np.r_[mnist_X[holdout_indices]]
holdout_data = np.concatenate((holdout_y.reshape(-1, 1), 
                               holdout_X), axis = 1)

# check on shape of the holdout_data array
print('\nShape of holdout_data:', holdout_data.shape)

# shuffle the rows because MNIST data rows have a sequence
# with lower digits coming before higher digits
# shuffle is by the first index, which is the rows
np.random.seed(RANDOM_SEED)
np.random.shuffle(model_data)

np.random.seed(RANDOM_SEED)
np.random.shuffle(holdout_data)

# --------------------------------------------------------
# specify the k-fold cross-validation design
from sklearn.model_selection import KFold

# ten-fold cross-validation employed here
# As an alternative to 10-fold cross-validation, restdata with its 
# small sample size could be analyzed would be a good candidate
# for  leave-one-out cross-validation, which would set the number
# of folds to the number of observations in the data set.
N_FOLDS = 10
print('\nProgress with' + str(N_FOLDS) + '-fold cross-validation')

# set up numpy array for storing results
cv_results = np.zeros((N_FOLDS, len(names)))

kf = KFold(n_splits = N_FOLDS, shuffle=False, random_state = RANDOM_SEED)
# check the splitting process by looking at fold observation counts
index_for_fold = 0  # fold count initialized 
for train_index, test_index in kf.split(model_data):
    print('\nFold index:', index_for_fold,
          '------------------------------------------')
#   the structure of modeling data for this study has the
#   response variable coming first and explanatory variables later          
#   so 1:model_data.shape[1] slices for explanatory variables
#   and 0 is the index for the response variable    
    X_train = model_data[train_index, 1:model_data.shape[1]]
    X_test = model_data[test_index, 1:model_data.shape[1]]
    y_train = model_data[train_index, 0]
    y_test = model_data[test_index, 0]   
    print('\nShape of input data for this fold:',
          '\nData Set: (Observations, Variables)')
    print('X_train:', X_train.shape)
    print('X_test:',X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:',y_test.shape)

    index_for_method = 0  # initialize
    for name, clf in zip(names, classifiers):
        print('\nClassifier evaluation for:', name)
        print('  Scikit Learn method:', clf)
        clf.fit(X_train, y_train)  # fit on the train set for this fold
        # evaluate on the test set for this fold
        y_test_predict = clf.predict_proba(X_test)
        fold_method_result = roc_auc_score(y_test, y_test_predict[:,1]) 
        print('Area under ROC curve:', fold_method_result)
        cv_results[index_for_fold, index_for_method] = fold_method_result
        index_for_method += 1
  
    index_for_fold += 1

cv_results_df = pd.DataFrame(cv_results)
cv_results_df.columns = names

print('\n----------------------------------------------')
print('Average results from ', N_FOLDS, '-fold cross-validation\n',
      '\nMethod                 Area under ROC Curve', sep = '')     
print(cv_results_df.mean())   

# --------------------------------------------------------
# let's select logistic regression and 
# see how well it does on the holdout sample

print('\n----------------------------------------------')
# fit logistic regression to full model building data set
clf = LogisticRegression()
X_train = model_data[:, 1:model_data.shape[1]]
y_train = model_data[:, 0]
clf.fit(X_train, y_train)
print('\nSelected modeling method is', clf)

# predict holdout cases probability values and compute ROC on holdout
y_holdout_predict = clf.predict_proba(holdout_X)
print('\nArea under ROC for holdout observations:',
      roc_auc_score(holdout_y, y_holdout_predict[:,1])) 


 