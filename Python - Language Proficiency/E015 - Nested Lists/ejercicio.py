# >>> Nested Lists
# >>> https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    alumnos = []
    for i in range(5): #int(input())):
        name = students[i][0] #input()
        score = students[i][1] #float(input())
        alumnos.append([name, score])
    listaAlumnos = sorted([x[0] for x in alumnos if x[1] == sorted(set([x[1] for x in alumnos]))[1]])
    for alumno in listaAlumnos:
        print(alumno)