import request

BASE = 'https://api.twilio.com/'
VERSION = '2010-04-01/'
API = BASE + VERSION

ACCOUNT_SID = 'AC4b1eef4d8e640e8209bd55be229cb527'
TOKEN = '0f3a8ff44c9daa46919b5192dd5e7da9'
NUMBER = '+7149801295'


sendMessage(to_number, body):
	ENDPOINT = 'API/Accounts/' + ACCOUNT_SID + '/Messages.json'
	payload = {
		'From': NUMBER,
		'To': to_number,
		'Body': body
	}

	r = requests.post(ENDPOINT, data=payload, auth=(ACCOUNT_SID, TOKEN))
	print(r)
