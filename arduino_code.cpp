// Pin definitions
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 13;
const int buzzerPin = 8;

// Variables for ultrasonic sensor
long duration;
int distance;

void setup() {
  // Start serial communication
  Serial.begin(9600);

  // Set pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Send a pulse to the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the duration of the pulse
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  distance = duration * 0.0344 / 2;

  // Display the distance
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check distance and act accordingly
  if (distance < 10) {
    digitalWrite(ledPin, HIGH);  // Turn on LED
    tone(buzzerPin, 1000);        // Play tone on buzzer
  } else {
    digitalWrite(ledPin, LOW);   // Turn off LED
    noTone(buzzerPin);            // Stop buzzer tone
  }

  delay(500);  // Small delay before next reading
}
