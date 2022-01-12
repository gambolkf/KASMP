from machine import Pin, ADC
from time import sleep_ms


# Xvr = pin 34; Yvr = pin 35; SW = pin 32


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
        a = False
    elif X_value < 1000:
        print('B')
        sleep_ms(500)
        a = False
    
    # cos nie chce dzialac ten switch
    # ale dziala reszta ladnie

    # elif SW_value == 0
    #     print('switch')
    #     sleep_ms(500)
    #     a = False
    
    
