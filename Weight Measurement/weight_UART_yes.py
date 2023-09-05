import time
import serial
import serial.tools.list_ports

# List available serial ports (uncomment the following lines if needed)
ports = serial.tools.list_ports.comports()
# for port in ports:
#     print(port.device, port.description)

# Replace '/dev/ttyUSB0' with the correct port name
port_name = '/dev/ttyUSB0'

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

try:
    user_input = input("enter 'yes' to start measuring height: ")
    if user_input.lower() == "yes":
        previous_value = 0
        # Configure the serial port
        ser = serial.Serial(port_name, 115200) # Use the appropriate baud rate

        while True:
            if ser.in_waiting > 0:
                received_data = ser.readline().decode().strip() # Read the received data
                myFloat = float(received_data) # Convert the received data to an integer
                print(myFloat)
                while True:
                    if check_consistency(myFloat):
                        # Process the received integer value
                        print("Received integer value:", myFloat)
                        time.sleep(1) #gap to switch between process
                        break #causing the while loop to terminate
                    else:
                        print("Please dont move while measuring your weight")
                        time.sleep(2)
                break
    else:
        print("Invalid input")
        user_input = input("enter 'yes' to start measuring weight: ")

except serial.SerialException as e:
    print(f"Error opening {port_name}: {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")

