
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
    float coef[] = {0.900778495882178, 0.44032924242521543, 0.31941144675759303, -0.019955588837847617, -0.032862524219693254, -0.15603384043503676, -0.2185955343074074, -0.0919574931128661, -0.04556012006558774, -0.009044252157331433, 0.03869887328400564, 0.35104689963726626, 0.1252708185965012, -0.10455900867926196, -0.002986535433509543, -0.033686315814397995, -0.04686533231381692, -0.0120027202331192, -0.011014343675245604, -0.003117556914260859, 0.9566109540677902, -0.4723702715396471, -0.274739799367571, -0.010910679316239506, -0.05977457945038488, -0.48762551879811133, -0.6068887975151076, -0.17719008159338626, -0.14496874887415165, -0.046680645945192625};
    float prediction = 0;
    for (int i = 0; i < n_features; i++) {
        prediction += coef[i] * features[i];
    }
    prediction = sigmoid(prediction);
    return prediction;
}

int main() {
    float features[] = {3.0, 12.0, 21.0};
    int n_features = sizeof(features) / sizeof(float);
    float pred = prediction(features, n_features);
    printf("Prediction: %f\n", pred);
    return 0;
}
