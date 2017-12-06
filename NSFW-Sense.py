##################################################
#			Author: Atri Tripathi
##################################################

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from twilio.rest import Client
import json
import requests

# Enter the Image URL to be searched for NFSW content
sense_url = 'http://www.abeautyclub.com/wp-content/uploads/2013/01/Beauty-Icons-Pictures-of-Beautiful-Women-03.jpg'

app = ClarifaiApp(api_key='ad566cd963be453589a7610f042683c5')

model = app.models.get('nsfw-v1.0')
image = ClImage(url = sense_url)
response = model.predict([image])

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
	if concept["name"] == "sfw":
		sfw_val = concept["value"]
	if concept["name"] == "nsfw":
		nsfw_val = concept["value"]
    
print("sfw: ", sfw_val)
print("nsfw: ", nsfw_val)

# JSON data to be fed as a POST Request to Hasura's Data API table
data = {
	"type": "bulk",
	"args": [
		{
			"type": "delete",
			"args": {
				"table": "clarifai_nsfw",
				"where": {}
			}
		},
		{
			"type": "insert",
			"args": {
				"table": "clarifai_nsfw",
				"objects": [
					{
						"sfw": sfw_val,
						"nsfw": nsfw_val
					}
				]
			}
		}
	]
}

request = requests.post("https://data.forgone31.hasura-app.io/v1/query", data=json.dumps(data))
print(request.json())		# Get and print response for any errors

def send_sms():
	url = "https://notify.forgone31.hasura-app.io/v1/send/sms"

	# This is the json payload for the query
	requestPayload = {
		"to": "<Enter the mobile number to send message to>",			# eg: 9913426728
		"countryCode": "<Enter the country code>",						# eg: 91 for India
		"message": "Alert! Your child is viewing explicit content which might not be safe for work."
	}

	# Setting headers
	headers = {
		"Content-Type": "application/json",
		"Authorization": "Bearer b9ab86a30e592215d3e00ea922ef507524de44773c4356ef"
	}

	# Make the query and store response in sms
	sms = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	# sms.content contains the json response.
	print(sms.content)
	
def make_call():

	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC66765cb9e59399b3636e356346ceb096"
	auth_token = "5abaaca1210415d0300e7312de0b8168"
	client = Client(account_sid, auth_token)
	
	# The mobile number entered below, should be of the format +918602783457, begnning with <+country_code>
	call = client.calls.create(to="<Enter mobile no. to make alert call>", from_="+14159935460", url="https://handler.twilio.com/twiml/EHedeb19a47c8ec0abe3d447268ede7ebf")
	
	print(call.sid)				# Get and print response for any errors

if(nsfw_val >= 0.25):
	send_sms()
	make_call()



















