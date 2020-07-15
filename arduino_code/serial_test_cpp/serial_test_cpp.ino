#include <Servo.h>
#define MAX_PINS 12

Servo servo[MAX_PINS];

const int echo = A0;
const int trig = A1;

//define servos' ports
const int pin = 2;

double * get_state(){
    int state_arr[13] = {}
    for (int i = 0; i < MAX_PINS; i++)
    {
        state_arr[i] = servo[i].read();
        delay(50);
    }
    digitalWrite(trig, LOW);
    delayMicroseconds(2);
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
    delayMicroseconds(2);

    long duration = pulseIn(echo, HIGH);
    int cm = duration / 29 / 2;
    state_arr[12] = cm;
    return state_arr;
}
void do_action(int [] actions){
    for (int i=0; i<MAX_PINS; i++){
        servo[i].write(actions[i]);
        delay(50);
    }
}

void setup(){
    Serial.begin(9600);
    for (int i = 0; i < MAX_PINS; i++)
    {
        servo[i].attach(pin + i);
        delay(500);
    }
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
}
void loop(){
    if (Serial.available()){
        char message = Serial.read();
        switch (message){
            case 'A':
                int actions[12];
                for (int i=0; i<12; i++){
                    int c = Serial.read();
                    actions[i] = c;
                }
                do_action(actions);
                Serial.print("D")
                break;
            case 'G':
                double * states = get_state();
                for (int i=0; i < 13; i++){
                    Serial.print(*(states + i));
                    Serial.print(", ");
                }
                Serial.print("\n");
                break;
            default:
                break;
        }
    }
}