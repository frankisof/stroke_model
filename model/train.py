from os import PathLike
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib
from sklearn.impute import SimpleImputer

# Crear un imputador
imputer = SimpleImputer(strategy="mean")  # Puedes usar "mean" u otra estrategia

# Aplicar la imputación a tus datos

df = pd.read_csv(pathlib.Path('data/full_data.csv'))
y = df.pop('stroke')
X = df
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)
X_train = imputer.fit_transform(X_train)
print ('Training model.. ')
clf = RandomForestClassifier(n_estimators = 10,
                            max_depth=2,
                            random_state=0)
clf.fit(X_train, y_train)
print ('Saving model..')
dump(clf, pathlib.Path('strokev1.joblib'))

