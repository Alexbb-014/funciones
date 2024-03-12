import os 
def fnt_LimpiarPantalla():
    os.system('cls')
    print('sistema de control de inventario')
    print('Autor: alexxx bb')
    print('universidad catolica luis amigó')
    print('\n\n')
    
def fnt_menu(repetir):
    while repetir == True:
        fnt_LimpiarPantalla()
        opcionStr = input('<<<<< menu de opciones>>>>>\n1. sumar\n2. restar\n3.multiplicar\n4. dividir\n---->')
        if opcionStr == 'F' or opcionStr == 'f':
                print('finalizando el programa........')
                repetir = False
        elif int(opcionStr) >= 1 and int(opcionStr) <= 4:
            numero1Flt = float(input('ingrese el primer numero'))
            numero2Flt =float(input('ingrese el segundo numero'))
            fnt_operaciones(numero1Flt,numero2Flt,opcionStr)
        else:
            print('\nopcion incorrecta')
            enter = input('\n<enter>')   
            if opcionStr == 'F' or opcionStr == 'f':
                repetir = False
        
def fnt_operaciones(n1, n2, op):
    if op == '1':
        resultadoFlt = n1 + n2
        operadorStr = '+'
    if op == '2':
        resultadoFlt = n1 - n2
        operadorStr = '-'
    if op == '3':
        resultadoFlt = n1 * n2
        operadorStr = '*'
    if op == '4':
        if n2 == 0:
            enter = input('\nno se puede dividir por 0 <enter>')
        else:
            resultadoFlt = n1 + n2
            operadorStr = '/'
            
    print('\n', n1, ' ', operadorStr, ' ', n2 ,' = ', resultadoFlt)
    enter = input('\n<enter>')

fnt_menu(True)
