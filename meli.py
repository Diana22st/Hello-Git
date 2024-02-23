palabra=input("Dame una palabra para dividirla: ")
longitud=len(palabra)
vocales=[]
consonantes=[]
for i in range(0,longitud):
    if palabra[i]=="a":
        vocales.append(palabra[i])
    elif palabra[i]=="e":
        vocales.append(palabra[i])
    elif palabra[i]=="i":
        vocales.append(palabra[i])
    elif palabra[i]=="o":
        vocales.append(palabra[i])
    elif palabra[i]=="u":
       vocales.append(palabra[i])
    else:
       consonantes.append(palabra[i])
print(vocales)
print(consonantes)

oh lala