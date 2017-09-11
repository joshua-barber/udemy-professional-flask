import os
import pdb

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	pdb.set_trace() #Python debugger step-through
	i = 3
	visited = i + 1
	return 'You have visited ' + str(visited) + ' times'

if __name__ == '__main__':
	#GetEnv variables used as docker container does not do well with Flask defaults
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.debug = true #Poll Flask source file for changes & descriptive error pages
	app.run(host=host,port=port)