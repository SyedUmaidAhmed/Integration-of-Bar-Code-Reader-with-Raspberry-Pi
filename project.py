from signal import pause
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver
import os
import sys

GPIO.setwarnings(False)

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("  INDUS UNIVERSITY", 1)
mylcd.lcd_display_string("   BE-ELECTRICAL", 2)
mylcd.lcd_display_string("BATCH OF SPRING-16", 3)
mylcd.lcd_display_string("ENGR.ABDUL LATIF", 4)
time.sleep(10)
mylcd.lcd_clear()
mylcd.lcd_display_string("   [SMART TROLLEY] ", 1)
mylcd.lcd_display_string("Hamza (327S-2016)", 2)
mylcd.lcd_display_string("Sijad (121S-2016)", 3)
mylcd.lcd_display_string("Maaz  (796-2016)", 4)
time.sleep(10)
mylcd.lcd_clear()
mylcd.lcd_display_string("  SCAN BARCODE ON  ",1)
mylcd.lcd_display_string("   TROLLEY TO START ",2)
     
product = number = state = a = b = c = d = e = f = g = h = i = j = price = 0
string = ' ' 

barcodetoStart = '8001841420912'


barcode = ['95010816','8964000101957','8886950031309','8001841474922','671866116565','7622210844064','8961008215495',
           '8964001434535', '8961003514005', '8961014241167',barcodetoStart]



def allreset():
    global number,string,price,product 
    product = number = state = a = b = c = d = e = f = g = h = i = j = price = 0
    string = ' ' 
    
def removing():
    global string
    global number
    global product
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Removing %s" %string, 1)
    time.sleep(0.5)
    mylcd.lcd_clear()
    product = 0
    number-=1
    string = ' ' 
    

    
def Ghareeb():

    global string
    global product
    global number
    global price


    code = input("Enter your product here: ")
        
    if code==barcode[0]:
         global a
         a= not a
         string = 'CAPSTAN'
         if a==1:            
                 number+=1
                 product = 80                 
                 price += 80
         elif a==0:
                removing()
                price -= 80
    
    elif code==barcode[1]:
         global b
         b= not b
         string = 'SLICE'
         if b==1:
                 number+=1
                 
                 product = 25
                 price += 25
         elif b==0:
                removing()
                price -= 25
    
    elif code==barcode[2]:
        
         global c
         c= not c
         string = 'PALMOLIVE'
         if c==1:
                 number+=1
                 price += 150
                 product = 150
         elif c==0:
                removing()
                price -= 150
                
    
    elif code==barcode[3]:
         global d
         d= not d
         string = 'ARIEL'
         if d==1:
                 number+=1
                 price += 10
                 product = 10
         elif d==0:
                removing()
                price -= 10
    
    
    elif code==barcode[4]:
         global e
         e= not e
         string = 'SLANTY'
         if e==1:
                 number+=1
                 price += 10
                 product = 10
         elif e==0:
                removing()
                price -= 10
    
    elif code==barcode[5]:
         global f
         f= not f
         string = 'DAIRYMILK'
         if f==1:
                 number+=1
                 price += 15
                 product = 15
         elif f==0:
                removing()
                price -= 15

                
    elif code==barcode[6]:
         global g
         g= not g
         string = 'NESTLE EVERYDAY'
         if g==1:
                 number+=1
                 price += 15
                 product = 15
         elif g==0:
                removing()
                price -= 15
    
    elif code==barcode[7]:
         global h
         h= not h
         string = 'Choc Chips Min'
         if h==1:
                 number+=1
                 price += 5
                 product = 5
         elif h==0:
                removing()
                price -= 5

    elif code==barcode[8]:
         global i
         i= not i
         string = 'PRINCE PACK'
         if i==1:
                 number+=1
                 price += 105
                 product = 105
         elif i==0:
                removing()
                price -= 105

    elif code==barcode[9]:
         global j
         j= not j
         string = 'LIFEBUOY'
         if j==1:
                 number+=1
                 price += 40
                 product = 40
         elif j==0:
                removing()
                price -= 40


    elif code==barcode[10]:
         global state
         state = not state


    if state ==1:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Name: %s"%string,1)
        mylcd.lcd_display_string("Price: %d" %product ,2 )
        mylcd.lcd_display_string("Total Price: %d " %price, 3)
        mylcd.lcd_display_string("# of P: %d" %number,4)
        time.sleep(2)
    
    if state ==0:     
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Please Pay PKR %d   " % price,2)
        mylcd.lcd_display_string("THANK YOU!",4)
        time.sleep(10)
        mylcd.lcd_clear()
        global number,string,price,product
        product = number = state = a = b = c = d = e = f = g = h = i = j = price = 0
        string = ' ' 

        mylcd.lcd_display_string("SCAN BARCODE ON  ",1)
        mylcd.lcd_display_string("TROLLEY TO START ",2)

    else:
        string = 'UNKNOWN'
        product = 0


while True:
    Ghareeb()
