from App.database import db
from App.models import Word
import csv

# def get_all_words():

#     with open('/workspace/Brainstormin-Spelling-Bee/App/Words.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
         #print(reader)

    #     for row in reader:
    #         if row['word_w'] == '':
    #             row ['word_w'] == None
    #         if row['char_count_num'] == '':
    #             row ['char_count_num'] == None
    #         if row['difficulty_lvl'] == '':
    #             row ['difficulty_lvl'] == None

    #     Words = words(
    #          word = row ['word_w'],
    #          char_count = row ['char_count_num'],
    #          difficulty = row['difficulty_lvl']
    #      )
    # return words
    #     db.session.add(Words)
    # db.session.commit()

def print_all_words():
    with open('App/Words.csv','r') as csv_file:
        csv_read = csv.reader(csv_file)

        next(csv_read)
        wid = []
        wrd = []
        chars = []
        diff = []
        wordList = []

        for line in csv_read:
            wrd.append(line[0])
            chars.append(line[1])
            diff.append(line[2])

        for i in range(len(chars)):
            currWord = Word(word=wrd[i], char_count=chars[i], difficulty=diff[i])
            wordList.append(currWord.toDict())
            db.session.add(currWord)
        db.session.commit()
        return wordList
    
def get_all_words_json():
    words = Word.query.all()
    if not words:
        return []
    words = [word.toDict() for word in words]
    return words

def get_easy_words_json():
    easyWords = []
    easyWords = Word.query.filter_by(difficulty='easy')
    if not easyWords:
        return []
    easyWords = [word.toDict() for word in easyWords]
    return easyWords

def get_medium_words_json():
    mediumWords = []
    mediumWords = Word.query.filter_by(difficulty='medium')
    if not mediumWords:
        return []
    mediumWords = [word.toDict() for word in mediumWords]
    return mediumWords


def get_hard_words_json():
    hardWords = []
    hardWords = Word.query.filter_by(difficulty='hard')
    if not hardWords:
        return []
    hardWords = [word.toDict() for word in hardWords]
    return hardWords

def get_genius_words_json():
    geniusWords = []
    geniusWords = Word.query.filter_by(difficulty='genius')
    if not geniusWords:
        return []
    geniusWords = [word.toDict() for word in geniusWords]
    return geniusWords
   