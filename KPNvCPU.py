#Behold! My first AI!

import random

print('Kamień...')
print('Papier...')
print('Nożyce...')

gracz1 = input('Gracz pierwszy, Twój ruch! ')
rand_num = random.randint(0,2)
if rand_num == 0:
	CPU = 'kamień'
elif rand_num ==1:
	CPU ='kamień'
elif rand_num == 2:
	CPU = 'nożyce'
print(f'Komputer wybiera {CPU}')

if gracz1 == CPU:
	print('REMIS')
if gracz1 == 'kamień':
	if CPU =='nożyce':
		print('Gracz pierwszy wygrywa!')
	elif CPU == 'papier':
		print('Komputer wygrywa')
elif gracz1 =='papier':
	if CPU == 'kamień':
		print('Gracz pierwszy wygrywa!')
	elif CPU == 'nożyce':
		print('Komputer wygrywa')
elif gracz1 =='nożyce':
	if CPU == 'papier':
		print('Gracz pierwszy wygrywa!')
	elif CPU == 'papier':
		print('Komputer wygrywa')
else:
	print('No... coś nie wyszło, ziomek')