// Define pins for each LED
const int led1 = 2;  // Dot 1
const int led2 = 3;  // Dot 2
const int led3 = 4;  // Dot 3
const int led4 = 5;  // Dot 4
const int led5 = 6;  // Dot 5
const int led6 = 7;  // Dot 6

// Braille representations for letters (lowercase)
// Each entry in the array represents a Braille character (1 = ON, 0 = OFF)
const byte braillePatterns[26][6] = {
    {1, 0, 0, 0, 0, 0},  // A
    {1, 1, 0, 0, 0, 0},  // B
    {1, 0, 0, 1, 0, 0},  // C
    {1, 0, 0, 1, 1, 0},  // D
    {1, 0, 0, 0, 1, 0},  // E
    {1, 1, 0, 1, 0, 0},  // F
    {1, 1, 0, 1, 1, 0},  // G
    {1, 1, 0, 0, 1, 0},  // H
    {0, 1, 0, 1, 0, 0},  // I
    {0, 1, 0, 1, 1, 0},  // J
    {1, 0, 1, 0, 0, 0},  // K
    {1, 1, 1, 0, 0, 0},  // L
    {1, 0, 1, 1, 0, 0},  // M
    {1, 0, 1, 1, 1, 0},  // N
    {1, 0, 1, 0, 1, 0},  // O
    {1, 1, 1, 1, 0, 0},  // P
    {1, 1, 1, 1, 1, 0},  // Q
    {1, 1, 1, 0, 1, 0},  // R
    {0, 1, 1, 1, 0, 0},  // S
    {0, 1, 1, 1, 1, 0},  // T
    {1, 0, 1, 0, 0, 1},  // U
    {1, 1, 1, 0, 0, 1},  // V
    {0, 1, 0, 1, 1, 1},  // W
    {1, 0, 1, 1, 0, 1},  // X
    {1, 0, 1, 1, 1, 1},  // Y
    {1, 0, 1, 0, 1, 1}   // Z
};

// Function to display a Braille character based on the letter index (0 = 'A', 25 = 'Z')
void displayBrailleCharacter(int letterIndex) {
    // Ensure the index is within range
    if (letterIndex < 0 || letterIndex > 25) return;

    // Set each LED according to the Braille pattern
    digitalWrite(led1, braillePatterns[letterIndex][0]);
    digitalWrite(led2, braillePatterns[letterIndex][1]);
    digitalWrite(led3, braillePatterns[letterIndex][2]);
    digitalWrite(led4, braillePatterns[letterIndex][3]);
    digitalWrite(led5, braillePatterns[letterIndex][4]);
    digitalWrite(led6, braillePatterns[letterIndex][5]);
}

void setup() {
    // Initialize each LED pin as an OUTPUT
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
    pinMode(led6, OUTPUT);

    // Begin serial communication
    Serial.begin(9600);
    Serial.println("Enter a letter to display its Braille representation:");
}

void loop() {
    // Check if a character has been entered in the Serial Monitor
    if (Serial.available() > 0) {
        char inputChar = Serial.read();  // Read the character

        // Convert to uppercase if needed
        inputChar = toupper(inputChar);

        // Check if it's a valid letter (A-Z)
        if (inputChar >= 'A' && inputChar <= 'Z') {
            int letterIndex = inputChar - 'A';  // Convert letter to index (A=0, B=1, ..., Z=25)
            displayBrailleCharacter(letterIndex); // Display the Braille pattern for the letter
            Serial.print("Displaying Braille for: ");
            Serial.println(inputChar);
        } else {
            Serial.println("Please enter a letter (A-Z).");
        }
    }
}