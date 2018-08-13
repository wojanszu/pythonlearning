print('Kamień...')
print('Papier...')
print('Nożyce...')

gracz1 = input('Gracz pierwszy, Twój ruch! ')
print('*** BEZ PODGLĄDANIA *** \n\n' * 20 )
gracz2 = input('Gracz drugi, Twój ruch! ')

if gracz1 == gracz2:
	print('REMIS')
if gracz1 == 'kamień':
	if gracz2 =='nożyce':
		print('Gracz pierwszy wygrywa!')
	elif gracz2 == 'papier':
		print('Gracz drugi wygrywa')
elif gracz1 =='papier':
	if gracz2 == 'kamień':
		print('Gracz pierwszy wygrywa!')
	elif gracz2 == 'nożyce':
		print('Gracz drugi wygrywa')
elif gracz1 =='nożyce':
	if gracz2 == 'papier':
		print('Gracz pierwszy wygrywa!')
	elif gracz2 == 'papier':
		print('Gracz drugi wygrywa')
else:
	print('No... coś nie wyszło, ziomek')