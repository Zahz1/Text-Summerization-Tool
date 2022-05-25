import requests, json


PathData = "data.txt"
PathResults = "Results/SMMRY.txt"

#load data from file into text var
fileIn = open(PathData, "r")
text = fileIn.read().replace("\n", " ")
fileIn.close()

#SMMRY_API
key = "A7466B3D36" #add in your own key here
SMMRY_apiKey = "SM_API_KEY=" + key
sentenceCount = 1
SMMRY_apiLen = "SM_LENGTH=" + str(sentenceCount)
apiURL = "https://api.smmry.com"

#print(apiURL + "/&" + SMMRY_apiKey)

#send api request
#SM_URL needs to be at end of request
response = requests.post(apiURL + "/&" + SMMRY_apiKey + "&" + SMMRY_apiLen, data = {"sm_api_input": text})
#print(response.status_code)

#get data from json return request
data = json.loads(response.text)
output = str(data['sm_api_content'])
print(output)

#output data to file
fileOut = open(PathResults, "w")
fileOut.write(output)
fileOut.close()
