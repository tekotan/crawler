import serial
import time
import threading
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)

def set_speed(action_list):
    ser.write(str.encode('A'))
    for i in action_list:
        ser.write(str.encode(str(chr(int(i)))))
    time.sleep(0.7)

def get_state():
    ser.write(str.encode('G')) # get motor state
    state_data = ser.readline()
    state_list = list(map(int, state_data.split(", ")))
    if state_list[12] > 1100:
        state_list[12] = 1100
    return state_list

