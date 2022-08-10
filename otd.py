from datetime  import datetime
import key_file
import inquirer
import requests

nasaKey = key_file.MY_NASA_API_KEY
headers = {
    'api_key': nasaKey
}

print('What is your year of birth?')
year = int(input())

if year < 1900:
    print("Records aren't available this far back.")
    exit()

monthList = [
    inquirer.List(
        'option', 
        message = 'What is your month of birth?', 
        choices = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        carousel = True
    ),
]

month = (inquirer.prompt(monthList)).get('option')

dayList = [
    inquirer.List(
        'option', 
        message = 'What is your day of birth?', 
        choices = list(range(1,32)),
        carousel = True
    ),
]

day = (str((inquirer.prompt(dayList)).get('option'))).rjust(2, '0')

date = str(f'{year}-{month}-{day}')

#validate entered date by returning true if returns value, a Feb 30 won't return any value and thus exit
try:
    dateTest = bool(datetime.strptime(f'{date}', '%Y-%b-%d').date())
except ValueError:
    dateTest = False
    print("Date entered isn't valid.")
    exit()

parsedDate = datetime.strptime(f'{date}', '%Y-%b-%d').date()

url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={parsedDate}&end_date={parsedDate}'

results = (requests.get(url, headers)).json()

miss_distance_data = []

for i in range(0, len(results['near_earth_objects'][f'{parsedDate}'])):
	miss_distance_data.append(results['near_earth_objects'][f'{parsedDate}'][i]['close_approach_data'][0]['miss_distance']['kilometers'])

distance = min(miss_distance_data)

print(f'You were {distance}km away from a near earth object!')