
import os
from twilio.rest import Client
from creds import auth_token, account_sid
# pip install twilio
# Find creds at values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure

def send_txt_message(message):
    # Numbers you want to send text messages to
    phone_numbers = ["+14345551212"]
    for phone_number in phone_numbers:
        client = Client(account_sid, auth_token)
        client.api.account.messages.create(
            to=phone_number,
            # Has to be a phonenumber you own in twilio
            # This is the number the text will be from
            from_="+19845551212",
            body=message)

