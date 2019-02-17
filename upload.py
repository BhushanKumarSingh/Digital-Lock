
import RPi.GPIO as pin
import requests
import random
import urllib # Python URL functions
import urllib2 # Python URL functions

pin.setmode(pin.BOARD)
pin.setup(40,pin.OUT);
pin.output(40,True)
import sys
import re
def validateAdhar(adharNo):
    if((len(adharNo)==16) and (adharNo.isdigit())):
        return True
    else:
        print('Adhar Number Is Not Correct.Try Next Time')
        sys.exit()
        
def validateMobileNum(cph):
    if((len(cph)==10) and (cph.isdigit()) and (re.match("^[6789]",cph))):
        return True
    else:
        print('Mobile Number Is Not Correct.Try Next Time')
        sys.exit()

def takeMobileNum():
    cph=str(input("Enter the client Mobile number:-"))
    validateMobileNum(cph)
    return cph

def takeAdhar():
    adh=str(input("Enter the client Aadhaar number:-"))
    validateAdhar(adh)
    s1=adh[12:16]
    return s1
    
s1=takeAdhar()
cph=takeMobileNum()
otp=random.randint(1000, 9999)

authkey ="263274A9QZSUvL5c67f37d" # Your authentication key.

mobiles = str(cph) # Multiple mobiles numbers separated by comma.

message = str(otp) # Your message to send.

sender = "123456" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }


url = "http://sms1.codenicely.in/api/sendhttp.php?authkey="+authkey+"&mobiles="+mobiles+"&message="+message+"&sender="+sender+"&route="+route; # API URL

postdata = urllib.urlencode(values) # URL encoding the data here.

req = urllib2.Request(url, postdata)

response = urllib2.urlopen(req)

output = response.read() # Get Response

#print (output) # Print Response


otp=str(otp);
resp=requests.post('https://api.thingspeak.com/update?api_key=T09R2AH7YV0T8VFJ&field1='+otp)
print("Your password is successfully added")

res3=requests.get('https://api.thingspeak.com/channels/704469/feeds.json?api_key=NFMCKPOG553CYEEQ&results=1')
val3=res3.json()

res=val3["feeds"][0]["field1"]

res=res+s1
flag=0
while(True):
    var=input("Enter the Password using your OTP:-");
    var=str(var)
    
    print(res)
    if(var==res):
        pin.output(40,False)
        flag=0
    else:
        pin.output(40,True)
        print("Your password is incorrect")
        flag=flag+1
    if(flag==3):
        print("You are not eligible person you have to contact with admin:-")
        break

pin.cleanup()
