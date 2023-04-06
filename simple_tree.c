
    #include <stdio.h>

    float simple_tree(float*features, int n_features){
        return ((features[0] > 0 || (features[1] > 0)) ? 0 : 1);
    }

    int main() {
        float features[] = {3.0, 12.0};
        int n_features = sizeof(features) / sizeof(float);
        float pred = simple_tree(features, n_features);
        printf("Prediction: %f\n", pred);
        return 0;
    }
    