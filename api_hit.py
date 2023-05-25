def sendLoginRequest(User, Pass):
    api_url = 'http://localhost:5000/api/users/authenticate'
    data = {
        'username': User,
        'password': Pass
    }
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result = response.json()
        authenticated = result.get('authenticated')
        if authenticated:
            print('Authentication successful!')
        else:
            print('Authentication failed!')
    else:
        print('Failed to connect to the API endpoint.')
        
# Here while also development we can check our code for testability,
# we already know at this specific endpoint we pass 2 paremeters,
# so we can make a simple program that generates random strings (2 of each)
# and go hit this api for testability and check if it can handle the pressure
        
def generate_random_string(length):
    # Generate a random string of specified length
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
    
def testOurAPI():
    for x in 1000:
        username = generate_random_string(10)
        password = generate_random_string(10)
        sendLoginRequest(username, password)