void setup() {
  Serial.begin(9600);  // Initialize serial communication
  pinMode(2, OUTPUT);  // Set digital pin 13 as an output (example)
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();  // Read the incoming byte
    if (received == '1') {          // if Digital Pin 2 gets 1, turn on
      digitalWrite(2, HIGH);        // Turn on the LED
      delay(1000);
      digitalWrite(2, LOW);  // Turn on the LED
      delay(1000);
    } else if (received == '0') {
      digitalWrite(2, LOW);  // Turn off the LED
    }
  }
}
