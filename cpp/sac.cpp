#include <math.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <numeric>

#include <tiles2.c>
#include <matrix.h>
#include <helper.h>

using namespace std;

class ActorCriticSoftmaxAgent{
    private:
    double actor_step_size;
    double critic_step_size;
    double avg_reward_step_size;
    double avg_reward;
    Matrix critic_w = Matrix(1, 1, 1);
    Matrix actor_w = Matrix(1, 1, 1);
    vector<double> softmax_prob;
    vector<int> prev_tiles;
    int last_action;
    vector<int> actions;
    
    public:
    void agent_init(map<string, double> agent_info){
        int num_tilings = agent_info["num_tilings"];
        actor_step_size = agent_info["actor_step_size"] / num_tilings;
        critic_step_size = agent_info["critic_step_size"] / num_tilings;
        actions = vector<int>(agent_info["num_actions"], 0);
        avg_reward = 0.0;
        actor_w = Matrix(int(agent_info["num_actions"]), 1000, 0);
        critic_w = Matrix(1000, 1, 0);
    }
    int agent_policy(vector<int> active_tiles){
        softmax_prob = compute_softmax_prob(actor_w, active_tiles);
        int chosen_action = choice(actions, softmax_prob);
        return chosen_action;
    }
    int agent_start(vector<double> state){
        vector<int> active_tiles = tc.get_tiles(state);
        int current_action = agent_policy(active_tiles);
        last_action = current_action;
        prev_tiles = active_tiles;
        return last_action;
    }
    int agent_step(double reward, vector<double> state){
        vector<int> active_tiles = tc.get_tiles(state);
        vector<double> active_critic_w = critic_w.vec_index(1, active_tiles);
        vector<double> prev_critic_w = critic_w.vec_index(1, prev_tiles);
        float delta = reward - avg_reward + accumulate(active_critic_w.begin(), active_critic_w.end(), 0) - accumulate(prev_critic_w.begin(), prev_critic_w.end(), 0);
        avg_reward += avg_reward_step_size * delta;
        
    }
};
