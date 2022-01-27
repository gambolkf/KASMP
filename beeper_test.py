from machine import Pin, time_pulse_us, ADC, PWM
from time import sleep_ms
import time

S0 = Pin(33, Pin.OUT)
S1 = Pin(25, Pin.OUT)
S2 = Pin(19, Pin.OUT)
S3 = Pin(18, Pin.OUT)
echo = Pin(4, Pin.IN)
Xvr = ADC(Pin(34, Pin.IN))
Yvr = ADC(Pin(35, Pin.IN))
SW = ADC(Pin(32, Pin.IN))
Xvr.atten(ADC.ATTN_11DB)
Yvr.atten(ADC.ATTN_11DB)
SW.atten(ADC.ATTN_11DB)

S0.off()
S1.on()


def check_red_time():
    S2.off()
    S3.off()
    ex = [time_pulse_us(echo, 0), time_pulse_us(echo, 0)]
    return ex[1]


def check_blue_time():
    S2.off()
    S3.on()
    ex = [time_pulse_us(echo, 0), time_pulse_us(echo, 0)]
    return ex[1]


def check_green_time():
    S2.on()
    S3.on()
    ex = [time_pulse_us(echo, 0), time_pulse_us(echo, 0)]
    return ex[1]


def check_frq():
    red = check_red_time()
    blue = check_blue_time()
    green = check_green_time()
    anwser = [red, blue, green]
    return anwser


def return_color():
    colors_dict = {
        (0): "red",
        (1): "blue",
        (2): "green",
        (0, 1): "pink",
        (0, 2): "yellow",
        (1, 2): "turquoise",
        (1, 0): "pink",
        (2, 0): "yellow",
        (2, 1): "turquoise",
    }
    colors = check_frq()
    print(colors)
    maks_color = max(colors)
    min_color = min(colors)
    for color in colors:
        if not color == min_color and not color == maks_color:
            mid_color = color
    if min_color > 2500:
        return "black"
    elif maks_color - min_color <= 100:
        return "white"
    elif mid_color - min_color <= 150:
        idx1 = colors.index(min_color)
        idx2 = colors.index(mid_color)
        color = colors_dict[(idx1, idx2)]
        return color
    else:
        idx1 = colors.index(min_color)
        color = colors_dict[(idx1)]
        return color


def read_color(color):
    tones = {
        1: 262,
        2: 440,
    }
    colors_dict = {
        "red": (1, 3),
        "blue": (1, 1),
        "green": (1, 2),
        "pink": (1, 4),
        "yellow": (2, 1),
        "turquoise": (2, 2),
        "white": (2, 3),
        "black": (2, 4),
    }
    beeper = PWM(Pin(23, Pin.OUT), freq=440, duty=512)
    i = colors_dict[color][1]
    a = 0
    while a < i:
        beeper.freq(tones[colors_dict[color][0]])
        time.sleep(0.5)
        a += 1
    beeper.deinit()
    print(color)


a = True
while a:
    X_value = Xvr.read()
    SW_value = SW.read()
    if X_value > 3000:
        color = return_color()
        sleep_ms(500)
        continue
    elif X_value < 1000:
        read_color(color)
        sleep_ms(500)
        continue
    else:
        continue
