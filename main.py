student_scores = input("Escribe una serie de puntajes entre el numero (0) y (100), separados por un espacio.\n(Ejemplo: 78 65 89 86 55 91 64 89)\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)

max_score = 0
for  score  in student_scores:
  if score > max_score:
    max_score = score
# print(max_score)
print(f"\nLa puntuación más alta en la clase es: {max_score}")

min_score = 101
for score in student_scores:
  if score <= min_score:
    min_score = score
# print(min_score)
print(f"\nLa puntuación más baja en la clase es: {min_score}")