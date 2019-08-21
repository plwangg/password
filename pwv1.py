password = 'a123456'
i = 0
while i < 3:
	userpw = input('pls enter password')
	if password == userpw :
		print('login success')
		break
	else :
		i = i + 1
		print('login fail , pls retry again')
		print('remain',3-i,'times')

