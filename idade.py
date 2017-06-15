#python/idade.py

from datetime import date

def calcula_idade() :
	hoje = date.today()
	print('data atual: %s/%s/%s' % (hoje.day, hoje.month, hoje.year) )
	print('Informe o ano de nascimento: ')
	nascimento = int(raw_input())
	idade = hoje.year - nascimento
	print('Sua idade: %s' % idade )
	return idade