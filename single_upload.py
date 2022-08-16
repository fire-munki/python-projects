import requests
import key_file as key_file 
import inquirer
from os import listdir
from time import sleep

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
    if fileName[-3:] in ["mp4","m4a","3gp","avi","mov","wmv"]:
        videoList.append(fileName)

if not videoList:
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

print("Enter the media title and press return")
mediaTitle = input()

category = [
    inquirer.List(
        "option", 
        message="Select the media category and press return", 
        choices=[
            "Automotive",
            "Books and Literature",
            "Business and Finance",
            "Careers",
            "Education",
            "Events and Attractions",
            "Family and Relationships",
            "Fine Art",
            "Food and Drink",
            "Healthy Living",
            "Hobbies and Interests",
            "Home and Garden",
            "Medical Health",
            "Movies",
            "Music and Audio",
            "News and Politics",
            "Personal Finance",
            "Pets",
            "Pop Culture",
            "Real Estate",
            "Religion and Spirituality",
            "Science",
            "Shopping",
            "Sports",
            "Style and Fashion",
            "Technology and Computing",
            "Television",
            "Travel",
            "Video Gaming"
        ],
        carousel=True
    ),
]

choice = inquirer.prompt(category)

mediaCategory = choice.get("option")

print("Enter the tag for the media:")
mediaTag = input()

response = requests.post(
    url = f"https://api.jwplayer.com/v2/sites/{siteId}/media",
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"{apiV2Key}"
    },
    json = {
        "upload": {
            "method": "direct"
        },
        "metadata": {
            "title": f"{mediaTitle}",
            "tags": [f"{mediaTag}"],
            "category": f"{mediaCategory}"
        }
    }
)

uploadUrl = response.json()["upload_link"]
mediaId = response.json()["id"]

requests.put(url=uploadUrl, data=open(meidaUrl, "rb").read())

status = ""

while status != "ready":
    response = requests.get(
        headers={
        "Accept": "application/json",
        "Authorization": apiV2Key
    },
    url=f"https://api.jwplayer.com/v2/sites/{siteId}/media/{mediaId}",
    )
    status = response.json()["status"]
    print(f"The media is in a '{status}' status")
    sleep(15)
