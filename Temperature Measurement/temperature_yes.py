import board
import busio as io
import adafruit_mlx90614
import time

from time import sleep

def temp():
    print("Place your finger")
    sleep(10)

    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)
    global ambientTemp
    global targetTemp
    ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
    targetTemp = "{:.2f}".format(mlx.object_temperature)

    sleep(10)
    print("Remove your finger")
    #print("Ambient Temperature:", ambientTemp, "°C")
    #print("Target Temperature:", targetTemp,"°C")

def check_consistency(current_value):
    global previous_value  # Declare previous_value as a global variable
    current_value = float(current_value)  # Convert current_value to float
    if abs(current_value - previous_value) < 2:
        previous_value = current_value
        return True
    else:
        previous_value = current_value

    return False

try:
    user_input = input("Enter 'yes' to start measuring temperature: ")
    if user_input.lower() == "yes":
        previous_value = 0
        while True:
            temp()
            if check_consistency(targetTemp):
                print("Ambient Temperature:", ambientTemp, "°C")
                print("Target Temperature:", targetTemp, "°C")
                time.sleep(1)  # Gap to switch between processes
                break  # Causes the while loop to terminate
            else:
                print("Please don't move your finger while measuring your temperature")
                time.sleep(2)
    else:
        print("Invalid input")
        user_input = input("Enter 'yes' to start measuring temperature: ")

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User (Interrupt)")
    GPIO.cleanup()
