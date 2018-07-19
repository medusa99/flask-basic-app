from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Method used: %s" % request.method

@app.route('/apple', methods=['Get', 'Post'])
def apple():
    if request.method == 'Post':
        return "You are using POST"
    else:
        return "Your are probably using GET"
    
if  __name__ =="__main__":
    app.run()
