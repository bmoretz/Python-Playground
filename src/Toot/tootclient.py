import requests

BASE_URL= 'http://localhost'
PORT = ":3000"

GET_ENDPOINT = BASE_URL + PORT + '/get-toots'
POST_ENDPOINT = BASE_URL + PORT + '/post-toot'

logged_in = False
token = ''
username = ''
  
def login():
    global logged_in
    global token
    global username
    u = input('Enter username: ')
    p = input('Enter password: ')
    logged_in = True
    token = '1234567890'
    username = u

def print_toots(r):
    if r.ok:
        print('-----TOOTS-----')
        for toot in r.json():
            print(toot['userid'] + ' -> ' + toot['text'])
        print('---------------')
    else:
        print(r.text)
     
     
def get_toots():
    r = requests.get(GET_ENDPOINT)
    print_toots(r)
 
def get_toots_by_user():
    u = input('Enter user to get toots for: ')
    
    if len(u) == 0:
        print("Invalid user")
    
    r = requests.get(GET_ENDPOINT, data={'userid': u})
    
    print_toots(r)

def my_toots():
    if not logged_in:
        print('Not logged in')
        return

    r = requests.get(GET_ENDPOINT, data={'userid': username}, headers={'Token':token})

    print_toots(r)
 
def post_toot():
    if not logged_in:
        print('Not logged in')
        return
    t = input('Enter your toot: ')
    if len(t) > 280:
        print('Toot too long!')
        return
    r = requests.post(POST_ENDPOINT, data={'text': t}, headers={'Token':token})
    return

# Main body
print('Welcome to Tooter!')
while True:
    print('(0) quit')
    print('(1) login')
    print('(2) get toots')
    print('(3) get toots by user')
    print('(4) my toots')
    print('(5) post toot')
    i = input('Enter command : ')
    if i == '0':
        break
    elif i == '1':
        login()
    elif i == '2':
        get_toots()
    elif i == '3':
        get_toots_by_user()
    elif i == '4':
        my_toots()
    elif i == '5':
        post_toot()
    else:
        print('Illegal command. Please try again.')