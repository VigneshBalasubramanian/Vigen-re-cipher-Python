# Name: Vignesh Balasubramanian
# Date: 03/02/2016
# Class: CS524-02
# Deciphers mesage based on the user's selected operation (Encode/Decode) based on Vignere cipher.

#Importing library files

import sys
import os.path

#Declaring variables

Character_Set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flag = 1

#Encoding string

def EncodeString(Code_Word, String):
    return DecipherString(Code_Word, String, 'Encode')

#Decoding string

def DecodeString(Code_Word, String):
    return DecipherString(Code_Word, String, 'Decode')

#Deciphering String based on the chosen operation

def DecipherString(Code_Word, String, mode):
    String_Deciphered = []

    Code_WordIndex = 0
    Code_Word = Code_Word.upper()

    #Deciphering each letter of the string

    for symbol in String:
        num = Character_Set.find(symbol.upper())
        #Case check to handle case sensitivity
        
        if num != -1:
            if mode == 'Encode':
                num += Character_Set.find(Code_Word[Code_WordIndex])
            elif mode == 'Decode':
                num -= Character_Set.find(Code_Word[Code_WordIndex])

            num %= len(Character_Set)
            
            if symbol.isupper():
                String_Deciphered.append(Character_Set[num])
            elif symbol.islower():
                String_Deciphered.append(Character_Set[num].lower())

            Code_WordIndex += 1
            if Code_WordIndex == len(Code_Word):
                Code_WordIndex = 0

        #If not found in the Character Set
        else:
            String_Deciphered.append(symbol)

    return ''.join(String_Deciphered)

def main():
    flag = 1;
    while flag == 1:        
            print("\nEncode -> 1/Decode -> 2/Quit -> 3")
            print("\nEnter operation you would like to go with:")
            Operation = raw_input("Operation: " )

            if Operation == '1':
                Code_Word = raw_input('Enter the code word: ')
                Filename = raw_input("File name: " )
                file_exists = os.path.exists(Filename)
                if file_exists == True:
                    invar = open(Filename, "r")
                    String = invar.read()
                    print("Input string from your file:")
                    print(String)
                    String_Deciphered = EncodeString(Code_Word, String)
                    outvar = open(Filename+"_e.out", "w")
                    outvar.write(String_Deciphered)
                    invar.close()
                    outvar.close()
                else:
                    print("File doesn't exist. Check the Filename.")
            elif Operation == '2':
                Code_Word = raw_input('Enter the code word: ')
                Filename = raw_input("File name: " )
                file_exists = os.path.exists(Filename)
                if file_exists == True:
                    invar = open(Filename, "r")
                    String = invar.read()
                    print("Input string from your file:")
                    print(String)
                    String_Deciphered = DecodeString(Code_Word, String)
                    outvar = open(Filename+"_d.out", "w")
                    outvar.write(String_Deciphered)
                    invar.close()
                    outvar.close()                    
                else:
                    print("File doesn't exist. Check the Filename.")
            elif Operation == '3':
                print('Program terminating..')
                sys.exit() 

            if file_exists == True:
                print('Deciphered String:')
                print(String_Deciphered)
 

if __name__ == '__main__':
    main()
