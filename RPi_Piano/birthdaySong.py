#***************************************************************************************
#*                                                                                     *
#*  Title:            Birthday Song using Piezo Buzzer                                 *
#*                                                                                     *
#*  Description:      demonstration of birthday song played using piezo buzzer on Pi   *
#*                                                                                     *
#*  Author:           Jayant Bhalla, Amity University                                  *
#*                                                                                     *
#*  Date:             28th August, 2017                                                *
#***************************************************************************************

#header file to control Pi's GPIO pins
import RPi.GPIO as GPIO
from time import sleep

#the frequency of the main 7 notes of piano stored into variables
note1 = 262
note2 = 294
note3 = 330
note4 = 349
note5 = 392
note6 = 440
note7 = 466

#this is the high scale for the note1
note8 = 524

#assigning a variable to the pin number
buzzerPin = 15

#sets the mode to access pins by pin numbers on the pi
GPIO.setmode(GPIO.BOARD)

#sets the buzzer pin to give output
GPIO.setup(buzzerPin, GPIO.OUT)

#assigning instance of PWM to a variable
bz = GPIO.PWM(buzzerPin, 100)

#time interval between 2 consecutive notes
delay = 0.5

def birthdaySong():
    
    #start the PWM 90% duty cycle. highest is 100(makes the pi slower and buzzer gives a screaching sound)
    bz.start(90)
    GPIO.output(buzzerPin, True)
    
    bz.ChangeFrequency(note1)
    sleep(delay / 2)
    bz.ChangeFrequency(note1)
    sleep(delay)
    bz.ChangeFrequency(note2)
    sleep(delay)
    bz.ChangeFrequency(note1)
    sleep(delay + 0.25)
    bz.ChangeFrequency(note4)
    sleep(delay)
    bz.ChangeFrequency(note3)
    sleep(delay + 0.25)
    
    bz.ChangeFrequency(note1)
    sleep(delay / 2)
    bz.ChangeFrequency(note1)
    sleep(delay)
    bz.ChangeFrequency(note2)
    sleep(delay)
    bz.ChangeFrequency(note1)
    sleep(delay + 0.25)
    bz.ChangeFrequency(note5)
    sleep(delay)
    bz.ChangeFrequency(note4)
    sleep(delay + 0.25)
    
    bz.ChangeFrequency(note1)
    sleep(delay / 2)
    bz.ChangeFrequency(note1)
    sleep(delay)
    bz.ChangeFrequency(note8)
    sleep(delay)
    bz.ChangeFrequency(note6)
    sleep(delay)
    bz.ChangeFrequency(note5)
    sleep(delay)
    bz.ChangeFrequency(note4)
    sleep(delay / 2)
    bz.ChangeFrequency(note3)
    sleep(delay / 2)
    bz.ChangeFrequency(note2)
    sleep(delay + 0.25)
    
    bz.ChangeFrequency(note7)
    sleep(delay / 2)
    bz.ChangeFrequency(note7)
    sleep(delay / 2)
    bz.ChangeFrequency(note6)
    sleep(delay)
    bz.ChangeFrequency(note4)
    sleep(delay)
    bz.ChangeFrequency(note5)
    sleep(delay)
    bz.ChangeFrequency(note4)
    sleep(delay * 2)
    
    
    
    
try:
    print('press ctrl + c to quit')
    #plays the birthday song untill interrupted by the user
    while(True):
        birthdaySong()
        
except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
    
# GPIO.cleanup() cleans the alloted pin numbers on exiting the python script
    