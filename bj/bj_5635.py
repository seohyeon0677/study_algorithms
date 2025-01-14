n = int(input())
students = []
for _ in range(n):
    data = input().split()
    name = data[0]
    d, m, y = map(int, data[1:])
    students.append((name, d, m, y))

students.sort(key=lambda x: (x[3], x[2], x[1]))

print(students[-1][0])
print(students[0][0])
