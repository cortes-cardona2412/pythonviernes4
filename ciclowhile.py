guardian=100

#ciclo while
print("***Menu***")
print("1.Saludar")
print("2.Despedir")
print("0.Salir")
while(guardian!=0):
    guardian=int(input("Digita una opcion"))
    if(guardian==1):
        print("hola")
    elif(guardian==2):
        print("chao")
    elif(guardian==0):
        break
    else:
        print("Digite una opcion valida")       
else:    
    print("termine")