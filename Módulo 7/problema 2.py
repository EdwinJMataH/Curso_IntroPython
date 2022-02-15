nuevoPlaneta = ''
planetas = []

while nuevoPlaneta.lower() != 'done':
    if nuevoPlaneta:
        planetas.append(nuevoPlaneta)
    nuevoPlaneta = input('Introduce un planeta')


for planeta in planetas:
    print(planeta)