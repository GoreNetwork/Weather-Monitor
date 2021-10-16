
import os
from twilio.rest import Client
from creds import auth_token, account_sid
# pip install twilio
# Find creds at values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure

def send_txt_message(message):
    phone_numbers = ["+14348412662"]
    for phone_number in phone_numbers:
        client = Client(account_sid, auth_token)
        client.api.account.messages.create(
            to=phone_number,
            #Has to be a phonenumber you own in twilio
            from_="+19842082527",
            body=message)

