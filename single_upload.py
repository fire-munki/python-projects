import requests
import key_file as key_file 
import inquirer
from os import listdir
from time import sleep
import shutil

siteId = key_file.MY_JW_SITE_ID
apiV2Key = key_file.MY_V2_API_KEY
filePath = key_file.VIDEO_FILE_PATH

print(filePath)
location = [
    inquirer.List(
        "option", 
        message="Are your files stored in the video folder shown", 
        choices=["Yes","No"],
        carousel=True
    ),
]

locationChoice = inquirer.prompt(location)

locationChoiceAnswer = locationChoice.get("option")

if locationChoiceAnswer == "No":
    print("Please enter the folder path:")
    filePath = input()

dirList = listdir(filePath)

videoList = []
for fileName in dirList:
    if fileName[-3:] in ["mp4", "m4a", "3gp", "avi", "mov", "wmv"]:
        videoList.append(fileName)

if videoList == []:
    print("No supported media in directory, program ending")
    exit()

mediaChoice = [
    inquirer.List(
        "option", 
        message = "Select the media to upload", 
        choices = videoList,
        carousel = True
    ),
]

file = inquirer.prompt(mediaChoice)

media = file.get("option")

meidaUrl = f"{filePath}{media}"

uploadedLocation = f"{filePath}uploaded/{media}"

print("Enter the media title:")
mediaTitle = input()

print("Enter the tag for the media:")
mediaTag = input()

url = f"https://api.jwplayer.com/v2/sites/{siteId}/media"
payload = {
    "upload": {
        "method": "direct"
    },
    "metadata": {
        "title": f"{mediaTitle}",
        "tags": [f"{mediaTag}"]
    }
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"{apiV2Key}"
}

response = requests.post(url, json=payload, headers=headers)

uploadUrl = response.json()["upload_link"]
mediaId = response.json()["id"]

requests.put(url=uploadUrl, data=open(meidaUrl, "rb").read())


url2 = f"https://api.jwplayer.com/v2/sites/{siteId}/media/{mediaId}"

headers = {
    "Accept": "application/json",
    "Authorization": apiV2Key
}

status = ""

while status != "ready":
    response = requests.get(url2, headers=headers)
    status = response.json()["status"]
    print(f"The media is in a {status} status")
    sleep(5)

shutil.move(meidaUrl, uploadedLocation)

print("You file has been upload to your JW Dashboard, and the orginal moved to the uploaded folder.")