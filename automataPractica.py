from lista_ligada import LSL
import itertools as it;

archivo = open("C:/Files/UdeA/Teoría de Lenguajes/Practica1/automataV.txt")

errores = []
typevar = -1
contador = 0
af_pr = {
    'S': {'b': 'B', 'l': 'L', 'i': 'I', 'c': 'C', 'd': 'D', 'f': 'F1'},
    'B': {'o': 'O1', 'l': 'L'},
    'O1': {'o': 'O2', 'n': 'N1', 'r': 'RE', 'u': 'U'},
    'L': {'o': 'O1', 'e': 'E1E2'},
    'O2': {'l': 'L'},
    'U': {'b': 'B'},
    'N1': {'t': 'T', 'g': 'G'},
    'R': {},
    'E1E2': {'a': 'AE'},
    'T': {},
    'G': {},
    'N2': {},
    'I': {'n': 'N1', 'f': 'F2'},
    'C': {'h': 'H'},
    'F1': {'o': 'O1'},
    'F2': {},
    'H': {'a': 'AE'},
    'D': {'o': 'O1'},
    'E': {},
    'AE': {'n': 'N2E', 'r': 'RE'},
    'N2E': {},
    'RE': {},
}
af_pr_acc = {'R', 'E1E2', 'T', 'G', 'N2', 'F2', 'N2E', 'RE'}

af_sep = {
    'SE0': {',': 'SE1', ';': 'SE1'},
    'SE1': {}
}
af_sep_acc = {'SE1'}

af_op = {
    'OP0': {'+': 'OP1', '-': 'OP2', '=': 'OP3', '!': 'OP5', '<': 'OP6', '>': 'OP7', '&': 'OP8', '^': 'OP9',
            '|': 'OP10',
            '~': 'OP11', '/': 'OP3', '%': 'OP3'},
    'OP1': {'+': 'OP14', '=': 'OP14'},
    'OP2': {'-': 'OP14', '=': 'OP14'},
    'OP3': {'=': 'OP14'},
    'OP5': {'=': 'OP14'},
    'OP6': {'=': 'OP14', '<': 'OP3'},
    'OP7': {'=': 'OP14', '>': 'OP16'},
    'OP8': {'=': 'OP14', '&': 'OP14'},
    'OP9': {'=': 'OP14', '^': 'OP14'},
    'OP10': {'=': 'OP14', '|': 'OP14'},
    'OP11': {},
    'OP14': {},
    'OP16': {'=': 'OP14', '>': 'OP3'},
}
af_op_acc = {'OP1', 'OP2', 'OP3', 'OP6', 'OP7', 'OP8', 'OP9', 'OP10', 'OP11', 'OP14', 'OP16'}

af_bool = {
    'BO0': {'t': 'BO1', 'f': 'BO5'},
    'BO1': {'r': 'BO2'},
    'BO2': {'u': 'BO3'},
    'BO3': {'e': 'BO4'},
    'BO4': {},
    'BO5': {'a': 'BO6'},
    'BO6': {'l': 'BO7'},
    'BO7': {'s': 'BO4'}
}
af_bool_acc = {'BO4'}


