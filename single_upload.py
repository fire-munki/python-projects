import requests
import key_file 
import inquirer
import time

siteId = key_file.MY_JW_SITE_ID
apiV2Key = key_file.MY_V2_API_KEY

category = [
    inquirer.List(
        'option', 
        message='Select the media category and press return', 
        choices=['Automotive','Books and Literature','Business and Finance','Careers','Education','Events and Attractions','Family and Relationships','Fine Art','Food and Drink','Healthy Living','Hobbies and Interests','Home and Garden','Medical Health','Movies','Music and Audio','News and Politics','Personal Finance','Pets','Pop Culture','Real Estate','Religion and Spirituality','Science','Shopping','Sports','Style and Fashion','Technology and Computing','Television','Travel','Video Gaming'],
        carousel=True
    ),
]

print('Enter the full file path of the media to upload')
file_path = input()

print('Enter the media title and press return')
mediaTitle = input()

choice = inquirer.prompt(category)
mediaCategory = choice.get('option')

url = f'https://api.jwplayer.com/v2/sites/{siteId}/media'
payload = {
    'upload': {
        'method': 'direct'
    },
    'metadata': {
        'title': f'{mediaTitle}',
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

requests.put(url=uploadUrl, data=open(file_path, 'rb').read())


url2 = f'https://api.jwplayer.com/v2/sites/{siteId}/media/{mediaId}'

headers = {
    "Accept": "application/json",
    "Authorization": apiV2Key
}

status = ''

while status != 'ready':
    response = requests.get(url2, headers=headers)
    status = response.json()['status']
    print('The media is in a {} state'.format(status))
    time.sleep(30)

print('The media is now {}'.format(status))