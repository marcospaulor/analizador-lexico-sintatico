import os
import Scanner as sc
import Parser as ps

# This file is the main file. It is the one that calls the Scanner and the Parser.
# The Scanner is the lexical analyzer. It is the one that creates the tokens.
# The Parser is the syntactic analyzer. It is the one that uses the tokens to create the parse tree.

def main():
    #  Open file .java and read it
    file = open("test.java", "r")
    file = file.read()
    print (file)

    #  Create Scanner and Parser objects
    try:
    
        scanner = sc.Scanner(file)
        scanner.print_tokens()
        # parser = ps.Parser(file)
    except Exception as e:
        print(e)
        return

    print("Código analisado com sucesso!")

if __name__ == "__main__":
    main()
