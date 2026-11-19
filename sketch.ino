const int ledPin = 8;

void setup() {
  // Set LED pin as output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn LED ON for 3 seconds
  digitalWrite(ledPin, HIGH);
  delay(3000);

  // Turn LED OFF for 1 second
  digitalWrite(ledPin, LOW);
  delay(1000);
}
