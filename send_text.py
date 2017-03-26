from twilio import rest

# Find these values at https://twilio.com/user/account
account_sid = "AC01c614c48682af05e7a4f5768f0b1054"
auth_token = "59765c42a4db89719b78df42ec2996df"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+919910883713", from_="+14243245290",
                                     body="zxcsdskjdhgsj")
