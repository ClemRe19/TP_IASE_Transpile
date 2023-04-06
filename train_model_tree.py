def build_model():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    import joblib

    # charge l'ensemble de données iris
    iris = load_iris()

    # construit un arbre de décision
    clf = DecisionTreeClassifier()
    clf.fit(iris.data, iris.target)

    # enregistre l'arbre de décision dans un fichier joblib
    joblib.dump(clf, "tree.joblib")
    
build_model()