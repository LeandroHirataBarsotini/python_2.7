#python/arquivos
# -*- coding: UTF-8 -*-

def ler_arquivo():

	arquivo = open('perfis.csv', 'r')

	# le uma linha
	linha = arquivo.readline()
	print linha

	# le todas as linhas
	for linha in arquivo:
		print linha

	arquivo.close()

def escreve_arquivo():
	arquivo_novo = open('arquivo_novo.csv', 'a')
	print arquivo_novo.mode
	arquivo_novo.write('teste arquivo novo - append 2, 879, Receita Federal \n')
	arquivo_novo.close()
	
