'''
Problem 4. Books
Input / Constraints
You are asked to write a program for a bookstore. Your task is to create a software, which tells the sellers if there is a requested book in stock or not. If there is you should sell it and at the end of the workday the software should list all sold books and the sum of their prices.
A valid book has:
•	Title -> string
•	Author -> string
•	Chapters -> list of strings
•	Price -> with positive floating point number or integer
First you start receiving strings of books – the bookstore's stock, which you should store the book if it's valid until you receive the command 'on work'.
Then you will start receiving requests for books. If the bookstore has that book in stock, you should list it as a sold book, if there is no such book you should print -> "No such book here"
When you receive the command 'end work' you should print all sold books and after that the amount of money.
A valid book will always be in format:
"{title} {author} {price} -> {chapter1}, {chapter2}, {chapter3} ..."
A requests for a book always will be in format: "{title}"
Output
The output should be printed on the console.
For every sold book you should print the information in the following format:
•	"SOLD: {title of the sold book} with author {author of the sold book}. Chapters in the book {the sum of the chapters of the sold book}"
At the end of the program you should print the sum formatted to second digit after decimal:
•	"Money: {sum of all sold books prices}"
If there aren't any sold books print
•	"Bad day :("

Constraints:
No books with same name and different authors will come as input

Examples
Input	Output	Comments
richDadPoorDad RobertKiyosaki 7.00 -> beRich, thinkDifferent, eDucateYourself, startThinking
richWoman kimKiyosaki 12.00 -> launchWithMyGirls, myStory, goAndDo
on work
richDadPoor
richDadPoorDad
richWomen
richWoman
end work

No such book here
No such book here
SOLD: richDadPoorDad with author RobertKiyosaki. Chapters in the book 4
SOLD: richWoman with author kimKiyosaki. Chapters in the book 3
Money: 19.00

First book is valid, so we add it to the store.
Second book is also valid, so we add it to the store

richDadPoor is not  in the store, so  we print “no such book here”
richDadPoorDad (7.00) is in the store and we sell it
richWomen is not  in the store, so  we print “no such book here”
richWoman (12.00) is in the store and we sell it
The amount is 12+7 = 19

---------------------------------------
killAmockingBird  20.50 -> chapter1
on work
richDadPoor
killAmockingBird
killAmockingBirds
richWomen
end work

No such book here
No such book here
No such book here
No such book here
Bad day :(




'''
class Book:
    def __init__(self, title, author, chapters, price):
        self.title = title
        self.author = author
        self.chapters = int(chapters)
        self.price = price
        self.info = f'SOLD: {self.title} with author {self.author}. Chapters in the book {self.chapters}'


books_list = []
books_buy = []


line = input()
while line != "on work":
    tokens = [x for x in line.split(' -> ')]
    author_data = list(tokens[0].split())
    num_chapters = len(list(tokens[1].split()))
    if len(author_data) > 2:
        title = author_data[0]
        author = author_data[1]
        chapters = num_chapters
        price = author_data[2]
        books_list.append(Book(title, author, chapters, float(price)))
    else:
        pass
    line = input()
line = input()

while line != "end work":
    books_buy += [line]

    line = input()

book_compare = []
for book_stored in books_list:
    book_compare.append(book_stored.title)

for book in books_buy:
    if book not in book_compare:
        print("No such book here")


book_prices = []
for book_stored in books_list:
    for book in books_buy:
        if book_stored.title == book:
            print(book_stored.info)
            book_prices.append(book_stored.price)
            sum_price = sum(book_prices)
if len(book_prices) == 0:
    print("Bad day :(")
else:
    print(f'Money: {sum_price:.2f}')








