#python/conversao.py

def converte_int() :
	print('Informe um valor inteiro: ')
	valor_string = raw_input();
	valor = int(valor_string)
	print('Valor convertido: %s' % (valor))
	return valor
	
def converte_float() :
	print('Informe um valor float: ')
	valor_string = raw_input();
	valor = float(valor_string)
	print('Valor convertido: %s' % (valor))
	return valor