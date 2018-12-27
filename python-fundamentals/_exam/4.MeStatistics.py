class Movie:
    def __init__(self, name, views, likes):
        self.Name = name
        self.Views = views
        self.Likes = likes

    def dislike(self):
        self.Likes = self.Likes - 1

    def like(self):
        self.Likes = self.Likes + 1

    def update_views(self, views):
        self.Views = self.Views + views

    def print_self(self):
        print(f"{str(self.Name)} - {str(self.Views)} views - {str(self.Likes)} likes")


movies = {}


line = input()

while line != "stats time":
    tokens_movies = [x for x in line.split('-')]

    if len(tokens_movies) == 1:
        tokens_likes = [x for x in line.split(':')]
        if tokens_likes[0] == "like":
            name_inp = tokens_likes[1]
            movies[name_inp].like()
        if tokens_likes[0] == "dislike":
            name_inp = tokens_likes[1]
            movies[name_inp].dislike()
    else:
        views_inp = int(tokens_movies[1])
        name_inp = tokens_movies[0]
        likes_inp = int(0)
        if name_inp not in movies:
            movies[name_inp] = Movie(name_inp, views_inp, likes_inp)
        else:
            movies[name_inp].update_views(views_inp)

    line = input()
else:
    command = input()
    if command == "by views":
        sorted_dict = sorted(movies.values(), key=lambda x: -x.Views)
        for row in sorted_dict:
            row.print_self()
    elif command == "by likes":
        sorted_dict = sorted(movies.values(), key=lambda x: -x.Likes)
        for row in sorted_dict:
            row.print_self()

