char dataString[50] = {0};
int a = 50;
int g[]  = {5};

void setup() {
Serial.begin(19200);              //Starting serial communication
}
  
void loop() {
  g[0]=g[0]+5;                          // a value increase every loop
  sprintf(dataString,"%02X",g[0]); // convert a value to hexa 
  //Serial.println(datastring);   // send the data
  //Serial.println(a);
  //Serial.print(g,HEX);
  Serial.println(dataString);
  //delay(1000);                  // give the loop some break
 
}
