'''
MeTube Statistics
Let’s create a video platform such as YouTube. It will be called MeTube. Your task is to store videos, videos’ views and likes.
You will be receiving lines in the following format: "{videoName}-{views}" until you receive "stats time". You should store video and its views, if the video already exists add the views to it.
You can receive a command to rate a video in the following format: "like:{video}" or "dislike:{video}". The like command will give a single like whereas the dislike command will remove a like, but the given video needs to exist.
After receiving "stats time" you will receive an order criterion – either "by views" or "by likes". If you receive "by views" order the videos by views in descending order, otherwise order the videos by likes in descending order.
Print each of the videos in the following format:
"{video} - {views} views - {likes} likes"
Input
•	Until you receive " stats time " you will be receiving videos in the following format: "{video}-{views}".
•	You can receive a rate command -> "like {video}" or "dislike {video}".
•	After "stats time" you will receive either "by views" or "by likes".
Output
•	Print the statistics for each video in the following format:  "{video} - {views} views - {likes} likes"
Constraints
•	The views will be a valid integer in the range [1-1000].
•	The video's name will not contain dashes ('-') or colon (':').
•	Allowed working time / memory: 100ms / 16MB.
Examples
Input
Eninem Venom-500
like:Eninem Venom
Funny Cats-700
like:Funny Cats
like:Funny Cats
Eninem Venom-300
stats time
by likes
Output
Funny Cats - 700 views - 2 likes
Eninem Venom - 800 views - 1 likes
Eminem Ringer-300
Messi Top Goals-500


like:Eminem Ringer
like:Eminem Ringer
dislike:Eminem Ringer
stats time
by views
Output
Messi Top Goals - 500 views - 0 likes
Eminem Ringer - 300 views - 1 likes



'''




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