def variableEscrita(palabra, flag):
    estado = 'S';

    if len(palabra) == 1:
        estado = "¬"
        return estado

    palabra = palabra.rstrip()

    for i in range(len(palabra)):
        if estado == 'S':
            if palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = 'A'
            elif palabra[i] == " ":
                estado = 'S'
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'S'
            elif palabra[i] == ";":
                estado = "ERROR12"
            else:
                estado = 'ERROR1'
                return estado

        elif estado == 'A':
            if palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = 'A'
            elif palabra[i].isdigit():
                estado = 'A'
            elif palabra[i] == " ":
                estado = 'B'
            elif palabra[i] == ",":
                estado = 'C'
            elif palabra[i] == "=":
                estado = 'D'
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = 'P'
            elif palabra[i] == ";" and flag == 0:
                estado = 'ERROR4'
            elif palabra[i] == ";":
                estado = '¬'
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'A'
            else:
                estado = 'ERROR2'
                return estado

        elif estado == "B":
            if palabra[i] == " ":
                estado = "B"
            elif palabra[i] == ",":
                estado = 'C'
            elif palabra[i] == "=":
                estado = 'D'
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = 'P'
            elif palabra[i] == ";" and flag == 0:
                estado = "ERROR4"
            elif palabra[i] == ";":
                estado = '¬'
            elif palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "ERROR3"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'B'
            else:
                estado = "ERROR4"
                return estado

        elif estado == "C":
            if palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "A"
            elif palabra[i] == " ":
                estado = "C"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'C'
            else:
                estado = "ERROR2"
                return estado

        elif estado == "D":
            if palabra[i] == " ":
                estado = "D"
            elif palabra[i] == '"':
                estado = "E"
            elif palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "H"
            elif palabra[i].isdigit():
                estado = "J"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'D'
            elif palabra[i] == "'":
                estado = "R"
            else:
                estado = "ERROR4"
                return estado

        elif estado == "E":
            if palabra[i] == '"':
                estado = "F"
            else:
                estado = "E"


        elif estado == "F":
            if palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == ",":
                estado = "C"
            elif palabra[i] == " ":
                estado = "I"
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = "G"
            elif palabra[i] == "=" or palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "<" or palabra[i] == ">":
                estado = "O"
            elif palabra[i] == "&" or palabra[i] == "|":
                estado = "K"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'F'
            else:
                estado = "ERROR5"
                return estado

        elif estado == "G":
            if palabra[i] == ' ':
                estado = "G"
            elif palabra[i] == '"':
                estado = "E"
            elif palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "H"
            elif palabra[i].isdigit():
                estado = "J"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'G'
            elif palabra[i] == "'":
                estado = "R"
            else:
                estado = "ERROR6"
                return estado

        elif estado == "H":
            if palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "H"
            elif palabra[i].isdigit():
                estado = "H"
            elif palabra[i] == ' ':
                estado = "I"
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = "G"
            elif palabra[i] == ",":
                estado = "S"
            elif palabra[i] == "=":
                estado = "M"
            elif palabra[i] == "=" or palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "<" or palabra[i] == ">":
                estado = "O"
            elif palabra[i] == "&" or palabra[i] == "|":
                estado = "K"
            elif palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'H'
            else:
                estado = "ERROR7"
                return estado

        elif estado == "I":
            if palabra[i] == ' ':
                estado = "I"
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = "G"
            elif palabra[i] == ",":
                estado = "S"
            elif palabra[i] == "&" or palabra[i] == "|":
                estado = "K"
            elif palabra[i] == "=" or palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "<" or palabra[i] == ">":
                estado = "O"
            elif palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'I'
            else:
                estado = "ERROR2"
                return estado

        elif estado == "J":
            if palabra[i].isdigit():
                estado = "J"
            elif palabra[i] == ' ':
                estado = "I"
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = "G"
            elif palabra[i] == ",":
                estado = "S"
            elif palabra[i] == "=" or palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "<" or palabra[i] == ">":
                estado = "O"
            elif palabra[i] == "&" or palabra[i] == "|":
                estado = "K"
            elif palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'J'
            else:
                estado = "ERROR2"
                return estado

        elif estado == "K":
            if palabra[i] == palabra[i - 1]:
                estado = "L"
            elif palabra[i] == "=":
                estado = "D"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'K'
            else:
                estado = "ERROR8"
                return estado

        elif estado == "L":
            if palabra[i] == " ":
                estado = "D"
            elif palabra[i].isdigit():
                estado = "D"
            elif palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "D"
            elif palabra[i] == '"':
                estado = "E"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'L'
            elif palabra[i] == "'":
                estado = "R"
            else:
                estado = "ERROR4"
                return estado

        elif estado == "M":
            if palabra[i] == "=":
                estado = "D"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'M'
            else:
                estado = "ERROR9"
                return estado


        elif estado == "O":
            if palabra[i] == "=":
                estado = "D"
            elif palabra[i].isalpha() or palabra[i] == "_" or palabra[i] == "$":
                estado = "H"
            elif palabra[i].isdigit():
                estado = "J"
            elif palabra[i] == " ":
                estado = "D"
            elif palabra[i] == '"':
                estado = "E"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'O'
            else:
                estado = "ERROR4"
                return estado

        elif estado == "P":
            if palabra[i] == "=":
                estado = "D"
            elif palabra[i] == palabra[i - 1]:
                if palabra[i] == "+" or palabra[i] == "-":
                    estado = "Q"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'P'
            else:
                estado = "ERROR4"
                return estado

        elif estado == "Q":
            if palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == " ":
                estado = "Q"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'Q'
            else:
                estado = "ERROR10"
                return estado

        elif estado == "R":
            if palabra[i] == "'":
                estado = "U"
            else:
                estado = "T"

        elif estado == "T":
            if palabra[i] == "'":
                estado = "U"
            elif palabra[i] == ";":
                estado = "E"
                return estado
            else:
                estado = "ERROR11"
                return estado

        elif estado == "U":
            if palabra[i] == ";":
                estado = "¬"
            elif palabra[i] == ",":
                estado = "C"
            elif palabra[i] == " ":
                estado = "I"
            elif palabra[i] == "+" or palabra[i] == "-" or palabra[i] == "*" or palabra[i] == "/":
                estado = "G"
            elif palabra[i] == "=" or palabra[i] == "!":
                estado = "M"
            elif palabra[i] == "<" or palabra[i] == ">":
                estado = "O"
            elif palabra[i] == "&" or palabra[i] == "|":
                estado = "K"
            elif palabra[i] == "(" or palabra[i] == ")":
                estado = 'F'
            else:
                estado = "ERROR5"
                return estado

        elif estado == "¬":
            if palabra[i]:
                estado = "¬"
                return estado

    return estado


