# TP_IASE_Transpile

Transpileurs en C :

Il y a différents types de fichiers dans ce dépôt :
  - .csv : contient des données utilisées pour la régression linéaire
  - .c : contient les codes en C créés par transpilation depuis un code transpileur en python
  - .exe : contient les exécutables post-compilation
  - .py : fichiers python servant à entraîner des modèles pour les train_model_... et servant à faire la transpilation pour les transpile_...
  - .joblib : fichiers joblib de sauvegarde d'entraînement
  
Le fichier 'Main_Transpile_All.py' contient l'ensemble des travaux du TP.

Les modèles supportés par les travaux de ce dépôt sont :
  - regression linéaire
  - regression logistique
  - arbre de décisions
  
Les binaires générés font chacun entre 131 et 133 Ko.


Verilog et transpileur verilog :

Il y a différents types de fichiers dans ce dépôt :
  - .v : fichiers verilog contenant les exercices
  - .vcd : fichiers générés pour les tests verilog
  - .py : transpileur (ne fonctionne pas)
  
