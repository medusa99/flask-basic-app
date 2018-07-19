from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage."

#/profile/tiff
@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username

#/post/23
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

if __name__ =="__main__":
    app.run()
