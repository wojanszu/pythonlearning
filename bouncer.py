#ask for age
age = input ('How old are you?')
if age != '':
	# 18-21 wristbands
	if int(age) >= 18 and int(age) < 21:
			print ('You can enter but you need a wristband')
	# 21+ drink, normal entry
	elif int(age) >=21:
		print('You can enter, youre allowed to drink as well')
	else:
		print('YOu cannot enter,kid')
else:
	print('Enter age')