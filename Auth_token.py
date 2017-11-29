Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
Code: 
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC97d26327e6d81f889e210134cbabf940"
auth_token = "9b81a6156300bfcfc21ba043d22f24a5"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+13012049407",
    from_="+12407861570",
    body="Hello there!",
    media_url=['https://demo.twilio.com/owl.png',
               'https://demo.twilio.com/logo.png'])

import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    resp.message('Sent from Twilio via INST126 Project')
    
    return str(resp)

if __name__ == "__main__"




Additional resources:
Useful video if you want to explore: https://www.youtube.com/watch?v=uzBRycRYsqw&ab_channel=CleverProgrammer 

https://www.twilio.com/docs/tutorials/workflow-automation-python-flask#workflow-building-blocks 
https://www.twilio.com/docs/ Docs for Twilio
https://developers.google.com/civic-information/ This is the Civic Info API
Phone: 12407861570
account_sid = "AC97d26327e6d81f889e210134cbabf940"
auth_token = "9b81a6156300bfcfc21ba043d22f24a5"
