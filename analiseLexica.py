import re

def analiseLexica():
    f = open("calculadoraBasica.c", "r") #Abre o arquivo para leitura
    lines = f.readlines()

    tokens = {}
    qtdLines = 1

    for line in lines:
        line = re.sub("{", " {", line)
        line = re.sub(";", " ;", line)
        line = re.sub(",", " ,", line)
        line = re.sub("=", " = ", line)
        line = re.sub("[ ]{2,}", " ", line)
        if line.strip() != '':
            line = line.strip()

            if re.search("^#include <.*[.]h>$", line):
                line = line.split()
                tokens[line[0]] = "Palavra reservada"
                biblioteca = re.sub("(<|>)","", line[1])
                tokens[biblioteca] = "Biblioteca"
            elif re.search("^int main\\(\\)( {|)$", line):
                line = line.split()
                tokens[line[0]] = "Palavra reservada"
                tokens[line[1]] = "Palavra reservada"
                if len(line) == 3:
                    tokens[line[2]] = "Delimitador de início"
            elif line == "{":
                tokens[line] = "Delimitador de início"
            elif line == "}":
                tokens[line] = "Delimitador de fim"
            else:
                aux = line
                line = line.split()
                for i in line:
                    if i == "int" or i == "return":
                        tokens[i] = "Palavra reservada"
                    elif i == "=":
                        tokens[i] = "Comando de atribuição"
                    elif i == "+":
                        tokens[i] = "Operador de adição"
                    elif i == "*":
                        tokens[i] = "Operador de multiplicação"
                    elif i == ";":
                        tokens[i] = "Finalizador de linha"
                    elif re.search("^[a-zA-Z]{1,}[0-9]*$", i):
                        tokens[i] = "Nome de variável"
                    elif re.search("^[0-9]{1,}$", i):
                        tokens[i] = "Constante numérica"
                    elif i == ",":
                        tokens[i] = "Separador"
                    else:
                        if i == "#include":
                            i = aux
                        print("O token '" + i + "' na linha " + str(qtdLines) + " é inválido")
                        return
        qtdLines += 1 
    for key in tokens:
        print(key + " - " + tokens[key])
    

def main():
    analiseLexica()

main()