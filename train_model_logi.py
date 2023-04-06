def build_logi_model():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    import joblib

    # charge l'ensemble de données breast cancer
    cancer = load_breast_cancer()

    # construit une régression logistique
    clf = LogisticRegression()
    clf.fit(cancer.data, cancer.target)

    # enregistre la régression logistique dans un fichier joblib
    joblib.dump(clf, "logistic_regression.joblib")
    
build_logi_model()