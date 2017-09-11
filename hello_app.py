import os
import pdb

from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
	#Use url_for to reference app routes indirectly
	return url_for('show_user_profile',username='Richard') #example username Richard

@app.route('/login',methods=['GET'])
	#restrict login page to GET methods
def login():
	#Generate simple login form
	if request.values:
		return 'username is ' + request.values["username"] #return results once data has been submitted
	else:
		return'<form method="get" action="/login"><input type="text" name="username"/><p><button type="submit">Submit</button></form>'

@app_route('user/<username>')
def show_user_profile(username):
	#show the user profile for a given user - taken from entered URL
	return "User %s" username

@app.route('/post/<int:post_id>') 
def show_post(post_id):
	#show the post with the given id; the id must be an integer
	return "Post %s" post_id

@app.route('/hello')
def hello_world():
	#Display hello world
	#pdb.set_trace() #Python debugger step-through
	return 'Hello World!'

if __name__ == '__main__':
	#GetEnv variables used as docker container does not do well with Flask defaults
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.debug = true #Poll Flask source file for changes & descriptive error pages
	app.run(host=host,port=port)