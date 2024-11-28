/**
 * H-bridge control for switching the polarity of an electromagnet
 */

// Define H-bridge control pins
int motorAPin_A = 8; // Connected to A-1A terminal
int motorAPin_B = 9; // Connected to A-1B terminal

void setup() {
  // Set the control pins as OUTPUT
  pinMode(motorAPin_A, OUTPUT);
  pinMode(motorAPin_B, OUTPUT);
}

void loop() {
  // Activate electromagnet in one polarity
  digitalWrite(motorAPin_A, HIGH); // Set one pin HIGH
  digitalWrite(motorAPin_B, LOW);  // Set the other pin LOW
  delay(3000);                     // Hold for 3 seconds

  // Turn off the electromagnet
  digitalWrite(motorAPin_A, LOW);
  digitalWrite(motorAPin_B, LOW);
  delay(500);                     // Optional pause for 1 second

  // Activate electromagnet in the opposite polarity
  digitalWrite(motorAPin_A, LOW);  // Set one pin LOW
  digitalWrite(motorAPin_B, HIGH); // Set the other pin HIGH
  delay(3000);                     // Hold for 3 seconds

  // Turn off the electromagnet
  digitalWrite(motorAPin_A, LOW);
  digitalWrite(motorAPin_B, LOW);
  delay(500);                     // Optional pause for 1 second
}
