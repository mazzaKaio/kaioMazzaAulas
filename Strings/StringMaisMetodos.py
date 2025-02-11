# TRANSFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA
nome = "kaio"
print(nome.capitalize(), "\n")

# TRANSFORMA TODAS AS LETRAS EM MINUSCULA
nome = "KAIO"
print(nome.casefold(), "\n")

# CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING
nome = "kaiomazza@gmail.com"
print(nome.count('a'), "\n")

# RETORNA 'True' OU 'False' PARA UM TESTE se A STRING TERINA COM UMA STRING ESPECIFICA
print(nome.endswith("gmail.com"), "\n")

# ENCONTRA A POSIÇÃO DO TERMO PROCURADO. LEMBRE-SE QUE COMEÇA DO 'zero'
print(nome.find('@'), "\n")

# VERIFICA SE O TEXTO É todo FEITO COM LETRAS
nome = "Kaio"
print(nome.isalpha(), "\n")

# VERIFICA SE O TEXTO É todo FEITO COM NUMEROS
nome = "007"
print(nome.isnumeric(), "\n")

# SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO
nome = "Kaio"
print(nome.replace("K", "C"), "\n")

# SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO
nome = "Kaio & Anny"
print(nome.split("&"), "\n")

# COLOCAR TODAS AS LETRAS INICIAS EM maiscucula
nome = "kaio gomes do nascimento mazza"
print(nome.title(), "\n")

# RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO espaços QUE NAO AGRAVAM VALOR
nome = "      kaio mazza     "
print(nome.strip(), "\n")

# RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO
nome = "kaio 2009"
print(nome.startswith("kai"), "\n")
print(nome.startswith("Kai"), "\n")