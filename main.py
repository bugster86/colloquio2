#!/usr/bin/python
# coding=utf-8
# Autore: Martino Vigano'
# Versione: 1.0
# Aggiornamenti

for numero in range(1,301):
	if  numero%5 ==0 and numero%3 ==0:
		print ("Martino Viganò")
	elif numero%5==0:
		print ("Martino")
	elif numero%3==0:
		print ("Viganò")
	else:
		print(numero)

print( ":D" )
