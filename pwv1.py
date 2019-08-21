password = 'a123456'
i = 0
while i < 3:
	userpw = input('pls enter password')
	if password == userpw :
		print('login success')
		break
	else :
		i = i + 1
		if 3 - i > 0:
			print('login fail , pls retry again')
			print('remain', 3 - i, 'times')
		#elif 3 - i == 0:
			#print('login fail , no more chance')



