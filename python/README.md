## Install Python Package

We provide a scikit-learn wrapper interface. Before you use the Python interface, you must [install](https://fedtree.readthedocs.io/en/latest/Installation.html) FedTree first. 
Then, you can run the following command to install the Python package from source.
```bash
python setup.py install
```

## Class

We provide two classes, ```FLClassifier``` and ```FLRegressor```, where the first is for classification task and the second is for regression task.

### Parameters
Please refer to [here](https://fedtree.readthedocs.io/en/latest/Parameters.html) for the list of parameters.


### Methods

*fit(X, y)*:\
Fit the FedTree model according to the given training data.

*predict(X)*:\
Perform prediction on samples in X.

*save_model(model_path)*:\
Save the FedTree model to model_path.

*load_model(model_path)*:\
Load the FedTree model from model_path.

## Examples
Users can simply input parameters to these classes, call ```fit()```like models in scikit-learn.

```bash
from fedtree import FLClassifier
from dataloader import DataLoader


dataloader = DataLoader()
x,x_test, y, y_test = dataloader.load_datasets(["maskedxgb"], return_dict=False)[0]
clf = FLClassifier(n_trees=1, n_parties=2, mode="vertical", partition_mode="vertical", learning_rate=0.8, max_depth=6, objective="binary:logistic", variance = 0)
clf.fit(x, y)
```

You can find maskedxgb.py on how to use MaskedXGBoost with Python.