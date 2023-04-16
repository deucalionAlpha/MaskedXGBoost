from fedtree import FLClassifier
from dataloader import DataLoader


dataloader = DataLoader()
x,x_test, y, y_test = dataloader.load_datasets(["maskedxgb"], return_dict=False)[0]
clf = FLClassifier(n_trees=1, n_parties=2, mode="vertical", partition_mode="vertical", learning_rate=0.8, max_depth=6, objective="binary:logistic", variance = 0)
clf.fit(x, y)