// Arduino DC motor speed and direction control

#define button   8
#define pot      0
#define pwm1     9
#define pwm2    10

boolean motor_dir = 0;
int motor_speed;
int LED=11;

void setup() {
  pinMode(button, INPUT_PULLUP);
  pinMode(pwm1,   OUTPUT);
  pinMode(pwm2,   OUTPUT);
}

void loop() {
 float in, out;
  motor_speed = analogRead(pot) / 4;
  if(motor_dir)
       {analogWrite(pwm1, motor_speed);
       analogWrite(LED,0);}
  else
   { analogWrite(pwm2, motor_speed);
for (in = 0; in < 6.283; in = in + 0.001)
  {
    out = sin(in) * 127.5 + 127.5;
    analogWrite(LED,out);
  }}
    
  if(!digitalRead(button)){                // If direction button is pressed
    while(!digitalRead(button));           // Wait until direction button released
    motor_dir = !motor_dir;                // Toggle direction variable
    if(motor_dir)
      digitalWrite(pwm2, 0);
    else
      digitalWrite(pwm1, 0);
  }
  }

