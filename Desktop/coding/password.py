password = ('a123456')
time = 3
while time > 0:
	time = time - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		print('密碼錯誤！')
		if time > 0:
			print('還有',time,'次機會') 