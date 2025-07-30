import requests
import json
def random_user_information():
    random_user = requests.get('https://randomuser.me/api/')
    data = random_user.json()
    print(json.dumps(data, indent=2))
    user = data['results'][0]
    first_name = user['name']['first']
    last_name = user['name']['last']
    country = user['location']['country']
    email = user['email']
    phone = user['phone']

    print(f'🤵Name: {first_name} {last_name}')
    print(f'🚩Country: {country}')
    print(f'📩Email: {email}')
    print(f'📱Phone: {phone}')

