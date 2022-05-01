from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import db, Post
from config import DB_URI

app = Flask(__name__)

app.config["MONGODB_HOST"] = DB_URI

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://127.0.0.1:8080',"allow_headers": "Access-Control-Allow-Origin"}})

db.init_app(app)

# post = Post(post_id = 4, votes = 0)
# post.save()

# current_post = Post.objects.get(post_id=2)
# print(current_post)
# current_votes = current_post.votes
# print(current_votes)

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


@app.route('/score/', methods=['GET', 'POST'])
def score():
    print(request.args)
    if request.method == "POST":
        # print("POST REQUEST")
        try:
            data = request.get_json()
            postId = int(data.get('post_id'))
            vote = int(data.get('val'))
            post = list(Post.objects(post_id = postId))
            
            if len(post) > 0:
                post = post[0]
                post.votes = post.votes + vote
                post.save()
            else:
                abort(400)
            
            responseObject = {'status':'success'}
            responseObject['score'] = str(post.votes)
            return jsonify(responseObject)
        except:
            abort(400, "Error")



    elif request.method == "GET":
        postId = request.args.get('post_id')
        print(postId)
        
        post = list(Post.objects(post_id = int(postId)))
        if len(post) > 0:
            post = post[0]
            currentVotes = post.votes
            response = jsonify(score = currentVotes)
            return response
        else:
            abort(400)
        
    
    # response.headers.add("Access-Control-Allow-Origin", "*")

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 5001)