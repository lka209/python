from math import radians, sin, cos, tan
angulo = float(input('digite o angulo:'))
seno = sin(radians(angulo))
print(f'o angulo de {angulo} tem o seno de {seno:.2F}')
coseno = cos(radians(angulo))
print(f'o angulo de {angulo} tem o coseno de {coseno:.2F}')
tangente = tan(radians(angulo))
print(f'o angulo de {angulo} tem o tangente de {tangente:.2F}')
