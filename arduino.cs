#include <SoftwareSerial.h>
int IRPin = 3;
int value=0;
SoftwareSerial mySerial(9, 10);
void setup()
{
  mySerial.begin(115200);    
  Serial.begin(115200);    
  delay(100);
   pinMode(IRPin, INPUT);  
  Serial.begin(115200); 
}


void loop()
{
    value = digitalRead(IRPin);
  Serial.println(value);  
  if (Serial.available()>0)
   {
       if(value!=0)
       SendMessage();
      
      else
       RecieveMessage();
     
   }

 if (mySerial.available()>0)
   Serial.write(mySerial.read());
}


 void SendMessage()
{
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"+91xxxxxxxxxx\"\r"); // Replace x with mobile number
  delay(1000);
  mySerial.println("There has been an accident");// The SMS text you want to send
  delay(100);
   mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(1000);
}


 void RecieveMessage()
{
  mySerial.println("AT+CNMI=2,2,0,0,0"); // AT Command to receive a live SMS
  delay(1000);
 }
 
