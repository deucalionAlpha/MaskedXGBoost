from fedtree import FLClassifier
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from dataloader import DataLoader
from sklearn.metrics import roc_auc_score
import numpy as np
from fedtree import FLRegressor
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_svmlight_file

dataloader = DataLoader()

x,x_test, y, y_test = dataloader.load_datasets(["adult"], return_dict=False)[0]
clf = FLRegressor(n_trees=1, n_parties=2, mode="masked", partition_mode="vertical", learning_rate=0.8, max_depth=6, objective="binary:logistic", variance = 0)
clf.fit(x, y)