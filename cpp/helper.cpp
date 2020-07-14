#include "helper.h"
using namespace std;

int choice(const vector<int> samples, vector<double> probabilities){
    const int outputSize = 1;

    vector<double> vec(outputSize);

    const vector<int> samples{1, 2, 3, 4, 5, 6, 7};
    const vector<double> probabilities{0.1, 0.2, 0.1, 0.5, 0, 1};

    default_random_engine generator;
    discrete_distribution<int> distribution(probabilities.begin(), probabilities.end());

    vector<int> indices(vec.size());
    generate(indices.begin(), indices.end(), [&generator, &distribution]() { return distribution(generator); });

    transform(indices.begin(), indices.end(), vec.begin(), [&samples](int index) { return samples[index]; });
    return indices[0];
}