from App.database import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column('word',db.String(150), unique=True)
    char_count = db.Column('char_count',db.Integer, nullable=False, unique=False)
    difficulty = db.Column('difficulty',db.String(20), nullable=False)

    def __init__(self, word, char_count, difficulty):
        self.word = word
        self.char_count = char_count
        self.difficulty = difficulty


    def toDict(self):
        return {
            'id': self.id,
            'word': self.word,
            'Number of Characters: ': self.char_count,
            'Word Difficulty: ': self.difficulty
        }