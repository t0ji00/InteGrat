from sympy import integrate, init_printing, diff
import numpy as np
from sympy.abc import *
import os
import requests, sys, signal
init_printing(use_latex="mathjax")

#Ctrl+C
def sig_handler(sig, frame):
         print("\n\n[!] Saliendo... \n")
         sys.exit(1)
signal.signal(signal.SIGINT, sig_handler)

def eRRor():
    os.system("cls")
    print("[!] Ingrese un numero de las opciones dadas!\n")
    print("[!] Utiliza Ctrl+C para salir... \n")
    input("[!] Toque Enter para continuar... \n\n")

    # Integrar_Funcion
def Integrar_Funcion():
    try:
        print("  _       _        _____           _ ")                
        print(" (_)     | |      / ____|         | |")               
        print("  _ _ __ | |_ ___| |  __ _ __ __ _| |_   _ __  _   _ ")
        print(" | | '_ \| __/ _ \ | |_ | '__/ _` | __| | '_ \| | | |")
        print(" | | | | | ||  __/ |__| | | | (_| | |_ _| |_) | |_| |")
        print(" |_|_| |_|\__\___|\_____|_|  \__,_|\__(_) .__/ \__, |")
        print("                                        | |     __/ |")
        print("                                        |_|    |___/ ")

        print("[*]Ejemplo de sintaxis")
        print("[*] 3*x+2**3")
        print("[*] Donde '**' representa un numero elevado")
        i = input("[*]ingresa tu funcion a integrar\n\n[#] ")
        result = (integrate(i))
        os.system("cls")
        print("El resultado es: " + str(result)+"\n")
        print("[!] Utiliza Ctrl+C para salir... \n")
        input("[!] Toque Enter para continuar... \n\n")
        os.system("cls")
    except Exception as e:
        os.system("cls")
        print("\n[!] Ingrese una funcion valida\n\n")
        print("[!] Utiliza Ctrl+C para salir...\n")
        input("[!] Toque Enter para continuar... \n")
            

# Derivar_Funcion  
def Derivar_Funcion():
    try:
        print("  _       _        _____           _ ")                
        print(" (_)     | |      / ____|         | |")               
        print("  _ _ __ | |_ ___| |  __ _ __ __ _| |_   _ __  _   _ ")
        print(" | | '_ \| __/ _ \ | |_ | '__/ _` | __| | '_ \| | | |")
        print(" | | | | | ||  __/ |__| | | | (_| | |_ _| |_) | |_| |")
        print(" |_|_| |_|\__\___|\_____|_|  \__,_|\__(_) .__/ \__, |")
        print("                                        | |     __/ |")
        print("                                        |_|    |___/ ")
        print("[*]Ejemplo de sintaxis")
        print("[*] 3*x+2**3")
        print("[*] Donde '**' representa un numero elevado")
        d = input("[*]ingresa tu funcion a integrar\n\n[#] ")
        result = diff(d)
        os.system("cls")
        print("[#] El resultado es: " + str(result)+"\n")
        print("[!] Utiliza Ctrl+C para salir...\n")
        input("[!] Toque Enter para continuar... \n")
        os.system("cls")
    except Exception as e:
        os.system("cls")
        print("\n[!] Ingrese una funcion valida\n\n")
        print("[!] Utiliza Ctrl+C para salir...\n")
        input("[!] Toque Enter para continuar... \n")

print("  _       _        _____           _ ")                
print(" (_)     | |      / ____|         | |")               
print("  _ _ __ | |_ ___| |  __ _ __ __ _| |_   _ __  _   _ ")
print(" | | '_ \| __/ _ \ | |_ | '__/ _` | __| | '_ \| | | |")
print(" | | | | | ||  __/ |__| | | | (_| | |_ _| |_) | |_| |")
print(" |_|_| |_|\__\___|\_____|_|  \__,_|\__(_) .__/ \__, |")
print("                                        | |     __/ |")
print("                                        |_|    |___/ ")
print("[*] Welcome to the inteGrat.py\n")
print("1 - Integrar\n")
print("2 - Derivar\n")
answer = input("Elige una Opcion\n\n [#] ")

if answer == "1":
    Integrar_Funcion()
elif answer == "2":
    Derivar_Funcion()
else:
    eRRor()
