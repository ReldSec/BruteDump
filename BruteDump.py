#!/usr/bin/env python
#_*_ coding: utf8 _*_

from os import path
import os
import sys
import hashlib
from datetime import datetime
import argparse
from colorama import Fore
import time

arg = argparse.ArgumentParser()
arg.add_argument("-t","--text",help="Password a crackear")
arg.add_argument("-w","--wordlist",help="Diccionario")
arg.add_argument("-n","--notify",help="Resaltar la palabra cuando se crackee")
arg.add_argument("-e","--encrypt",help="Tipo de cifrado del hash")
parser = arg.parse_args()

exec_hour = datetime.now()
exec_hour_style = exec_hour.strftime("%H:%m")

md5_long = 32
sha1_long = 40
sha224_long = 56
sha256_long = 64
sha384_long = 96
sha512_long = 128

def logo():
    print(Fore.LIGHTRED_EX + """
██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ ██╗   ██╗███╗   ███╗██████╗ 
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║████╗ ████║██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║  ██║██║   ██║██╔████╔██║██████╔╝
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║  ██║██║   ██║██║╚██╔╝██║██╔═══╝ 
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝                                                                             
        """)
    print(Fore.LIGHTWHITE_EX + "\t\t<== https://www.facebook.com/reldsec ==>")
def md5_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.md5(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))

def sha1_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.sha1(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))

def sha224_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.sha224(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))

def sha256_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.sha256(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))

def sha384_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.sha384(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))

def sha512_crack(find_dict_wordlist,parser_text):
    ext_fin = find_dict_wordlist.find('.')

    if ext_fin == -1:
        print("Diccionario Invalido!")
        exit()

    path_dictionary = path.exists(parser.wordlist)
    if path_dictionary is False:
        print("El diccionario no existe!")
        exit()

    dictionary = open(parser.wordlist,"r")
    print("Ejecucion => {}".format(exec_hour_style))
    print("Ruta de ejecucion => {}".format(path.realpath(sys.argv[0])))
    print("Crackeando... ;)")
    time.sleep(0.3)

    #Creamos una lista con los hashes
    list_attack = []
    for cracked_word in dictionary:
        ad = cracked_word.replace("\n","")
        list_attack.append(ad)
    
    list_attack_hash = []
    
    for i in range(0,len(list_attack)-1):
        add_list_hash = hashlib.sha512(list_attack[i])
        list_attack_hash.append(add_list_hash.hexdigest())

    for n in range(0,len(list_attack)-1):
        if list_attack_hash[n] == parser.text:
            print(Fore.LIGHTGREEN_EX + "\n\nCrackeado!: {} => {}\n\n".format(parser.text,list_attack[n]))
            raw_input()
            time.sleep(2)
            exit()
        print(Fore.LIGHTRED_EX + "Cracking Failed!: {} => {}".format(list_attack_hash[n],list_attack[n]))
def main():
    cmd = os.system("reset")
    if parser.encrypt:
        if parser.text:
            if parser.wordlist:
                find_dict_wordlist = parser.wordlist
                if parser.encrypt == "md5":
                    if len(parser.text) < md5_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    md5_crack(find_dict_wordlist,parser.text)
                elif parser.encrypt == "sha1":
                    if len(parser.text) < sha1_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    sha1_crack(find_dict_wordlist,parser.text)
                elif parser.encrypt == "sha224":
                    if len(parser.text) < sha224_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    sha224_crack(find_dict_wordlist,parser.text)
                elif parser.encrypt == "sha256":
                    if len(parser.text) < sha256_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    sha256_crack(find_dict_wordlist,parser.text)
                elif parser.encrypt == "sha384":
                    if len(parser.text) < sha384_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    sha384_crack(find_dict_wordlist,parser.text)
                elif parser.encrypt == "sha512":
                    if len(parser.text) < sha512_long:
                        print("Error de palabra")
                        exit()
                    logo()
                    print(Fore.LIGHTBLUE_EX + "Modo de ataque => {}".format(parser.encrypt))
                    sha512_crack(find_dict_wordlist,parser.text)
                else:
                    print(Fore.LIGHTRED_EX + "Encriptacion desconocida")
                    exit()
                
            else:
                print(Fore.LIGHTRED_EX + "No se especifico un diccionario!!")
        else:
            print(Fore.LIGHTRED_EX + "No hay una entrada de texto")

    else:
        print(Fore.LIGHTRED_EX + "No se especifico la encriptacion")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
