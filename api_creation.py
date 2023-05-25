@app.route('/api/users/authenticate', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    cursor = db_connection.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return jsonify({'authenticated': True})
    else:
        return jsonify({'authenticated': False})
        
# This top code can be hosted at GCP, Clouds, AWS, Azure, 
# and many other IAAS providers, we can create docker image or an 
# executable file/jar/service out of this and upload to the cloud and 
# deploy it whever the server is. Of course per our needs we can scale
# our product meaning we can make it sufficient for 5 users if thats' 
# what we are aiming for or we can make it for a huge corporate
# company 