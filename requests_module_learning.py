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

def check_github_stats():
    username = input('Enter your github username: ')
    url_repo = f'https://api.github.com/users/{username}/repos'
    url_info = f'https://api.github.com/users/{username}'
    repos = requests.get(url_repo)
    info = requests.get(url_info)
    if repos.status_code == 200 and info.status_code == 200:

        repo_data = repos.json()
        info_data = info.json()
        repo_name = repo_data[0]['name']
        profile_link = repo_data[0]['url']
        name = info_data['name']
        following = info_data['following']
        followers = info_data['followers']
        print(f'💻 Username: {username}')
        print(f'🌐 Profile Link: {profile_link}')
        print(f'🧠 Repo: {repo_name}')
        print(f'👋 Name: {name}')
        print(f'🙏 Following: {following}')
        print(f'👈 Followers: {followers}')
        print('✅ Everything went smoothly!')
    else:
        print(f'❌ Something went wrong: {info.status_code}')


# check_github_stats()

def check_name():
    username = input('Enter username: ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"✅The user's name is {data['name']}"
    else:
        return f"❌Something went wrong: {response.status_code}"


# print(check_name())

def country_facts_lookup():
    country = input('Enter a country: ')
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        common_name = data[0]['name']['common']
        official_name = data[0]['name']['official']
        capital = data[0]['capital'][0]
        region = data[0]['region']
        population = data[0]['population']
        currencies = data[0]['currencies']
        currency_code = list(currencies.keys())[0]
        languages = data[0]['languages']
        language = list(languages.values())
        flag = data[0]['flag']
        print(f'🌍 Country: {common_name}')
        print(f'🤝 Official Name: {official_name}')
        print(f'🏛️ Capital: {capital}')
        print(f'🌐 Region: {region}')
        print(f'🧑‍🤝‍🧑 Population: {population}')
        print(f'💰 Currency: {currency_code}')
        print(f'🗣️ Language: {language}')
        print(f'🚩 Flag: {flag}')
        print('✅ Everything went smoothly!')
    else:
        print(f'❌ Something went wrong: {response.status_code}')


# country_facts_lookup()
    

