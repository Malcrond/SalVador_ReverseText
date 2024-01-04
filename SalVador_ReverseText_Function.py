while True:
	tex = input(str("Enter a word: "))
	reves = tex[::-1]
	if tex.isdigit():
		print('ERROR DETECTED, INPUT TEXT ONLY')
	elif any(char.isdigit() for char in tex):
		print('NUMBERS ARE NOT ACCEPTED')
	else:
		print(f'YOUR INPUT BACKWARDS IS: {reves}')
		break
