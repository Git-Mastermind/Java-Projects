import requests
import json
import time
def random_user_information():
    random_user = requests.get('https://randomuser.me/api/')
    data = random_user.json()
    json.dumps(data, indent=2)
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

# random_user_information()

def random_joke():
    random_joke = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = random_joke.json()
    json.dumps(data, indent=2)
    joke = data['setup']
    punchline = data['punchline']
    print(f'{joke}')
    time.sleep(3)
    print(f'{punchline}')    

# random_joke()

def motivational_quote_getter():
    random_quote = requests.get('https://zenquotes.io/api/random')
    data = random_quote.json()
    quote = data[0]['q']
    by_who = data[0]['a']
    print(f'{quote} - {by_who}')


# motivational_quote_getter()