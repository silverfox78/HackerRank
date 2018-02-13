# >>> Finding the percentage
# >>> https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = 3 #int(input())
    student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    query_name = '' #input()

    #// CARGA DE PRUEBA
    n = 3
    student_marks['Krishna']  = [67, 68, 69]
    student_marks['Arjun']  = [70, 98, 63]
    student_marks['Malika']  = [52, 56, 60]
    query_name = 'Malika'

    print("{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name])))
