user_choice = 0
print("Choissisez un transpileur parmi les suivants:\n1 : régression linéaire\n2 : régression logistique\n3 : arbre de décisions")
user_choice = int(input())

if (user_choice == 1):
    import joblib

    # charge un fichier joblib contenant une régression linéaire entraînée
    model = joblib.load("regression.joblib")

    #========================================#
    # récupère les valeurs de coefficients

    coef = model.coef_
    #print(coef)

    #========================================#
    # génère une chaîne de caractère contenant le code C permettant de calculer la prédiction du modèle (float prediction(float *features, int n_feature) )avec les valeur du coefficient

    c_code = """
    #include <stdio.h>

    float prediction(float *features, int n_features) {
        float coef[] = {%s};
        float prediction = 0;
        for (int i = 0; i < n_features; i++) {
            prediction += coef[i] * features[i];
        }
        return prediction;
    }
    """ % (', '.join(str(c) for c in coef))

    #========================================#
    # génère une fonction main qui permet d'appeler prediction sur une donnée définié par un tableau statique de votre choix. 

    c_code += """
    int main() {
        float features[] = {3.0, 12.0, 21.0};
        int n_features = sizeof(features) / sizeof(float);
        float pred = prediction(features, n_features);
        printf("Prediction: %f\\n", pred);
        return 0;
    }
    """

    #========================================#
    # sauvegarde le code c généré dans un fichier.c 

    with open('linear_regression.c', 'w') as f:
        f.write(c_code)

    #========================================#
    # et affiche la commande de compilation à lancer pour le compiler ou le compile directement.

    print ("gcc -o linear_regression linear_regression.c")

    import os
    os.system("gcc -o linear_regression linear_regression.c")

    #========================================#
elif user_choice == 2:
    import joblib

    # charge un fichier joblib contenant une régression logistique entraînée
    model = joblib.load("logistic_regression.joblib")

    #========================================#
    # récupère les valeurs de coefficients

    coef = model.coef_[0]
    #print(coef)

    #========================================#
    # génère une chaîne de caractère contenant le code C permettant de calculer la prédiction du modèle (float prediction(float *features, int n_feature) )avec les valeur du coefficient

    c_code = """
    #include <stdio.h>
    float exp_approx(float x, int n_term){
        
        float result = 1;
        float power_x = 1;
        int factorial_i = 1;
        
        for (int i = 1; i <= n_term; i++){
            power_x *= x;
            factorial_i *= i;
            
            result += power_x / factorial_i;
        }
        
        return result;
    }

    float sigmoid(float x){
        
        float result = 1;
        float exp_sigmoid = exp_approx(-x, 10);
        
        result = 1 / (1 + exp_sigmoid);
        
        return result;
    }

    float prediction(float *features, int n_features) {
        float coef[] = {%s};
        float prediction = 0;
        for (int i = 0; i < n_features; i++) {
            prediction += coef[i] * features[i];
        }
        prediction = sigmoid(prediction);
        return prediction;
    }
    """ % (', '.join(str(c) for c in coef))

    #========================================#
    # génère une fonction main qui permet d'appeler prediction sur une donnée définié par un tableau statique de votre choix. 

    c_code += """
    int main() {
        float features[] = {3.0, 12.0, 21.0};
        int n_features = sizeof(features) / sizeof(float);
        float pred = prediction(features, n_features);
        printf("Prediction: %f\\n", pred);
        return 0;
    }
    """

    #========================================#
    # sauvegarde le code c généré dans un fichier.c 

    with open('logistic_regression.c', 'w') as f:
        f.write(c_code)

    #========================================#
    # et affiche la commande de compilation à lancer pour le compiler ou le compile directement.

    print ("gcc -o logistic_regression logistic_regression.c")

    import os
    os.system("gcc -o logistic_regression logistic_regression.c")

    #========================================#
elif user_choice == 3:
    import joblib

    # charge un fichier joblib contenant un arbre de décisions entraînée
    model = joblib.load("tree.joblib")

    #========================================#
    # récupère les valeurs de coefficients

    #coef = model.coef_
    #print(coef)

    #========================================#
    # génère une chaîne de caractère contenant le code C permettant de calculer la prédiction du modèle (float prediction(float *features, int n_feature) )avec les valeur du coefficient

    c_code = """
    #include <stdio.h>

    float simple_tree(float*features, int n_features){
        return ((features[0] > 0 || (features[1] > 0)) ? 0 : 1);
    }

    int main() {
        float features[] = {3.0, 12.0};
        int n_features = sizeof(features) / sizeof(float);
        float pred = simple_tree(features, n_features);
        printf("Prediction: %f\\n", pred);
        return 0;
    }
    """

    #========================================#

    #========================================#
    # sauvegarde le code c généré dans un fichier.c 

    with open('simple_tree.c', 'w') as f:
        f.write(c_code)

    #========================================#
    # et affiche la commande de compilation à lancer pour le compiler ou le compile directement.

    print ("gcc -o simple_tree simple_tree.c")

    import os
    os.system("gcc -o simple_tree simple_tree.c")

    #========================================#
else:
    print("wrong input for your choice, you can choose an integer in this list [1;2;3] only")
    user_choice = input()

print(user_choice)