class Video:
    def __init__(self, trainer, course, hours, minutes, lecture):
        self.trainer = trainer
        self.course = course
        self.hours = hours
        self.minutes = minutes
        self.lecture = lecture
        self.duration = self.to_minutes()

    def to_minutes(self):
        return int(self.hours)*60 + int(self.minutes)


servers = []
videos_list = []

server_time_minutes = 10*60
counter_minutes_videos = 0

scrape_course_or_trainer = None
scrape_trainer_name_or_course_name = None

while True:
    data = input()
    lecture = None
    trainer = None
    duration = None
    course = None
    hours = None
    minutes = None

    if len(data.split(';')) == 1:
        servers.append(videos_list)
        scrape_course_or_trainer = data.split()[1]
        scrape_trainer_name_or_course_name = data.split()[2]
        break

    data_splited = data.split(';')
    for item in data_splited:
        if 'trainer' in item:
            trainer = item.split(":")[1]
        elif 'course' in item:
            course = item.split(":")[1]
        elif 'lecture' in item:
            lecture = item.split(":")[1]
        elif 'duration' in item:
            duration = item.split(":")[1]
            hours = duration.split('h')[0]
            minutes = duration.split('h')[1].replace("m", "")

    current_video = Video(trainer=trainer, lecture=lecture, course=course, hours=hours, minutes=minutes)
    counter_minutes_videos += current_video.duration

    if counter_minutes_videos <= server_time_minutes:
        videos_list.append(current_video)
    else:
        servers.append(videos_list)
        counter_minutes_videos = 0
        counter_minutes_videos += current_video.duration
        videos_list = []
        videos_list.append(current_video)

total_duration = 0

for i in range(0, len(servers)):
    for video in servers[i]:
        if scrape_course_or_trainer == 'course':
            if video.course == scrape_trainer_name_or_course_name:
                print(f"https://streamcdn{i+1}.softuni.bg/course={video.course}&lecture={video.lecture}&trainer={video.trainer}")
                total_duration += video.duration
        elif scrape_course_or_trainer == 'trainer':
            if video.trainer == scrape_trainer_name_or_course_name:
                print(f"https://streamcdn{i+1}.softuni.bg/course={video.course}&lecture={video.lecture}&trainer={video.trainer}")
                total_duration += video.duration

total_hours = total_duration//60
total_minutes = total_duration%60


print(f"total duration: {total_hours:02d}:{total_minutes:02d}:00")


'''
Problem 2. SoftUni Lecture CDN
In this exam problem’s universe, SoftUni decided to store its lectures’ recordings on its own servers. Also, in this universe your job application to SoftUni was accepted and as the new intern, you have been given the simple task of implementing a Content Delivery Network for the recordings. We’ll leave storing the actual video files to the backend engineers - your job here is to simply generate lecture links based on existing data. Since you’re a sneaky little hacker, you also want to scrape some of the links for “safe keeping”.
A sample lecture link looks like this:
•	https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
As you can see, every link begins with “https://streamcdn{n}.softuni.bg/”, where {n} is the stream server number. After that, it has parameters like the course, lecture and the trainer. A single server can only hold up to 10 hours of video, so keep that in mind when storing the videos.
Input / Constraints
The input data should be read from the console.
You will receive multiple lines in the format:
•	lecture:{name};trainer:{trainer};course:{course};duration:{hours}h{minutes}m
The tokens (lecture/trainer/course/duration) will be in random order, so you need to account for that fact when parsing them. The duration will always have hours and minutes, even if their values are 0.
When you parse the lecture info, you need to store it in the current server. As said above, each server can only hold 10 hours of video. If a video you’d store would overflow the maximum duration of 10 hours, put it on the next server (increment the server index by 1). Do not put videos in the previous server after an overflow occurs.
You will stop receiving lectures when you receive the command 
•	“scrape {course/trainer} {course_name/trainer_name}”,
The input data will always be in the format specified. There is no need to check it explicitly.
Output
Upon receiving the final line of the input, depending on what was specified (scrape course or scrape trainer), you need to look through the servers and find all lectures which have that course/trainer. Create links for them and print them on the console, separated by new lines, in order of insertion.
Finally, calculate the total duration of the lectures and print it in the following format:
•	“total duration: HH:MM:SS”
Make sure each token (hour/minute/second) has leading zeroes if it needs them.
 
Examples
Input
trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m
lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
duration:1h56m;trainer:housey;course:csharp-db;lecture:joins
trainer:viktor;duration:2h33m;course:js-fundamentals;lecture:dom
trainer:housey;course:python-fund;lecture:functional;duration:2h06m
lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
scrape course csharp-oop-basics
Output
https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=matrices-extra&trainer=bojo
https://streamcdn2.softuni.bg/course=csharp-oop-basics&lecture=matrices-extra&trainer=bojo
total duration: 12:15:00
Comments
The first (and only) server switch happens when we attempt to insert the “dom” lecture.

Input
trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m
lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
duration:1h56m;trainer:housey;course:csharp-db;lecture:joins
lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
lecture:matrices-extra-2;trainer:bojo;course:csharp-oop-basics;duration:2h20m
trainer:viktor;duration:2h33m;course:js-fundamentals;lecture:dom
trainer:housey;course:python-fund;lecture:functional;duration:2h06m
scrape trainer housey
Output
https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
https://streamcdn1.softuni.bg/course=csharp-db&lecture=joins&trainer=housey
https://streamcdn3.softuni.bg/course=python-fund&lecture=functional&trainer=housey
total duration: 07:07:00
Comments
The first server switch happens when we attempt to insert the “matrices-extra” lecture. The second – when we insert the “functional” lecture. 

Input
lecture:softuniada;course:marathons;duration:9h30m;trainer:nakov
lecture:softuniada2018;course:marathons;duration:10h00m;trainer:nakov
lecture:softuniada2033;course:marathons;duration:9h45m;trainer:nakov
scrape trainer nakov
Output
https://streamcdn1.softuni.bg/course=marathons&lecture=softuniada&trainer=nakov
https://streamcdn2.softuni.bg/course=marathons&lecture=softuniada2018&trainer=nakov
https://streamcdn3.softuni.bg/course=marathons&lecture=softuniada2033&trainer=nakov
total duration: 29:15:00
Comments
We insert the first lecture (which is 9h30m long) into the 1st server, then we insert the second lecture into the second server. Since the second server now has exactly 10 hours of video on it, we insert the third lecture into the third server.

'''