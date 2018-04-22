# Library for working with JSON files
import json
# Library for network requests
import urllib.request
# A basic set of words
import vocabulary
# Library to convert text into speech
from gtts import gTTS
# Library for random
import random
# import SSLContext
import ssl


class Responder(object):
    key_index = ""
    previous_action = ""
    greetings = ["Glad to see you, ", "Glad you're here, ", "Long time no see, "]
    apologies = ["Oh sorry. Sometimes it seems difficult to find.", "I am afraid I can't understand you :(",
                 "Be more clear, please :("]
    intronews = ["Look what I've found for you!\n\n", "There's something interesting :)\n\n", "You should read it!\n"
                                                                    "\n", "How do you feel about it?\n\n"]
    motivations = ["Try to guess if you can :)", "I've prepared something difficult :)",
                   "I think you'll cope with it!", "It's no as easy as it seems :)"]
    congratulations = ["Yeah! You're right ;)", "You're so impeccable!", "Well done", "Great job!"]
    mistakes = ["Oh, try to be more attentive", "Look harder", "No, you're mistaken", "Come on, one more attempt!"]
    censor = ["fuck", "dick", "whore", "ass", "stupid", "idiot", "suck", "cock", "piss", "shit"]
    newsindex = 0

    def __init__(self):
        pass

    # searching for a meaning of a word
    def meaning(self, message, id):
        if message not in vocabulary.glossary:
            # make a request
            url = urllib.request.urlopen(
                "http://api.urbandictionary.com/v0/define?term={0}".format(message.replace(" ", "+")))
            # load data from JSON
            data = json.loads(url.read().decode())
            # is there's no data
            if data['list'] == []:
                answer = self.fail()
                hit = False
            else:
                # if there's data
                answer = data['list'][0]['definition']
                if not any(check in answer for check in self.censor):
                    hit = True
                    # also we are going to pronounce it
                    self.audio(message, id)
                else:
                    hit = False
                    answer = self.fail()
        else:
            answer = vocabulary.glossary[message]
            hit = True
        # if we found an answer
        if hit:
            # also we are going to pronounce it
            self.audio(message, id)
        return answer

    def greeting(self, name):
        return self.greetings[random.randint(0, 2)] + name

    def fail(self):
        return self.apologies[random.randint(0, 2)]

    def audio(self, text, id):
        tts = gTTS(text=text, lang="en")
        tts.save("%s.mp3" % id)

    def news(self):
        # make a request
        context = ssl._create_unverified_context()
        url = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?category=technology"
                                     "&country=us&apiKey=c108cc06ce3d4c1c9f59cf46c7990b10", context=context)
        # load data from JSON
        data = json.loads(url.read().decode())
        if self.newsindex < len(data['articles']):
            answer = "Title:\n{0}\n\nDescription:\n{1}\n\nLink:\n{2}".format(data['articles'][self.newsindex]['title'],
                                                                      data['articles'][self.newsindex]['description'],
                                                                      data['articles'][self.newsindex]['url'])
            offer = "\n\nIf you don't find it interesting, type /news one more time and I'll show you other articles :)"
            self.newsindex += 1
            self.previous_action = "news"
            return self.intronews[random.randint(0, 3)] + answer + offer
        else:
            self.newsindex = 0
            self.previous_action = ""
            return "It seems you've already reached the end"

    def news_image(self):
        # make a request
        context = ssl._create_unverified_context()
        url = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?category=technology"
                                     "&country=us&apiKey=c108cc06ce3d4c1c9f59cf46c7990b10", context=context)
        # load data from JSON
        data = json.loads(url.read().decode())
        if self.newsindex < len(data['articles']) and data['articles'][self.newsindex]['urlToImage'] is not None:
            return data['articles'][self.newsindex]['urlToImage']
        else:
            return "https://www.jetmag.com/wp-content/uploads/2015/02/crop1.jpg"

    def game(self):
        # setting a word
        key_word = list(vocabulary.glossary.keys())[random.randint(0, len(vocabulary.glossary))]
        # make a copy of the original vocabulary
        dict_copy = vocabulary.glossary.copy()
        # find the right meaning
        self.key_index = dict_copy[key_word]
        # creating a list that contains all 4 meanings
        meaning_list = []
        # add a meaning of the key word
        right_meaning = dict_copy[key_word]
        meaning_list.append(right_meaning)
        # delete it from dict to avoid repeats
        del dict_copy[key_word]
        for i in range(0, 3):
            print(str(len(dict_copy)))
            # calculating a random word
            rand_word = list(dict_copy.keys())[random.randint(0, len(dict_copy))]
            # find a meaning of this word
            meaning_list.append(dict_copy[rand_word])
            # deleting this word from the dict
            del dict_copy[rand_word]
        # shuffling our list
        random.shuffle(meaning_list)
        # find our key index
        self.key_index = meaning_list.index(right_meaning)
        # creating an answering message
        answer = self.motivations[random.randint(0, 3)] + "\n\n" + 'What does "{0}" mean?'.format(key_word) + "\n\n"
        for i in range(0, 4):
            answer += "{0}. {1} \n\n".format(str(i + 1), meaning_list[i])
        self.previous_action = "game"
        return answer

    def game_result(self, text):
        # if a user has written a number
        try:
            number = int(text) - 1
            if number == self.key_index:
                answer = self.congratulations[random.randint(0, 3)] + " To play once more, type /play"
                self.previous_action = ""
            else:
                answer = self.mistakes[random.randint(0, 3)]
            return answer
        # if something else
        except ValueError:
            self.previous_action = ""
            answer = "Oh, I see you don't wanna play, so next time"
            return answer

    def start(self, name):
        answer = "Hello, {0}! Glad to see you use me. I am CoolDev, I wanna be your friend :) Is there anything I " \
                "can help you with? For your information, I can play, find words and news you need. Just type /help" \
                " if you need some help ;)".format(name)
        return answer

    def help(self):
        answer = "1) I can find meanings for a number of words and sets of words you wish of geek's culture." \
                 " All you need is to just type this word or phrase and I'll find out what it means and how it is " \
                 "spelled :) \n" \
                 "2) I can search for the latest and interesting news. To see them, type a message " \
                 "/news \n" \
                 "3) I can also play with you, type /play and I'll give you a puzzle ;) \n"
        return answer

    def about(self):
        answer = "Porgrammer: Еливанов Алексей\nStickers' designer: Ульяна Казакова\nNews API: https://newsapi.org/\n" \
                 "Created for Проспект Свободный 2018 Conference\nAll Rights Reserved\nKransoyarsk, 2018"
        return answer
