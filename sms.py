import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

shortcode = 
passkey = 

data_to_encode = shortcode + passkey+ formatted_time
encoded = base64.b64encode(data_to_encode.encode())

decoded_password = encoded.decode("utf-8")




consumer_key = 
consumer_secret = 
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']


  
def lipa_na_mpesa(request):
    if request.method == 'POST':
        phone  = 

        amount = 
        access_token = my_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
        "BusinessShortCode": shortcode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": shortcode,
        "PhoneNumber": phone,
        "CallBackURL": "https://linuxinvestors.com/signup",
        "AccountReference": phone,
        "TransactionDesc": "pay"
        }

        response = requests.post(api_url, json = request, headers=headers)
        
        lipa_na_mpesa()
        

        #print(response.text)
        
        
        


