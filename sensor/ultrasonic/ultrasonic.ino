#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include "SR04.h"
int TRIG_PIN = 26;
int ECHO_PIN = 25;
SR04 sr04(ECHO_PIN, TRIG_PIN);
int d;

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup()
{
  Serial.begin(9600);
  lcd.init(); // initialize the lcd 
  lcd.init();
  
  // Print a message to the LCD.
  lcd.backlight();
  lcd.setCursor(6,0);
  lcd.print("Standby...");
  delay(2000);
}

void loop()
{
  d = (int)sr04.Distance(); 

  if (d <= 100) {
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(1, 0);
    lcd.print("Welcome, user! :3");
    delay(10000);
    Serial.println("ON");
  } else {
    lcd.clear();
    lcd.noBacklight();
    Serial.println("OFF");
  }

  delay(1000);
}
