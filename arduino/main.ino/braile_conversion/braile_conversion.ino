// #include "polarity.h"




// Define pins for each LED
const int braile1 = 2;  // Dot 1
const int braile2 = 3;  // Dot 2
const int braile3 = 4;  // Dot 3
const int braile4 = 5;  // Dot 4
const int braile5 = 6;  // Dot 5
const int braile6 = 7;  // Dot 6

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}


// Braille representations for characters (1 = ON, 0 = OFF)
const byte braillePatterns[36][6] = {
  // Letters A-Z
  { 1, 0, 0, 0, 0, 0 },  // A
  { 1, 1, 0, 0, 0, 0 },  // B
  { 1, 0, 0, 1, 0, 0 },  // C
  { 1, 0, 0, 1, 1, 0 },  // D
  { 1, 0, 0, 0, 1, 0 },  // E
  { 1, 1, 0, 1, 0, 0 },  // F
  { 1, 1, 0, 1, 1, 0 },  // G
  { 1, 1, 0, 0, 1, 0 },  // H
  { 0, 1, 0, 1, 0, 0 },  // I
  { 0, 1, 0, 1, 1, 0 },  // J
  { 1, 0, 1, 0, 0, 0 },  // K
  { 1, 1, 1, 0, 0, 0 },  // L
  { 1, 0, 1, 1, 0, 0 },  // M
  { 1, 0, 1, 1, 1, 0 },  // N
  { 1, 0, 1, 0, 1, 0 },  // O
  { 1, 1, 1, 1, 0, 0 },  // P
  { 1, 1, 1, 1, 1, 0 },  // Q
  { 1, 1, 1, 0, 1, 0 },  // R
  { 0, 1, 1, 1, 0, 0 },  // S
  { 0, 1, 1, 1, 1, 0 },  // T
  { 1, 0, 1, 0, 0, 1 },  // U
  { 1, 1, 1, 0, 0, 1 },  // V
  { 0, 1, 0, 1, 1, 1 },  // W
  { 1, 0, 1, 1, 0, 1 },  // X
  { 1, 0, 1, 1, 1, 1 },  // Y
  { 1, 0, 1, 0, 1, 1 },  // Z

  // Numbers 1-9 (represented by A-J)
  { 1, 0, 0, 0, 0, 0 },  // 1
  { 1, 1, 0, 0, 0, 0 },  // 2
  { 1, 0, 0, 1, 0, 0 },  // 3
  { 1, 0, 0, 1, 1, 0 },  // 4
  { 1, 0, 0, 0, 1, 0 },  // 5
  { 1, 1, 0, 1, 0, 0 },  // 6
  { 1, 1, 0, 1, 1, 0 },  // 7
  { 1, 1, 0, 0, 1, 0 },  // 8
  { 0, 1, 0, 1, 0, 0 },  // 9
  { 0, 1, 0, 1, 1, 0 },  // 0 (this is letter J in Braille, but in numeric context it represents 0)
};

// Function to display a Braille character based on the letter index (0 = 'A', 25 = 'Z', 26-35 = '0'-'9')
void displayBrailleCharacter(int charIndex) {
  // Ensure the index is within range
  if (charIndex < 0 || charIndex > 35) return;

  // Set each LED according to the Braille pattern [charindex[X]] defines the position of a symbol within one of the arrays, charsymbol 0 for example is always the first
  digitalWrite(braile1, braillePatterns[charIndex][0]);
  digitalWrite(braile2, braillePatterns[charIndex][1]);
  digitalWrite(braile3, braillePatterns[charIndex][2]);
  digitalWrite(braile4, braillePatterns[charIndex][3]);
  digitalWrite(braile5, braillePatterns[charIndex][4]);
  digitalWrite(braile6, braillePatterns[charIndex][5]);

  // polarity_on();
  // polarity_off();
}

void loop() {
  // Check if a character has been entered in the Serial Monitor
  if (Serial.available() > 0) {
    char inputChar = Serial.read();  // Read the character

    // Convert to uppercase if needed
    inputChar = toupper(inputChar);

    // Check if it's a valid letter or number (A-Z, 0-9)
    if ((inputChar >= 'A' && inputChar <= 'Z')) {
      int letterIndex = inputChar - 'A';     // Convert letter to index (A=0, B=1, ..., Z=25)
      displayBrailleCharacter(letterIndex);  // Display the Braille pattern for the letter
      Serial.print("Displaying Braille for: ");
      Serial.println(inputChar);
    } else if (inputChar >= '0' && inputChar <= '9') {
      int numberIndex = inputChar - '0' + 26;  // Convert number to index (0=26, 1=27, ..., 9=35)
      displayBrailleCharacter(numberIndex);    // Display the Braille pattern for the number
      Serial.print("Displaying Braille for: ");
      Serial.println(inputChar);
    }
  }
}
