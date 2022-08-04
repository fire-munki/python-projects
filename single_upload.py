import requests
import key_file as key_file 
import inquirer
from os import listdir
from time import sleep

siteId = key_file.MY_JW_SITE_ID
apiV2Key = key_file.MY_V2_API_KEY

location = [
    inquirer.List(
        'option', 
        message='Are you files stored in the video folder? Y/N', 
        choices=['Yes','No'],
        carousel=True
    ),
]

locationChoice = inquirer.prompt(location)

locationChoiceAnswer = locationChoice.get('option')

if locationChoiceAnswer == 'Yes':
    filePath = key_file.VIDEO_FILE_PATH
else:
    print('Please enter the file path:')
    filePath = input()

dirList = listdir(filePath)

videoList = []
for fileName in dirList:
    if fileName.endswith('.mp4'):
        videoList.append(fileName)
    if fileName.endswith('.m4a'):
        videoList.append(fileName)
    if fileName.endswith('.3gp'):
        videoList.append(fileName)
    if fileName.endswith('.avi'):
        videoList.append(fileName)
    if fileName.endswith('.mov'):
        videoList.append(fileName)
    if fileName.endswith('.wmv'):
        videoList.append(fileName)

if videoList == []:
    print('No supported media in directory, program ending')
    exit()

mediaChoice = [
    inquirer.List(
        'option', 
        message = 'Select the media to upload', 
        choices = videoList,
        carousel = True
    ),
]

file = inquirer.prompt(mediaChoice)

media = file.get('option')

meidaUrl = f'{filePath}{media}'

print('Enter the media title and press return')
mediaTitle = input()

category = [
    inquirer.List(
        'option', 
        message='Select the media category and press return', 
        choices=['Automotive','Books and Literature','Business and Finance','Careers','Education','Events and Attractions','Family and Relationships','Fine Art','Food and Drink','Healthy Living','Hobbies and Interests','Home and Garden','Medical Health','Movies','Music and Audio','News and Politics','Personal Finance','Pets','Pop Culture','Real Estate','Religion and Spirituality','Science','Shopping','Sports','Style and Fashion','Technology and Computing','Television','Travel','Video Gaming'],
        carousel=True
    ),
]

choice = inquirer.prompt(category)

mediaCategory = choice.get('option')

print('Enter the tag for the media:')
mediaTag = input()

url = f'https://api.jwplayer.com/v2/sites/{siteId}/media'
payload = {
    'upload': {
        'method': 'direct'
    },
    'metadata': {
        'title': f'{mediaTitle}',
        'tags': [f'{mediaTag}'],
        'category': f'{mediaCategory}'
    }
}
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "Authorization": f'{apiV2Key}'
}

response = requests.post(url, json=payload, headers=headers)

uploadUrl = response.json()['upload_link']
mediaId = response.json()['id']

requests.put(url=uploadUrl, data=open(meidaUrl, 'rb').read())


url2 = f'https://api.jwplayer.com/v2/sites/{siteId}/media/{mediaId}'

headers = {
    "Accept": "application/json",
    "Authorization": apiV2Key
}

status = ''

while status != 'ready':
    response = requests.get(url2, headers=headers)
    status = response.json()['status']
    print(f'The media is in a {status} state')
    sleep(15)