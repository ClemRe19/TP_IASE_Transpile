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
