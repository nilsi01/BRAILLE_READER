

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // braile LED setup
  // Initialize each LED pin as an OUTPUT
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  braileconversion_loop();

  if 
}
