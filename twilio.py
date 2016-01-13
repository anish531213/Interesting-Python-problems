from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "ACed408ebc5e3b0fe9fd0abd85c44d4d6a"
auth_token = "feaae90aca2e9b5201ffacc22027cb2a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+12027962346", from_="+14694477001",
                                     body="Hello there!")
