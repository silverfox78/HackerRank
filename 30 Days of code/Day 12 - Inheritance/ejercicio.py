# >>> Day 12: Inheritance
# >>> 

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        suma = sum(self.scores)
        largo = len(self.scores)
        if largo <= 0:
            return 'T'
        valor = suma / largo
        if valor >= 90:
            return 'O'
        if valor >= 80:
            return 'E'
        if valor >= 70:
            return 'A'
        if valor >= 55:
            return 'P'
        if valor >= 40:
            return 'D'
        return 'T'

line = ['Heraldo', 'Memelli', '8135627'] #input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = 2 #int(input()) # not needed for Python
scores = [100, 80] #list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())