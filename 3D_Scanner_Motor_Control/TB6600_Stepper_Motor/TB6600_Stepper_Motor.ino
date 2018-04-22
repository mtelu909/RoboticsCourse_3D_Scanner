int PUL=7; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=5; //define Enable Pin

String rpmString = String();
int conv_int = 50;
int cycle = 0;
long int n = 0;
//------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
  
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);

}

void forward(int count, int rpm){
  for (int i=0; i<count; i++)    //Forward n steps
  {
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(rpm);
    digitalWrite(PUL,LOW);
    delayMicroseconds(rpm);
  }
}

void reverse(int count, int rpm){
  for (int i=0; i<count; i++)   //Backward n steps
  {
    digitalWrite(DIR,HIGH);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(rpm);
    digitalWrite(PUL,LOW);
    delayMicroseconds(rpm);
  }
}

void full_stop(){
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,LOW);
    digitalWrite(PUL,LOW);
    //delayMicroseconds(rpm);
    //digitalWrite(PUL,LOW);
    //delayMicroseconds(rpm);
}
// -----------------------------------------------------------------
void loop() {
 cycle = 10000;
 
// SERIAL DATA IN -------------
 
if(Serial.available()){
  String datain = String(Serial.read());
  int data1 = datain.toInt();
  delay(250);
  // data1 = # of pictures that will be taken (ex: 29)
}

//-------------------------------
 
 while (Serial.available()) {
    char c = Serial.read();  //gets one byte from serial buffer
    rpmString += c; //makes the String readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (rpmString.length() > 0) {
    Serial.print("Current delay value is: ");
    Serial.print(rpmString);  //so you can see the captured String 
    Serial.println(" microseconds");
    conv_int = rpmString.toInt();  //convert readString into a number
    //Serial.println(conv_int);
    rpmString="";
  } 
  else{
    conv_int = conv_int;
  }
 
 
 if (n > 0 && n < 156){
  forward(cycle,conv_int);
 }
 else if (n > 156 && n < 308){
  reverse(cycle,conv_int);
  
 }
 else{
  full_stop(); 
 }
 n = n + 1;
 
// SERIAL DATA OUT ----------
 
 char dataout[1];
 int data = n;                    // max number is +- 32767
 String dataout = String(data);
 Serial.println(dataout);
 delay(100);             

// -----------------------------
 
 //Serial.print(" Cycle value n = ");
 //Serial.println(n);
  
}
