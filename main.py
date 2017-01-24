import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.
        delete_form = """
        <form action="/delete" method="post">
            <label>
                I want to delete
                <select type="text" name="watched-movie">
                    <option value="Spotlight">Spotlight</option>
                    <option value="The Big Short">The Big Short</option>
                    <option value="Bridge of Spies">Bridge of Spies</option>
                    <option value="Brooklyn">Brooklyn</option>
                    <option value="The Martian">The Martian</option>
                    <option value="The Revenant">The Revenant</option>
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="Remove It"/>
        </form>
        """


        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)


        content = page_header + edit_header + add_form + delete_form + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming into '/delete'
        e.g. flicklist.com/delete
    """

    def post(self):
        # look inside the request to figure out what the user typed
        watched_movie = self.request.get("watched-movie")

        # build response content
        watched_movie_element = "<strike>" + watched_movie + "</strike>"
        sentence = watched_movie_element + " has been removed from your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/delete', CrossOffMovie)
], debug=True)
