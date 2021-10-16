// This uses Serial Monitor to display Range Finder distance readings

// Include NewPing Library
#include "NewPing.h"

// Hook up HC-SR04 with Trig to Arduino Pin 9, Echo to Arduino pin 10
#define TRIGGER_PIN_1 53
#define ECHO_PIN_1 52

#define TRIGGER_PIN_2 51
#define ECHO_PIN_2 50

#define TRIGGER_PIN_7 47
#define ECHO_PIN_7 46

#define TRIGGER_PIN_8 49
#define ECHO_PIN_8 48

// Maximum distance we want to ping for (in centimeters).
#define MAX_DISTANCE 400  

// NewPing setup of pins and maximum distance.
NewPing sonar1(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE);
NewPing sonar2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE);
NewPing sonar7(TRIGGER_PIN_7, ECHO_PIN_7, MAX_DISTANCE);
NewPing sonar8(TRIGGER_PIN_8, ECHO_PIN_8, MAX_DISTANCE);
float duration, distance1, distance2, distance7, distance8;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Send ping, get distance in cm
  distance1 = sonar1.ping_cm();
  distance2 = sonar2.ping_cm();
  distance7 = sonar7.ping_cm();
  distance8 = sonar8.ping_cm();
  
  // Send results to Serial Monitor
  Serial.print("Distance1 = ");
  
  if (distance1 >= 400 || distance1 <= 2) 
  {
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance1);
    Serial.println(" cm");
  }
  // SENSOR 2
  Serial.print("Distance2 = ");
  
  if (distance2 >= 400 || distance2 <= 2) 
  {
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance2);
    Serial.println(" cm");
  }

  ///////////////// SENSOR 7
  Serial.print("Distance7 = ");
  
  if (distance7 >= 400 || distance7 <= 2) 
  {
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance7);
    Serial.println(" cm");
  }


  ///////////// SENSOR 8
  Serial.print("Distance8 = ");
  
  if (distance8 >= 400 || distance8 <= 2) 
  {
    Serial.println("Out of range");
  }
  else 
  {
    Serial.print(distance8);
    Serial.println(" cm");
  }


  
  delay(2000);
}
