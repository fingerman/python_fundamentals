
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