def accepts(transitions, initial, accepting, s):
    state = initial
    for c in s:
        state = transitions[state][c] if c in transitions[state].keys() else None
        if state is None:
            break
    return state in accepting


def accepts_id(s):
    state = 'ID0'
    accepting = {'ID1'}
    for c in s:
        transitions = {
            'ID0': {c.isalpha(): 'ID1', c == '$': 'ID1', c == '_': 'ID1'},
            'ID1': {c.isalpha(): 'ID1', c == '$': 'ID1', c == '_': 'ID1', c.isnumeric(): 'ID1'}
        }
        if True in transitions[state].keys():
            state = transitions[state][True]
        else:
            state = transitions[state][c] if c in transitions[state].keys() else None
            if state is None:
                break
        transitions.clear()
    return state in accepting


def check_type_variable():
    global tokenstuple
    if len(tokenstuple) > 1:
        state = 'TV1'
        for i in range(2):
            transitions = {
                'TV1': {
                    tokenstuple[i][0] == 'tipo' and tokenstuple[i][1] != 'if' and tokenstuple[i][1] != 'else': 'TV4',
                    tokenstuple[i][0] == 'variable': 'TV3',
                    tokenstuple[i][0] != 'tipo' and tokenstuple[i][0] != 'variable': 'TV3'},
                'TV2': {
                    tokenstuple[i][0] == 'tipo' and tokenstuple[i][1] != 'if' and tokenstuple[i][1] != 'else': 'TV2',
                    tokenstuple[i][0] == 'variable': 'TV2',
                    tokenstuple[i][0] != 'tipo' and tokenstuple[i][0] != 'variable': 'TV2'},
                'TV3': {
                    tokenstuple[i][0] == 'tipo' and tokenstuple[i][1] != 'if' and tokenstuple[i][1] != 'else': 'TV3',
                    tokenstuple[i][0] == 'variable': 'TV3',
                    tokenstuple[i][0] != 'tipo' and tokenstuple[i][0] != 'variable': 'TV3'},
                'TV4': {
                    tokenstuple[i][0] == 'tipo' and tokenstuple[i][1] != 'if' and tokenstuple[i][1] != 'else': 'TV1',
                    tokenstuple[i][0] == 'variable': 'TV2',
                    tokenstuple[i][0] != 'tipo' and tokenstuple[i][0] != 'variable': 'TV1'}
            }
            if True in transitions[state].keys():
                state = transitions[state][True]
            else:
                state = transitions[state][c] if c in transitions[state].keys() else None
                if state is None:
                    break
            transitions.clear()
        if state == 'TV2':
            return 1
        elif state == 'TV3':
            return 0
        else:
            return 0
    return -1


def accepts_const(s):
    state = 'C0'
    accepting = {'C2', 'C3', 'C7', 'C13', 'C14', 'C15'}
    for c in s:
        transitions = {
            'C0': {c.isnumeric(): 'C2', '.': 'C8', '+': 'C1', '-': 'C1', '"': 'C12', "'": 'C11'},
            'C1': {c.isnumeric(): 'C2', '.': 'C8'},
            'C2': {c.isnumeric(): 'C2', '.': 'C3'},
            'C3': {c.isnumeric(): 'C3'},
            'C6': {c.isnumeric(): 'C7'},
            'C7': {c.isnumeric(): 'C7'},
            'C8': {c.isnumeric(): 'C3'},
            'C11': {c.isnumeric(): 'C14', '.': 'C14', '+': 'C14', '-': 'C14', "'": 'C15', c.isalpha(): 'C14',
                    not c.isalnum() and c != "'": 'C14'},
            'C12': {c.isnumeric(): 'C12', '.': 'C12', '+': 'C12', '-': 'C12', '"': 'C13', c.isalpha(): 'C12',
                    not c.isalnum() and c != '"': 'C12'},
            'C13': {},
            'C14': {"'": 'C15'},
            'C15': {}
        }
        if True in transitions[state].keys():
            state = transitions[state][True]
        else:
            state = transitions[state][c] if c in transitions[state].keys() else None
            if state is None:
                break
        transitions.clear()
    return state in accepting


