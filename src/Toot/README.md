Programming Assignment 6
================================

**Fundamentals of Modern Software**  
**Fall 2019**  
**Due 11:59 PM, October 23**

Introduction
------------

**REMINDERS**

1. **When you are done, be sure to submit your work.**
2. **You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.**
3. **Be sure to test your programs thoroughly. We will.**
4. **Your output should match the output in the samples as closely as possible.**

In this assignment you will extend the Tooter social networking platform from Lab 6. We have provided you with a slightly cleaned up version of the framework for the Tooter server (in `tootserver.py`) and a command-line client (in `tootclient.py`). The only working features right now are the two from Lab 6: retrieving a list of toots and posting a new toot.  We have upgraded the Lab 6 code in a few ways.

First, we have upgraded the database so that the `toots` table now contains three fields:

* `userid`: A string with the userid of the user who posted the toot.
* `time`: a string containing the time at which the toot was posted. Times are formatted as seconds and fractions of a second since January 1, 1970. You do not need to worry about the details. You can get the current time by importing the `time` package and calling `str(time.time())`. The nice thing about this time format is that it sorts cleanly.
* `text`: a string containing the body of the toot

Your job is to add support for multiple users.  This will require adding code for the following features:

* Log in
* Post a tweet _from the currently logged in user_
* Retrieve the 5 most recent toots by a specific user
* Retrieve the user's own 5 most recent toots

To so so, you will need to write _both_ the client-side code (using `requests`) and the server-side code (using `flask`), and you will need to test the client and server _simultaneously_ to make sure they are correctly talking to each other.


tootserver.py
--------
 
The Tooter server should expose the following endpoints:

**`POST /login`**

Logs in a user. The username and _unhashed_ password should be supplied in the _body_ of the request.

```
POST /login HTTP/1.1
...
userid:alice
pw:alicerocks
```

usernames and _hashed_ passwords are stored in `passwords.txt`. It follows the password format used for Assignment 2. To help you with the password hashing, we have provided you with `hash.py` from assignment 2.  We have also written code that loads the password file into a dictionary, `passwords`, where the usernames are the keys and the corresponding hashed passwords are the values.

If the username and password are valid and match, the request returns a `200 OK` status code and the body of the response contains a JSON data structure with a random session token.  You can generate a unique random token by importing the `uuid` module and then calling `uuid.uuid4().hex`.  This generates a 128-bit random number and prints it as a 32-digit hexadecimal number. On subsequent requests requiring authentication, this token is required.
```
HTTP/1.1 200 OK
...
{"result": "success", "token":"949566e6cd7c4dcd9565f7fbf3bc9b5d"}
```
If the username does not exist or the username and password do not match, the request returns a `401 Unauthorized` status code.

_This endpoint does not currently exist. You will need to write it from scratch._


**`GET /get-toots?userid=<username>`**

Returns the 5 most recent toots posted by user `username`.  If the username exists, the response has status code `200 OK` and the body contains a JSON data structure with the toots in reverse chronological order:
```
[{"userid": "alice", "time": "1538747379.7258956"", toot: "I can toot!"},
{"userid": "bob", "time": "1538747325.7155385", toot: "I can toot too!"},
{"userid": "alice", "time": "1538747233.6375887", toot: "I can toot again!"},
...
]
```
If no username is specified, the response has status code `200 OK` and returns the 5 most recent toots posted by any user. If a username is specified but does not exist, the response has status code `404 Not Found`.

_This endpoint currently exists, but it does not check the query string. Instead it currently returns the 5 most recent toots from any user. You will need to add the code to filter toots by user._


**`POST /post-toot`**

Posts a new toot. The _body_ of the request should consist of a JSON data struture containing the text of the new toot. In addition, this endpoint requires authorization, so the request headers must include a valid session token.

```
POST /post-toot HTTP/1.1
...
Token:949566e6cd7c4dcd9565f7fbf3bc9b5d

{"text": "This is my toot"}
```

If the token is one that the server has previously handed out during the current session, the toot is added to the database with the username of the appropriate user and the response has status code `200 OK`. If the token is invalid, the toot is not added and the response has status code `401 Unauthorized`.

_This endpoint currently exists but it does not check the `Token` header. Instead, it currently posts all toots as being by user `default`. You will need to validate the header and post toots from the appropriate user._



tootclient.py
--------

