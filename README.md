#Led Blink on message

Python program that works on Rasberry Pi and Grove pi . 

LED connected to port 4 ( or) update led_blink.py to udpate
the port number connected to Grove 

Create an account in pubnub.com and setup the publish and subscribe keys
in app.py


#Related projects
Alexa Trigger - https://github.com/arun2dot0/AlexaNodeJS
Data Integration Code - https://github.com/arun2dot0/metrics-rest-service-redis

#Demo
[Imgur](http://i.imgur.com/CbwxkHh.gifv)

#Run 
python app.py 

LED will turn on and print message when message "on" is sent to pubnub
LED will turn off and pring message when message "off" is sent to pubnub