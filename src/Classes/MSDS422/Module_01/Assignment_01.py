import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

HOME_PATH = "C:\Projects\Python-Playground\src\Classes\MSDS422"
WORK_PATH = ""
DATA_PATH = "DATA"

MODULE_PATH = "Module_01"
SURVEY_FILE = "mspa-survey-data.csv"

def get_wd():
	path = ""
	if os.path.exists( HOME_PATH ):
		path = HOME_PATH
	else:
		path = WORK_PATH
	return os.path.join( path, MODULE_PATH )

def get_data_file( filename ):
	return os.path.join( get_wd(), DATA_PATH, filename )

survey_data = pd.read_csv(get_data_file(SURVEY_FILE))

