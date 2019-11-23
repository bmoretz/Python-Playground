from flask import *
from basicdb import *
import time
import uuid
import hash

app = Flask(__name__)

DATABASE = 'toots.json'
PASSWORDS = 'passwords.txt'

load_db(DATABASE)

passwords = {}
with open(PASSWORDS) as f:
    for line in f.read().splitlines():
        fields = line.split(':')
        passwords[fields[0]] = fields[1]

@app.route('/get-toots')
def get_toots():

    user = request.form['userid']

    if user is not None:
        toots = where(db_from('toots'), 'userid', user)

        if len(toots) == 0:
            abort(404)
    else:
        toots = db_from('toots')

    toots = list(reversed(orderby(toots, 'time')))[:5]
    return json.dumps(toots)

@app.route('/post-toot', methods=['POST'])
def post_toot():
    toot = {'userid': 'default',
            'time': str(time.time()), 
            'text': request.form['text']}
    insert('toots', toot)
    return 'Toot posted'

@app.route('/get-toots-by-user')
def get_toots_by_user():
    user = request.form['userid']
    user_toots = where(db_from('toots'), 'userid', user)
    toots = list(reversed(orderby(user_toots,'time')))
    return json.dumps(toots)

app.run(host='0.0.0.0', port=3000)