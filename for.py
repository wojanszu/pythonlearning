
# Rozwiązanie w którym są trzy różne printy

# for n in range(1,21):
# 	if n ==4 or n == 13:
# 		print(f'{n} jest pechową liczbą')
# 	elif n % 2 == 0:
# 		print(f'{n} jest parzystą liczbą')
# 	else:
# 		print(f'{n} jest liczbą nieparzystą')


# Mała optymalizacja kodu. Zamiast 3 printów używamy jednego. Określamy "stan" liczby, by później ją sprintować

for n in range(1,21):
	if n ==4 or n == 13:
		stan = 'PECHOWĄ LICZBĄ'
	elif n % 2 == 0:
		stan = 'parzystą liczbą'
	else:
		stan = 'nieparzystą liczbą'
	print(f'{n} jest {stan}')