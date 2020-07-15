import serial
import time
import threading
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)

def set_speed(action_list):
    ser.write("A")
    for i in action_list:
        ser.write(i)
    time.sleep(0.7)
    print(action_list)

def get_state():
    ser.write("G") # get motor state
    state_data = ser.readline()
    state_list = list(map(int, state_data.split(", ")))
    return state_list