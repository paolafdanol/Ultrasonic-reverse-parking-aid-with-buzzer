#----------------------------------------------------------
# ULTRASONIC REVERSE CAR PARKING AID
# ==================================
#
# In this project a HC-SR04 type ultrasonic sensor module is
# connected to the Raspberry Pi Pico. Additionally, a buzzer
# is connected. The project sounds the buzzer as the car gets
# near an obstacle.The buzzer sounds faster as the car gets
# nearer an object
#------------------------------------------------------------
import utime
import LCD
from machine import Pin

    LCD.lcd_init()
    LCD.lcd_cursor_on()
    LCD.lcd_cursor

trig = Pin(16, Pin.OUT) # trig pin
echo = Pin(17, Pin.IN) # echo pin

Buzzer = Pin(18, Pin.OUT) # Buzzer at pin 18
Buzzer.value(0) # Turn OFF buzzer

while True:
    trig.value(0)
    utime.sleep_us(5) # Wait until settled
    
    trig.value(1) # Send trig pulse
    utime.sleep_us(10) # 10 microseconds
    trig.value(0) # Remove trig pulse
    
    while echo.value() == 0: # Wait for echo 1
        pass
    Tmrstrt = utime.ticks_us()
    
    while echo.value() == 1: # Wait for echo 0
        pass
    Tmrend = utime.ticks_us()
    
    Duration = utime.ticks_diff(Tmrend, Tmrstrt)
    distance = Duration * 0.0171
    
    LCD.lcd_clear()
    LCD.lcd_puts("Distancia:", 1)  # Primera línea
#
# Now sound the buzzer accordingly.The sounding should be faster
# as the car gets neareer the object.This is done by changing the
# delay in the duration of the sound
#
    if distance > 100:
        dely = 0
    elif distance > 70 and distance < 90:
        dely = 600
    elif distance > 50 and distance < 70:
        dely = 400
    elif distance > 30 and distance < 50:
        dely = 300
    elif distance > 10 and distance < 30:
        dely = 200
    elif distance < 10:
        dely = 10
        
    if distance < 100:
        Buzzer.value(1)
        utime.sleep_ms(dely)
        Buzzer.value(0)
        utime.sleep_ms(dely)

    