#**************************************************************************************
#*                                                                                    *
#*  Title:            Simple Piano using Piezo Buzzer                                 *
#*                                                                                    *
#*  Description:      demonstration of a simple piano made using piezo buzzer on Pi   *
#*                                                                                    *
#*  Author:           Jayant Bhalla, Amity University                                 *
#*                                                                                    *
#*  Date:             28th August, 2017                                               *
#**************************************************************************************

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
note7 = 494

#this is the high scale for the note1
note8 = 525

#array to store all the notes
notes = [note1, note2, note3, note4, note5, note6, note7, note8]

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

def playNotes(array):
    
    #start the PWM 90% duty cycle. highest is 100(makes the pi slower)
    bz.start(90)
    GPIO.output(buzzerPin, True)
    
    for i in range(len(array)):
        bz.ChangeFrequency(array[i])
        sleep(delay)
        
try:
    print('press ctrl + c to quit')
    #plays the notes untill stopped by the user
    while(True):
        playNotes(notes)
        
except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
    
# GPIO.cleanup() cleans the alloted pin numbers on exiting the python script
    