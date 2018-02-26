# >>> Day 13: Abstract Classes
# >>> https://www.hackerrank.com/challenges/30-abstract-classes/problem

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print('Title: {}\nAuthor: {}\nPrice: {}'.format(self.title, self.author, self.price))

title= 'The Alchemist' #input()
author= 'Paulo Coelho' #input()
price= 248 #int(input())
new_novel=MyBook(title,author,price)
new_novel.display()