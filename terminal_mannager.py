#!/bin/python3
#Creator: Patxa
import os, json, sys
from random import SystemRandom
from cryptography.fernet import Fernet

class Contrasena:
    key = None  # Class attribute to store the encryption key

    
    def Password(Longitud):
        Aleatoria = SystemRandom()
        Caracteres = 'abcdefghijklmnopqrstuvwxyz|@#~&%$+-_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        passWord = ''
        while Longitud > 0:
            passWord = passWord + Aleatoria.choice(Caracteres)
            Longitud = Longitud - 1
        return passWord

    
    def openFile(fileName):
        if os.path.isfile(fileName):
            with open(fileName, 'r') as archive:
                return json.load(archive)
        else:
            return {}

    
    def saveFile(fileName, data):
        with open(fileName, 'w') as archive:
            json.dump(data, archive, indent=4, separators=(',', ' : '))

    
    def generateKey(cls):
        if cls.key is None:
            keyname = '.key'
            if not os.path.isfile(keyname):
                cls.key = Fernet.generate_key()
                with open(keyname, 'wb') as f:
                    f.write(cls.key)
            else:
                with open(keyname, 'rb') as f:
                    cls.key = f.read()

    
    def cifrado(cls, filename):
        cls.generateKey()
        cipher_suite = Fernet(cls.key)
        with open(filename, 'r') as f:
            data = json.load(f)
        cipher_text = cipher_suite.encrypt(json.dumps(data).encode())
        with open(filename, 'wb') as f:
            f.write(cipher_text)

    
    def noCifrado(cls, filename):
        cls.generateKey()
        cipher_suite = Fernet(cls.key)
        with open(filename, 'rb') as f:
            cipher_text = f.read()
        plain_text = cipher_suite.decrypt(cipher_text).decode()
        return json.loads(plain_text)
        
def create():
    Longitud = 0
    fileName = 'Crack.json'

    while True:
        long = input('Nº de Carácteres: ')
        try:
            Longitud = int(long)
            break
        except:
            print(f'{long} no es un número.')

    while True:
        Pass = Contrasena.Password(Longitud)
        acepta = str(input(f'\n [si/no] Aceptas la contraseña: {Pass} '))
        if acepta.lower() == 'si':
            App = str(input('\n Para qué la necesitas:  '))
            user = str(input('\n Usuario/e-mail del sitio:   '))

            if not os.path.isfile(fileName):
                datos_existentes = {}
            else:
                datos_existentes = Contrasena.noCifrado(fileName)

            datos_existentes[App] = user + ' -> ' + Pass
            Contrasena.saveFile(fileName, datos_existentes)
            Contrasena.cifrado(fileName)
            break
        


def main():
    fileName = 'Crack.json'
    print('\nWELCOME TO MY PASSWORD GENERATOR...\n')
    print('\n 1 -> Generate a new password')
    print('\n 2 -> See your passwords')
    print('\n 3 -> Exit')
    chose = int(input('\nChoose an option: '))
    if chose == 1:
        create()
        main()
    elif chose == 2:
        try:
            print(Contrasena.noCifrado(fileName))  
        except:
            print('''\n -------------No hay datos para mostrar.------------\n''')
            main()  
    elif chose == 3:
        sys.exit(1)
    else:
        print('\n IT IS NOT AN OPTION, TRY AGAIN...')
        main()

main()