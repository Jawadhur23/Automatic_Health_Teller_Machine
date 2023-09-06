#include "HX711.h"

#define calibration_factor -7050.0 // This value is obtained using the SparkFun_HX711_Calibration sketch

const int DOUT = D5; // Replace D5 with the actual DOUT pin number connected to HX711
const int CLK = D6;  // Replace D6 with the actual CLK pin number connected to HX711

HX711 scale; // Declare the HX711 object

void setup() {
  Serial.begin(115200); // Start serial communication for debugging
  scale.begin(DOUT, CLK); // Initialize the HX711 scale with the specified pins
  scale.set_scale(calibration_factor); // This value is obtained using the SparkFun_HX711_Calibration sketch
  scale.tare(); // Assuming there is no weight on the scale at start up, reset the scale to 0

  Serial.println("Readings:");
}

void loop() {
  //Serial.print("Measured Weight: ");
  Serial.println(scale.get_units() / 3.8, 2); // scale.get_units() returns a float, divide it by 2.5
  //Serial.print("Kg"); // You can change this to kg but you'll need to refactor the calibration_factor
 // Serial.println();
  delay(1000);
}
