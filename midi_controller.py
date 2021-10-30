from machine import Pin, UART
import time
import ustruct

led = Pin(25, Pin.OUT)
button0 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(10, Pin.IN, Pin.PULL_DOWN)
button5 = Pin(8, Pin.IN, Pin.PULL_DOWN)
switch = Pin(14, Pin.IN, Pin.PULL_DOWN)
uart = UART(1, 31250)

def sendCC(cc_value):
    # 0xB0 is CC message
    print(cc_value)
    uart.write(ustruct.pack("bbb", 0xB0, cc_value, 127))
    uart.write(ustruct.pack("bbb", 0xB0, cc_value, 0))

def buttonPressed(button_number):
    led.value(1)
    sendCC(button_number + 20)
    time.sleep(0.5)
    led.value(0)

while True:
    offset = switch.value() * 6
    if button0.value():
        buttonPressed(0 + offset)
    if button1.value():
        buttonPressed(1 + offset)
    if button2.value():
        buttonPressed(2 + offset)
    if button3.value():
        buttonPressed(3 + offset)
    if button4.value():
        buttonPressed(4 + offset)
    if button5.value():
        buttonPressed(5 + offset)