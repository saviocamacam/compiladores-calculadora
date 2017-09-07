# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# calclexer.py
# Analisador léxico para a linguagem Caleidoscópio
# Autores: Rodrigo Hübner e Jorge Luiz Franzon Rossi
#-------------------------------------------------------------------------

import ply.lex as lex

class Calclex():

    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self, optimize=False)

    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'


    #Regras de expressões regulares para tokens simples
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    #Expressão regular com código de ação
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # String contendo caracteres em branco
    t_ignore = ' \t'

    #Regra de manipulação de erros
    def t_error(self, t):
        print("Caracter ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

    #Método para chamadas sucessivas dos tokens
    def test(self, code):
        #Entrada para o lexer
        lex.input(code)
        while True:
            t = lex.token()
            if not t:
                break #Sem mais entradas
            print(t)

if __name__ == '__main__':
    from sys import argv
    calclexer = Calclex()
    f = open(argv[1])
    calclexer.test(f.read())

