planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

user_planeta = input('Por favor ingrese el nombre del planeta (con una letra mayúscula para comenzar)')

planeta_index = planetas.index(user_planeta)

print('Aquí están los planetas más cerca que ' + user_planeta)
print(planetas[0:planeta_index])

print('Aquí están los planetas más lejos que ' + user_planeta)
print(planetas[planeta_index + 1:])