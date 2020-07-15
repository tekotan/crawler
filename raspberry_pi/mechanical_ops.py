import serial
import time
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

def set_speed(action_list):
    template = "A{}"
    ser.write(template.format(str(action_list).strip("[]")))

def get_state():
    ser.write("G") # get motor state
    state_data = ser.readline()
    state_list = list(map(state_data.split(", ")))
    return state_list