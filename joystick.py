from machine import Pin, ADC
from time import sleep_ms

Xvr = ADC(Pin(34, Pin.IN))
Yvr = ADC(Pin(35, Pin.IN))
SW = ADC(Pin(32, Pin.IN))
Xvr.atten(ADC.ATTN_11DB)
Yvr.atten(ADC.ATTN_11DB)
SW.atten(ADC.ATTN_11DB)


a = True
while a:
    X_value = Xvr.read()
    SW_value = SW.read()
    if X_value > 3000:
        print('A')
        sleep_ms(500)
        continue
        # a = False
    elif X_value < 1000:
        print('B')
        sleep_ms(500)
        continue
        # a = False
    else:
        continue