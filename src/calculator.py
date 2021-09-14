# -*- coding: utf-8 -*-

r=2.2
s=False

while s==False:
	x=input("insira um numero: ")
	x=float(x)
	o=input("insira o operador: ")
	y=input("insira o outro numero: ")
	y=float(y)

	if o=="+":
		r=(x+y)

	elif o=="-":
		r=(x-y)

	elif o=="*":
		r=(x*y)

	elif o=="/":
		r=(x/y)

	if o!="/" and o!="*" and o!="-" and o!="+":
		print("Voce inseriu o operador de forma incorreta")
	else:
		print("resultado")
		print(r)

	c=input("deseja continuar? (s/n): ")

	if c=="n":
		s=True




