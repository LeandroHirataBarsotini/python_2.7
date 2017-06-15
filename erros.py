# -*- coding: UTF-8 -*-

#erros.py

arquivo = None

try:

    arquivo = open('arquivo_imaginario.txt','r')
    print('vixi, ele existe')

except IOError as erro:
    print('Arquivo nao encontrado: %s' % erro)

finally:
    if(arquivo is not None):
        print('fechando arquivo')
        arquivo.close()