#!/usr/bin/python
# coding=utf-8
# Autore: Martino Vigano'
# Versione: 1.4
# Aggiornamenti
# 1.1 --> Esteso a 401 il ciclo
# 1.4 --> Esteso a 601 il ciclo

for numero in range(1,601):
	if  numero%5 ==0 and numero%3 ==0:
		print ("Martino Viganò")
	elif numero%5==0:
		print ("Martino")
	elif numero%3==0:
		print ("Viganò")
	else:
		print(numero)

print( ":D" )
