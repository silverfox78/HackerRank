# >>> Day 4 Class vs. Instance
# >>> 

class Person:
    def __init__(self,initialAge):
        self.edad = initialAge
        if self.edad < 0:
            print('Age is not valid, setting age to 0.')
            self.edad = 0
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.edad < 13:
            print('You are young.')
        else:
            if self.edad >= 13 and self.edad < 18:
                print('You are a teenager.')
            else:
                print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.edad += 1
        # Increment the age of the person in here      

t = 4 #int(input())
edades = [-1, 10, 16, 18]
for i in range(0, t):
    age = edades[i] #int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")