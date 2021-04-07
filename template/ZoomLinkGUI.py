from guizero import App, PushButton
import serial
from time import sleep

signal_sent = False
aud_on = False
vid_on = False
hand_up = False
ser= serial.Serial ("/dev/ttyS0", 9600)
def toggle_audio():
    global signal_sent
    global aud_on
    if aud_on == False:
        aud_on = True
        display_aud_light.bg = "yellow"
    else:
        aud_on = False
        display_aud_light.bg = "white"
    while True:
        if signal_sent == False:
            message = "ALT + A"
            ser.write(str.encode(message))
            signal_sent = True
        else:
            received_data = ser.read()
            sleep(0.03)
            data_left = ser.inWaiting()
            received_data += ser.read(data_left)
            test = str.encode("r")
            print(test)
            print(received_data)
            if test == b'r':
                break

def toggle_video():
    global signal_sent
    global vid_on
    if vid_on == False:
        vid_on = True
        display_vid_light.bg = "yellow"
    else:
        vid_on = False
        display_vid_light.bg = "white"
    while True:
        if signal_sent == False:
            message = "ALT + V"
            ser.write(str.encode(message))
            signal_sent = True
        else:
            received_data = ser.read()
            sleep(0.03)
            data_left = ser.inWaiting()
            received_data += ser.read(data_left)
            test = str.encode("r")
            print(test)
            print(received_data)
            if test == b'r':
                break


def toggle_hand():
    global signal_sent
    global hand_up
    if hand_up == False:
        hand_up = True
        display_hand_light.bg = "yellow"
    else:
        hand_up = False
        display_hand_light.bg = "white"
    while True:
        if signal_sent == False:
            message = "ALT + Y"
            ser.write(str.encode(message))
            signal_sent = True
        else:
            received_data = ser.read()
            sleep(0.03)
            data_left = ser.inWaiting()
            received_data += ser.read(data_left)
            test = str.encode("r")
            print(test)
            print(received_data)
            if test == b'r':
                break

app = App(title="ZoomLink Prototype", layout="grid")
display_aud_light = PushButton(app, text="Audio Off", enabled=False, grid=[0,0])
display_vid_light = PushButton(app, text="Video Off", enabled=False, grid=[1,0])
display_hand_light = PushButton(app, text="Hand Lowered", enabled=False, grid=[2,0])
audio_btn = PushButton(app, command=toggle_audio, text="Audio", grid=[0,1])
video_btn = PushButton(app, command=toggle_video, text="Video", grid=[1,1])
hand_btn = PushButton(app, command=toggle_hand, text="Raise Hand", grid=[2,1])
app.display()

    
