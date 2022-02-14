import json
import requests


def magi_base64Decode(payload):

	data = json.dumps({"input": payload,"recipe":{"op":"From Base64","args":["A-Za-z0-9+/=",True]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

def magi_base64Encode(payload):

	data = json.dumps({"input": payload,"recipe":{"op":"To Base64","args":["A-Za-z0-9+/="]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value


def magi_morseEncode(payload):

	data = json.dumps({"input": payload,"recipe":{"op":"To Morse Code","args":["-/.","Space","Line feed"]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

def magi_morseDecode(payload):

	data = json.dumps({"input": payload,"recipe":{"op":"From Morse Code","args":["Space","Line feed"]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

def magi_base85Encode(payload):
	data = json.dumps({"input": payload,"recipe":{"op":"To Base85","args":["!-u",False]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

def magi_base85Encode(payload):
	data = json.dumps({"input": payload,"recipe":{"op":"To Base85","args":["!-u",False]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value


def magi_base85Decode(payload):
	data = json.dumps({"input": payload,"recipe":{"op":"From Base85","args":["!-u"]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

def magi_atbash(payload):

	data = json.dumps({"input": payload,"recipe":{"op":"Atbash Cipher","args":[]},"outputType":"string"})
	API_ENDPOINT = "http://localhost:3000/bake"
	headers_dict = {"Content-Type":"application/json"}

	# #sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, headers=headers_dict,data = data)
  
	# # # # extracting response text 
	value_received = json.loads(r.text)

	value = value_received['value']

	return value

