# -*- coding: utf8


from collections import Counter # RECOMENDADO!


def conta_um_arquivo(fpath):
    
    contador = Counter()
    # Abre o arquivo
    with open(fpath) as input_file:
        # Lê linha por linha
        for line in input_file:
            # Remove o \n de cada linha
            line = line.lower().strip()
            if line:
                # Quebra uma linha em palavras
                palavras = line.split()
                
                for p in palavras:
                    contador[p] += 1
        # Seu código para processar um arquivo
        # Apague o pass
        # Retorne um dicionário {palavra: contagem}
    return dict(contador)   



def reduz(contagens_1, contagens_2):
    
    # Apague o pass
    # Seu código aqui
    # Soma as contagens de dois dicionários
    return Counter( contagens_1 ) + Counter( contagens_2 )



print( "\n\n" )

print("Teste Função conta_um_arquivo\n")

resultado1 = conta_um_arquivo( './entrada1.txt' )
print( resultado1 )

print( "\n\n" )

resultado2 = conta_um_arquivo( './entrada2.txt' )
print( resultado2 )

print( "\n\n" )

print("Teste Função reduz\n")

r = reduz( resultado1, resultado2 )
print( r )


print( "\n\n" )
