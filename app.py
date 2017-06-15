#python/app.py
# -*- coding: UTF-8 *-*

def cadastrar(nomes) :
	print 'Digite o nome: '
	nome = raw_input()
	nomes.append(nome)

def alterar(nomes) :

	posicao = 0

	print 'Qual nome vc gostaria de alterar?'
	nome = raw_input()

	if(nome in nomes) :
		posicao = nomes.index(nome)
		print 'Informe o novo nome:'
		nome = raw_input()
		nomes[posicao] = nome
	else :
		print 'Nome nao localizado'


def remover(nomes) :
	print 'Qual nome você gostaria de remover?'
	nome = raw_input()
	nomes.remove(nome)

def listar(nomes) :
	print 'Lista de nomes:'
	for nome in nomes :
		print nome

def procurar(nomes) :

	print 'Digite nome a procurar:'

	nome_a_procurar = raw_input()

	if (nome_a_procurar in nomes) :
		print 'Nome %s foi localizado na posicao %s' % (nome_a_procurar, nomes.index(nome_a_procurar))
	else :
		print 'Nome nao localizado'


def menu() :

	nomes = []
	escolha = ''

	while(escolha != '0') :

		print '1 - Cadastrar'
		print '2 - Listar'
		print '3 - Remover'
		print '4 - Alterar'
		print '5 - Procurar'
		print '0 - Sair'

		escolha = raw_input()
		if(escolha == '1') :
			cadastrar(nomes)

		if(escolha == '2') :
			listar(nomes)

		if(escolha == '3') :
			remover(nomes)

		if(escolha == '4') :
			alterar(nomes)

		if(escolha == '5') :
			procurar(nomes)

menu()
