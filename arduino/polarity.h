#ifndef POLARITY_H
#define POLARITY_H

// Define H-bridge control pins
extern int motorAPin_A;  // Connected to A-1A terminal
extern int motorAPin_B;  // Connected to A-1B terminal

// Declare the functions
void polarity_on();
void polarity_off();

#endif