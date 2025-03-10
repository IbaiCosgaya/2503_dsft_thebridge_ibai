from tabulate import tabulate

tablero = []  

for x in range(10): 
    fila = ["."] * 10  
    tablero.append(fila)  

print(tabulate(tablero, tablefmt="fancy_grid"))

tablero[3][5] = "B"

print(tabulate(tablero, tablefmt="fancy_grid"))
