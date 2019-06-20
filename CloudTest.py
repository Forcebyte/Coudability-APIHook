#Sample Cost Sharing Splitter

import json
import requests

#API structure - API token needed, leave the second string blank as Cloudability uses NormalMapping API
api_token = ('YOUR API TOKEN','')

def Cloudability_BusinessMap_Fetch(api_token,map_id):
    '''
	Cloudability_BusinessMap_Fetch(api_token) -> timedict
		Takes a given API token and mapping ID, and fetches a given Business Mapping
	'''
    api_url = 'https://api.cloudability.com/v3/business-mappings/' + str(map_id)
    webresponse = requests.get(
        api_url,
        auth=api_token
    )
    return(webresponse)

def Cloudability_BusinessMap_Post(api_token,jsonfile):
    '''
	Cloudability_BusinessMap_Fetch(api_token,jsonfile) -> Web Response
		Takes a given json and posts it to Cloudability
	'''
    api_url = 'https://api.cloudability.com/v3/business-mappings'
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    webresponse = requests.post(
        api_url,
        auth=api_token,
        data=open(jsonfile, 'rb'),
        headers=headers
    )
    return(webresponse)

Choice = input('Would you like to \nPost a Cloudability Business Mapping? - 1\nFetch a Cloudability Business Mapping - 2\n=========================================\n')
if str(Choice) == '1':
    '''
    Sample Business Mapping Fetch format - posts JSON file to Cloudability
    '''
    jsonfile = input('Please Enter the full or local path to the JSON file you want to send to Cloudability: ')
    Response = Cloudability_BusinessMap_Post(api_token,jsonfile)
    print(Response)
elif str(Choice) == '2':
    '''
    Sample Business Mapping Fetch format - grabs business mapping at 'n' index
    '''
    indexnum = input('Please Enter the suspected Index number for the Business Mapping you are trying to fetch: ')
    Response_Get = Cloudability_BusinessMap_Fetch(api_token,int(indexnum))
    print(Response_Get)
    json_data = json.loads(Response_Get.text)
    filename = input('Enter the file name you would like the JSON file to be saved under: ')
    with open(str(filename), 'w') as json_import:
        json_import.write(Response_Get.text)
else:
    print("Invalid Choice, exiting")