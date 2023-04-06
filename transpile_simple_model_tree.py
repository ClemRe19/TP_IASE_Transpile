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
