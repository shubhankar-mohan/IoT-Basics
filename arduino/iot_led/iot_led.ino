char val;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if(Serial.available() > 0) {
    val = Serial.read();
    delay(200);
    if(val == '1'){
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.print("Device ON");
      delay(200);
      }
   if(val == '0'){
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("Device OFF");
    delay(200);
    }
    
  }
}
