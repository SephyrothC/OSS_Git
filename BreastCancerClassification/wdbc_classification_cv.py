import numpy as np
from sklearn import datasets, ensemble
from sklearn.model_selection import RandomizedSearchCV

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Define the parameter space
    param_space = {
        'n_estimators': [10, 50, 100, 200],
        'criterion': ['gini', 'entropy'],
        'max_depth': [None] + list(np.arange(1, 20)),
        'min_samples_split': [2, 5, 10, 20],
        'min_samples_leaf': [1, 2, 5, 10],
        'max_features': [None, 'sqrt', 'log2']
    }

    # Train a model
    model = ensemble.ExtraTreesClassifier()
    model_cv = RandomizedSearchCV(
        model, param_space, cv=5, n_iter=50, n_jobs=-1, return_train_score=True)
    model_cv.fit(wdbc.data, wdbc.target)

    # Print the best parameters
    print(f'* Best parameters: {model_cv.best_params_}')
    print(f'* Best training accuracy: {model_cv.best_score_:.3f}')

    # Evaluate the model on the test set
    acc_test = model_cv.score(wdbc.data, wdbc.target)
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')
