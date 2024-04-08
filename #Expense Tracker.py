#Expense Tracker

print("1. Agregar Gastos")
print("2. Mostrar Gastos")
print("3. Mostrar Total")
print("4. Finalizar")

gastos =  {}

while True:
    try:
        a = int(input("Que deceas hacer?: "))
        
        if a == 1:
            descripción = input("Describir Gastos: ")

            while True:
                try:
                    costo = int(input("Costo: "))
                    break
                except:
                    print("Eso no es un numero")
            gastos[f"{descripción}"] = f"{costo}"

        elif a == 2:
            for descripción in gastos:
                print(f"Description: {descripción}, Cost: {gastos.get(descripción)}$")

        elif a == 3:
            total = 0
            for costos in gastos.values():
                total += int(costos)
            print(f"Total: {total}$")

            
        elif a== 4:    
            break

        else:
            print("Eso no es una opción")
    except:
        print("Eso no es una opción valida")