def add_token(wl):
    global tokenstuple
    global af_pr
    global af_op
    w = ''.join(wl)
    if accepts(af_pr, 'S', af_pr_acc, w):
        tokenstuple.append(('tipo', w))
    elif accepts(af_op, 'OP0', af_op_acc, w):
        tokenstuple.append(('operador', w))
    elif accepts(af_sep, 'SE0', af_sep_acc, w):
        tokenstuple.append(('separador', w))
    elif accepts(af_bool, 'BO0', af_bool_acc, w):
        tokenstuple.append(('boolean', w))
    elif accepts_const(w):
        tokenstuple.append(('constante', w))
    elif accepts_id(w):
        tokenstuple.append(('variable', w))


def token_to_LSL():
    global tokenstuple
    lsl = LSL()
    for i in tokenstuple:
        lsl.anadir_al_final(i[0], i[1])
    lsl_string = ""
    node = lsl.primero
    while node is not None:
        lsl_string += "["
        lsl_string += str(node.clase)
        lsl_string += ", "
        lsl_string += str(node.dato)
        lsl_string += "]"
        if node.liga is not None:
            lsl_string += " => "
        node = node.liga
    return lsl_string


def empty_list(lt):
    if lt:
        add_token(lt)
        lt.clear()



for linea in archivo:
    contadorfallos = 0
    contador = contador + 1
    symbols = {'+', '-', '~', '*', '/', '%', '<', '>', '=', '!', '&', '^'}
    tokenstuple = []
    l1 = []
    for c, nextc in it.zip_longest(linea, linea[1:], fillvalue=None):
        if c.isspace():
            empty_list(l1)
        elif c == ',' or c == ";":
            empty_list(l1)
            l1.append(c)
            add_token(l1)
            l1.clear()
        elif c in symbols:
            if len(l1) > 0 and l1[0] not in symbols:
                empty_list(l1)
            if nextc in symbols:
                l1.append(c)
            else:
                l1.append(c)
                add_token(l1)
                l1.clear()
        else:
            l1.append(c)
    if l1:
        add_token(l1)
    l1.clear()
    typevar = check_type_variable()
    if typevar == 1:
        linea = linea.split()
        linea1 = linea[1:]
        est = variableEscrita(''.join(str(x) for x in linea1), 1)
    elif typevar == 0:
        est = variableEscrita(linea, 0)
    if est == "ERROR1":
        fallo = "Linea " + str(contador) + ":El nombre de la variable empieza con un carácter invalido"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR2":
        fallo = "Linea " + str(contador) + ":Uso de signos prohibidos en el nombramiento de la variable"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR3":
        fallo = "Linea " + str(contador) + ":Uso de espacios en el nombramiento de la variable"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR4":
        fallo = "Linea " + str(contador) + ":Uso de signos prohibidos"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "E":
        fallo = "Linea " + str(contador) + ":Comillas sin cerrar"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR5":
        fallo = "Linea " + str(contador) + ":Uso de signos prohibidos despues del cierre de comillas"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR6":
        fallo = "Linea " + str(contador) + ":Uso de signos prohibidos despues de un operador aritmetico"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR7":
        fallo = "Linea " + str(contador) + ":Uso indebido de comillas"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR8":
        fallo = "Linea " + str(contador) + ":Uso de signos que no son el respectivo operador logico"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR9":
        fallo = "Linea " + str(contador) + ":Uso de signos que no son el respecto '=' "
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR10":
        fallo = "Linea " + str(
            contador) + ":Signos invalidos despues de los operadores de incremento o decremento '++' / '--' "
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR11":
        fallo = "Linea " + str(contador) + ":Cantidad de caracteres mayor de la permitida"
        errores.append(fallo)
        contadorfallos += 1
    elif est == "ERROR12":
        fallo = "Linea " + str(contador) + ":Linea vacia"
        errores.append(fallo)
        contadorfallos += 1
    elif est != "¬":
        fallo = "Linea " + str(contador) + ":Falta el operador de cierre ';'"
        errores.append(fallo)
        contadorfallos += 1
    if(contadorfallos == 0):
        print(token_to_LSL())
    tokenstuple.clear()
    contadorfallos = 0

for i in range(len(errores)):
    print(errores[i])
