import RPi.GPIO as pin
import requests
import random
import urllib # Python URL functions
import urllib2 # Python URL functions

pin.setmode(pin.BOARD)
pin.setup(40,pin.OUT);
pin.output(40,False)

adh=input("Enter the client Aadhaar number:-")
adh=str(adh)
s1=adh[12:16]

cph=input("Enter the client phone number:-")
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
print(res)
flag=0
while(True):
    var=input("Enter the Password using your OTP:-");
    var=str(var)
    res=res+s1
    print(res)
    if(var==res):
        pin.output(40,True)
        flag=0
    else:
        pin.output(40,False)
        print("Your password is incorrect")
        flag=flag+1
    if(flag==3):
        print("You are not eligible person you have to contact with admin:-")
        break

pin.cleanup()
