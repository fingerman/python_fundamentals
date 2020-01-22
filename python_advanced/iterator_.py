class Iterable:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
# Aufgabe lies einen Satz ein.
# Baue einen Iterator, der jedes Wort einzeln ausgibt.
satz = "Dies ist ein Satz."

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence[:-1]
        self.index = 0
        self.words = self.sentence.split()
        self.last = sentence[-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.words):
            self.index = 0
            raise StopIteration
        elif self.index == len(self.words):
            self.index += 1
            return self.last
        else:
            self.index += 1
            return self.words[self.index-1]

my_sentence = Sentence(satz)

for word in my_sentence:
    print(word)
print('------------')
for word in my_sentence:
    print(word)
print('end')


# sentence2 = iter(my_sentence)

# print(next(sentence2))
# print(sentence2.__next__())


l = iter([1,2,3])

for element in l:
    print(element)
