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

def post_blog_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title':"Eshan's Coding Blog",
        'body':'I coded today, and it felt magical!',
        'userId':13
    }

    post = requests.post(url, json=data)

    if post.status_code == 201:
        print('✅Everything went well!')
    else:
        print('❌Something went wrong!')
# post_blog_data()

def topic_related_jokes():
    url_categories = {
        'general':'https://official-joke-api.appspot.com/jokes/general/random',
        'programming':'https://official-joke-api.appspot.com/jokes/programming/random',
        'knock-knock':'https://official-joke-api.appspot.com/jokes/knock-knock/random'
    }
    type_of_joke = input('Enter the type of joke (general, programming or knock-knock): ').lower()
    if type_of_joke == 'general':
        data = requests.get(url_categories['general']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)

    elif type_of_joke == 'programming':
        data = requests.get(url_categories['programming']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)
    
    elif type_of_joke == 'knock-knock' or type_of_joke == 'knock knock':
        data = requests.get(url_categories['knock-knock']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)


# topic_related_jokes()

def topic_related_jokes_cleanedup():
    url_categories = {
        'general':'https://official-joke-api.appspot.com/jokes/general/random',
        'programming':'https://official-joke-api.appspot.com/jokes/programming/random',
        'knock-knock':'https://official-joke-api.appspot.com/jokes/knock-knock/random'
    }
    type_of_joke = input('Enter the type of joke (general, programming, or knock-knock): ').lower()
    if ty
    if type_of_joke == 'knock knock':
        type_of_joke = 'knock-knock'
    if type_of_joke in url_categories:
        data = requests.get(url_categories[type_of_joke]).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)
# topic_related_jokes_cleanedup()