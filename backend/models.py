from enum import unique
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Post(db.Document):
    post_id = db.IntField(required = True, unique = True)
    votes = db.IntField(required = True)

    def to_json(self):
        return {
            "post_id": self.post_id,
            "votes": self.votes
        }
