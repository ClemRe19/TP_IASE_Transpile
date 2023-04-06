
    #include <stdio.h>

    float prediction(float *features, int n_features) {
        float coef[] = {717.2583697096838, 36824.1959742563, 101571.8400215704};
        float prediction = 0;
        for (int i = 0; i < n_features; i++) {
            prediction += coef[i] * features[i];
        }
        return prediction;
    }
    
    int main() {
        float features[] = {3.0, 12.0, 21.0};
        int n_features = sizeof(features) / sizeof(float);
        float pred = prediction(features, n_features);
        printf("Prediction: %f\n", pred);
        return 0;
    }
    