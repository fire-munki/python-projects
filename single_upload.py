import requests
import variableFile 

siteId = variableFile.MY_JW_SITE_ID
apiV2Key = variableFile.MY_V2_API_KEY

category = ['0 Automotive','1 Books and Literature','2 Business and Finance','3 Careers','4 Education','5 Events and Attractions','6 Family and Relationships','7 Fine Art','8 Food &amp; Drink','9 Healthy Living','10 Hobbies &amp; Interests','11 Home &amp; Garden','12 Medical Health','13 Movies','14 Music and Audio','15 News and Politics','16 Personal Finance','17 Pets','18 Pop Culture','19 Real Estate','20 Religion &amp; Spirituality','21 Science','22 Shopping','23 Sports','24 Style &amp; Fashion','25 Technology &amp; Computing','26 Television','27 Travel','28 Video Gaming']

print('Enter the media title and press return')
mediaTitle = input()

for i in category:
    print(i)

print('Enter the media category number and press return')
mediaCategory = category[int(input())]


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

# print(mediaTitle)
# print(mediaCategory)
# print(apiV2Key)
print(response.text)
