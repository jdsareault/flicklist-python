import webapp2
import random

movielist = ["Spotlight","The Big Short","Bridge of Spies",
    "The Martian","The Imitation Game","The Wolf of Wall Street",
    "Captain Phillips", "Moneyball"]

def getRandomMovie():
    if(len(movielist)>0):
        moviepick = random.choice(movielist)
        movielist.remove(moviepick)
    else:
        moviepick = "Sorry, no more movies"
    return moviepick

'''class Movie():
    def __init__(self):
        self.todaymovie = '''

class Index(webapp2.RequestHandler):

    todaymovie = getRandomMovie()
    tomorrowmovie = getRandomMovie()


    def get(self):
#        todaymovie = self.getRandomMovie()
#        tomorrowmovie = self.getRandomMovie()

        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + Index.todaymovie + "</p>"

        content += "<h2>Movie of Tomorrow</h2>"
        content += "<p>" + Index.tomorrowmovie + "</p>"

        self.response.write(content)

        Index.todaymovie = Index.tomorrowmovie
        Index.tomorrowmovie = getRandomMovie()

#        self.todaymovie = self.tomorrowmovie

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
