from datetime  import datetime
from urllib import response
import key_file
import inquirer
import requests

nasaKey = key_file.MY_NASA_API_KEY

print('What is your year of birth')
year = int(input())

if year < 1900:
    print('Records aren\'t avaiable this far back' )
    exit()

monthList = [
    inquirer.List(
        'option', 
        message = 'What is your month of birth', 
        choices = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        carousel = True
    ),
]

month = inquirer.prompt(monthList)

mon = month.get('option')

dayList = [
    inquirer.List(
        'option', 
        message = 'What is your day of birth', 
        choices = list(range(1,32)),
        carousel = True
    ),
]

day = inquirer.prompt(dayList)

day = str(day.get('option'))

day = day.rjust(2, '0')

date = str(f'{year}-{mon}-{day}')

parsedDate = datetime.strptime(f'{date}', '%Y-%b-%d').date()

url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={parsedDate}&end_date={parsedDate}'

headers = {
    'api_key': nasaKey
}

results = requests.get(url, headers)

print(results.text)