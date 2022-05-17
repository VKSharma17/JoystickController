#include<Servo.h>

Servo FBServo;
Servo LRServo;

int FBServoPos = 90;
int LRServoPos = 90;
char val;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(50);
  Serial.println("Type something!");
  FBServo.attach(7);
  FBServo.write(FBServoPos);
  LRServo.attach(9);
  LRServo.write(LRServoPos);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()) // if serial value is available 
{
  val = (char)Serial.read(); // read the serial value
  if (val == 'w') //forward
  {
    FBServo.write(FBServo.read() - 50);
//    FBServo.write(450);
    Serial.println("You pressed w FBServoPos = ");
    Serial.println(FBServo.read());
  }
  if (val == 's') //Back
  {
     FBServo.write(FBServo.read() + 50);
//    FBServo.write(1250);
    Serial.println("You pressed s FBServoPos = ");
    Serial.println(FBServo.read());
  }
   if (val == 'a') //left
  {
    LRServo.write(LRServo.read() + 50);
//    FBServo.write(450);
//    delay(100);
//    LRServo.write(120);
    Serial.println("You pressed a LRServoPos = ");
    Serial.println(LRServo.read());
  }
  if (val == 'd')// right
  {
    LRServo.write(LRServo.read() - 50);
//    FBServo.write(450);
//    delay(100);
//    LRServo.write(450);
    Serial.println("You pressed d LRServoPos = ");
    Serial.println(LRServo.read());
  }

    if (val == 'r')
  {
    FBServo.write(FBServoPos);
    LRServo.write(LRServoPos);
    Serial.println("You pressed r for reset ");
  }
}
}
