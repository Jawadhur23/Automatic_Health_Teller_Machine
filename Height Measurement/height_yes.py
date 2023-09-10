import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    #distance1 = 165-distance
    return distance

#global previous_value
#previous_value = 0

def check_consistency(current_value):
    
    global previous_value  # Declare previous_value as a global variable
    #print(previous_value)
    #print(current_value)
    #if current_value == previous_value:
    if abs(current_value - previous_value) < 2:
        previous_value = current_value
        return True
    else:
        previous_value = current_value

    return False

    
#if __name__ == '__main__':
try:
    user_input = input("enter 'yes' to start measuring height: ")
    if user_input.lower() == "yes":
        previous_value = 0
        while True:               
                dist = distance()                  
                if check_consistency(dist):
                    print ("Measured Distance = %.1f cm" % dist)
                    time.sleep(1) #gap to switch between process
                    break #causing the while loop to terminate
                else:
                    print("Please dont move while measuring your height")
                    time.sleep(2)
                
    else:
        print("Invalid input")
        user_input = input("enter 'yes' to start measuring height: ")
                     
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User(Interrupt)")
    GPIO.cleanup()

