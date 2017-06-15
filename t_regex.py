
#python/t_regex

import re

def teste():
	print "Testes com regex"
	resultado = re.match('Py', 'Python')
	print type(resultado)
	print resultado.group()
	resultado = re.match('[pP]y', 'Python')
	print resultado.group()
	resultado = re.match('[a-zA-Z]y', 'Python ou ayo')
	print resultado.group()
	resultados = re.findall('[a-zA-Z]y[a-zA-Z]+', 'Python ou ayo ou xyz')
	print resultados
	resultados = re.findall('\wy\w+', 'Python ou ayo ou xyz ou popye')
	print resultados
	resultados = re.findall('\wy\w+\d', 'Python ou ayo ou xyz ou popye ou oye1  aya3 ey3')
	print resultados
	resultados = re.findall('[A-Za-z]+\d?', 'Python ou ayo ou xyz ou popye ou oye1  aya3 ey3')
	print resultados
	print "Testes com regex(raw string)"
	resultados = re.findall('[lL]\w+', 'Leandro Leonardo Lancelot Golon')
	print resultados
	resultados = re.findall(r'[lL]\w{4}', 'Leandro Leonardo Lancelot Golon')
	print resultados
	resultados = re.findall(r'[lL]\w{4,8}', 'Leandro Leonardo Lancelot Golon')
	print resultados
	resultado = re.match(r'^@', '@ comeca com arrouba')
	print resultado.group()
	resultado = re.match(r'.*|$', '| termina com pipe')
	print resultado.group()
	resultados = re.findall(r'([JP]\w+)', 'Java JavaScript Python')
	print resultados
	resultado = re.match(r'(.*/perfis/\d+)/convidar$', 'http://django.com/perfis/123/convidar')
	print resultado.group()
	print "FIM"
