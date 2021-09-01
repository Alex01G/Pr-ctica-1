print("Seleccione una opción")
print("1. Cobrar boleto")
print("2. Salir")

venTotAdul = 0
venTotNiñ = 0

listaNum = [1,2]
op = int(input())
if op in listaNum:
    while op != 2:
        print("Bienvenido. \n Los boletos de niño tienen un costo de 45.00, y los de adultos 70.00")

        totAdul = 0
        totNiñ = 0

        bolAdulCom = int(input("¿Cuántos boletos de adulto comprará? "))
        bolNiñCom = int(input("¿Cuántos voletos de niño comprará? "))

        bolAdul = 70
        bolNiñ = 45

        venTotAdul += bolAdulCom
        venTotNiñ += bolNiñCom

        totAdul = bolAdul*bolAdulCom

        totNiñ = bolNiñ*bolNiñCom
        total = totAdul + totNiñ

        print("El costo total es de: ",total)
        print("¿Con qué denominación pagará? \n OPCIONES:")

        listaDen = [5,10,20,50,100,200,500]
        print(listaDen)

        while total >= 0:
            pago = 0
            print("Ingrese una unidad de las denominaciones anteriores: ")
            pago = int(input())
            if pago in listaDen:
                total -= pago
            else: 
                print("Valor no válido, inténtelo de nuevo.")
            if total > 0:
                print("Debe: ",total)

        quin = 0
        dos = 0
        cien = 0
        cin = 0
        vein = 0
        diez = 0
        cinc = 0
        cero = 0

        if total < 0:
            total = -(total)
            print("Su cambio es de: ", total)
            if (total/500) >= 1:
                while (total/500) >= 1:
                    total -= 500
                    quin += 1
            if (total/200) >= 1:
                while (total/200) >= 1:
                    total -= 200
                    dos += 1
            if (total/100) >=1:
                while (total/100) >= 1:
                    total -= 100
                    cien += 1
            if (total/50) >= 1:
                while (total/50) >= 1:
                    total -= 50
                    cin += 1
            if (total/20) >= 1:
                while (total/20) >= 1:
                    total -= 20
                    vein += 1
            if (total/10) >= 1:
                while (total/10) >= 1:
                    total -= 10
                    diez += 1
            if (total/5) >= 1:
                while (total/5) >= 1:
                    total -= 5
                    cinc += 1

        print("Le regresamos: \n",cero+quin,"de 500, ",cero+dos,"de 200, ",cero+cien,"de 100, ",cero+cin,"de 50, ",cero+vein,"de 20, ",cero+diez,"de 10, y ",cero+cinc,"de 5")
        print("Disfrute su película.")

        print("¿Desea comprar más entradas?")
        print("1. Sí")
        print("2. No")
        listaNumSec = [1,2]
        op = int(input())
        while op not in listaNumSec:
            print("Inténtalo de nuevo.")
            op = int(input())
else:
    print("Opción no válida, inténtelo de nuevo.")

op2 = 0

while op2 != 4: 
    print("1. Ventas totales")
    print("2. Boletos vendidos para niños")
    print("3. Boletos vendidos para adultos")
    print("4. Cerrar definitivamente")

    listaNumTer = [1,2,3,4]

    op2 = int(input())
    while op2 not in listaNumTer:
        print("Inténtalo de nuevo.")
        op2 = int(input())
    if op2 == 1:
        print("Las ventas globales son: ",venTotAdul+venTotNiñ)
    if op2 == 2:
        print("Las ventas de boletos para niños fueron: ",venTotNiñ)
    if op2 == 3:
        print("LAs ventas de boletos para adultos fueron: ",venTotAdul)

print("Adiós.")