_The client currently has skeleton code for all of the required functions. `top_toots()` is fully implemented and you should not need to modify it.  `post_toot()` is partially implemented, but it does not currently set the `Token` header to authenticate the user. `login()`, `my_toots()` and `toots_by_user()` are stubs and you will need to implement them._




 
 
Notes 
-------

  * You can run the server in the usual way: `$ python tootserver.py`. You can run the client in the usual way: `$ python tootclient.py`. To run them both at once you will need to open a _second_ command-line tab in Codio. You can do so using the "Terminal" command from the "Tools" menu at the top of your Codio window. Start the server running in one tab, then start the client in the other tab.
  * The client makes its requests using HTTP (not HTTPS), to the hostname `localhost`, and on port number 3000. These are all required by Codio's security model. You should not need to modify any of this code.
  * You **do not** need to modify the database on disk.  Indeed, you **should not** write to the database by calling `save_db()`.  It is fine to make all changes in memory; the server can "forget" about new toots each time it is stopped and restarted.
  * We suggest that you start by extending the `get-toots` endpoint on the server to handle specific usernames, and add the appropriate code on the client in `toots_by_user()`.  Then extend the `post-toot` endpoint in the server so that it checks for a `Token` header and the `post_toot()` function in the client so that it sends one.  Start with a hard-coded token, then once it is working, implement the `login` endpoint on the server and the `login` function on the client to complete the authentication workflow.
  * The server will need to keep track of the tokens it has handed out and their associated usernames. (We suggest using a dictionary.)  As with the toots, you do not need to store this information on disk; when the server is stopped and restarted, this starts a new "session" and any users will need to log in again.
  *  Here are a few username/password pairs you can use to play around with:
```
augustus:augustus
caligula:d0g
vespasian:password
otho:0th0
decius:DECIUS
```


Here is a sample transcript from the client:
```
$ python tootclientSOLUTION.py 
Welcome to Tooter!
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 2
-----TOOTS-----
augustus -> Well, well, well. Look what the wolf dragged in.
pertinax -> @vespasian THREAD: you suck
vespasian -> THREAD: You probably think that a vomitorium is where Romans barfed up their meals. 1/
augustus -> Don't make me come over there and conquer a few provinces.
tiberius -> Not you too @titus
---------------
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 3
Which user? tiberius
-----TOOTS-----
tiberius -> Not you too @titus
tiberius -> @hadrian leave my mother out of this!
tiberius -> @augustus stop hogging the spotlight
---------------
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 4
Not logged in
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 5
Not logged in
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 1
Enter username: alice
Enter password: alicerocks
No such user
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 1
Enter username: augustus
Enter password: augustus
augustus logged in
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 4
-----TOOTS-----
augustus -> Well, well, well. Look what the wolf dragged in.
augustus -> Don't make me come over there and conquer a few provinces.
augustus -> Who's up for some gladiatorial contests!
augustus -> Guys. Seriously. Come on.
augustus -> Good. Let's have some fun!
---------------
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 5
Enter your toot: Whoo, I'm authenticated!
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 2
-----TOOTS-----
augustus -> Whoo, I'm authenticated!
augustus -> Well, well, well. Look what the wolf dragged in.
pertinax -> @vespasian THREAD: you suck
vespasian -> THREAD: You probably think that a vomitorium is where Romans barfed up their meals. 1/
augustus -> Don't make me come over there and conquer a few provinces.
---------------
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 4
-----TOOTS-----
augustus -> Whoo, I'm authenticated!
augustus -> Well, well, well. Look what the wolf dragged in.
augustus -> Don't make me come over there and conquer a few provinces.
augustus -> Who's up for some gladiatorial contests!
augustus -> Guys. Seriously. Come on.
---------------
(0) quit
(1) login
(2) top toots
(3) get toots by user
(4) my toots
(5) post toot
Enter command : 0
```

Here is the corresponding server log:
```
$ python tootserverSOLUTION.py 
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Oct/2019 15:20:54] "GET /get-toots HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:01] "GET /get-toots?userid=tiberius HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:21] "POST /login HTTP/1.1" 401 -
127.0.0.1 - - [17/Oct/2019 15:21:27] "POST /login HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:31] "GET /get-toots?userid=augustus HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:44] "GET /post-toot HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:46] "GET /get-toots HTTP/1.1" 200 -
127.0.0.1 - - [17/Oct/2019 15:21:49] "GET /get-toots?userid=augustus HTTP/1.1" 200 -
```


