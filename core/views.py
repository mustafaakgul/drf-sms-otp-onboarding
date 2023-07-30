from django.shortcuts import render


# def index(request):
#     # Download the helper library from https://www.twilio.com/docs/python/install
#     import os
#     from twilio.rest import Client
#
#     # Step 1: Authentication or Create a Verification Service
#     # Find your Account SID and Auth Token at twilio.com/console
#     # and set the environment variables. See http://twil.io/secure
#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     client = Client(account_sid, auth_token)
#
#     service = client.verify.v2.services.create(
#         friendly_name='My First Verify Service'
#     )
#
#     print(service.sid)
#
#     # Step 2: Generate a Verification Token
#     import os
#     from twilio.rest import Client
#
#     # Find your Account SID and Auth Token at twilio.com/console
#     # and set the environment variables. See http://twil.io/secure
#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     client = Client(account_sid, auth_token)
#
#     verification = client.verify \
#         .v2 \
#         .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
#         .verifications \
#         .create(to='+15017122661', channel='sms')
#
#     print(verification.status)
#
#     # Step 3: Check the Verification Token
#     import os
#     from twilio.rest import Client
#
#     # Find your Account SID and Auth Token at twilio.com/console
#     # and set the environment variables. See http://twil.io/secure
#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     client = Client(account_sid, auth_token)
#
#     verification_check = client.verify \
#         .v2 \
#         .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
#         .verification_checks \
#         .create(to='+15017122661', code='123456')
#
#     print(verification_check.status)
#
#     return render(request, 'index.html')
