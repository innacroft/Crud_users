import random
lista_de_numeros= list(range(100))
pares =[numero for numero in lista_de_numeros if numero % 2 == 0 ]
print(pares)

student_uid=[1,2,3]
students=['Natalia','Luis','Juan']

students_and_uid={uid: student for uid, student in zip(student_uid,students)}

print(students_and_uid)

random_numbers=[]
for i in range(10):
    random_numbers.append( random.randint(1,3))

print(random_numbers)
non_repeated={number for number in random_numbers}
print(non_repeated)