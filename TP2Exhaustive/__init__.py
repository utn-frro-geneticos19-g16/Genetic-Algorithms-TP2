#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ENUNCIADO DEL TRABAJO PRÁCTICO N° 2

El Problema de la Mochila
Consiste en elegir, de entre un conjunto de N elementos (cada uno con un valor $i, y un volumen Vi),
aquellos que puedan ser cargados en una mochila de volumen V de manera que el valor obtenido sea máximo.

Ejercicio 1
Resolver el Problema de la Mochila utilizando una Búsqueda Exhaustiva

Ejercicio 2
Resolver el ejercicio anterior usando el algoritmo Greedy (Heurística) y comentar su similitud o no con el Exhaustivo.

Ejercicio 3
Plantear el Problema de la Mochila teniendo en cuenta los pesos en lugar del volumen, y luego:
    A)- Resolverlo con Exhaustivo
    B)- Resolverlo con Greedy (Heurística)


FECHA DE ENTREGA DEL TRABAJO PRÁCTICO: 30 de Abril de 2019

--> Genetic-Algorithm TP2 --- V1.0 ---  Created on 20 jun. 2019

            Antonelli, Nicolás - Recalde, Alejando - Rohn, Alex
"""

import random
from time import time
from itertools import combinations
# Main Function is located at the end


# Elements may be created randomly or with inputs
def generateElements(N, isRandom, maxVol, maxPrice):
    elements = [[0] * N for _ in range(3)]  # Every Element has 3 values: Position (0), Price Value (0) and Volume (1)
    if isRandom:
        for i in range(N):
            num = i+1
            p = round(random.uniform(0, maxPrice), 3)
            v = round(random.uniform(0, maxVol), 3)
            elements[0][i] = num
            elements[1][i] = p
            elements[2][i] = v
    else:
        for i in range(N):
            num = i+1
            print("Ingrese Precio de elemento", i+1, ":", end="")
            p = round(float(input()), 3)
            print("Ingrese Volumen de elemento", i+1, ":", end="")
            v = round(float(input()), 3)
            print()
            elements[0][i] = num
            elements[1][i] = p
            elements[2][i] = v
    print("Elementos:")
    for j in range(N):
        print("Num "+str(elements[0][j])+": $"+str(elements[1][j])+", "+str(elements[2][j])+" cm3")
    print()
    return elements

# Elements may be created randomly or with inputs
def generateElementsForGreedy(N, isRandom, maxVol, maxPrice):
    elements = [[] for _ in range(N)]  # Every Element has 3 values: Position (0), Price Value (0) and Volume (1)
    if isRandom:
        for i in range(N):
            num = i+1
            p = round(random.uniform(0, maxPrice), 3)
            v = round(random.uniform(0, maxVol), 3)
            b = round(p/v, 3)
            elements[i].append(num)
            elements[i].append(p)
            elements[i].append(v)
            elements[i].append(b)
    else:
        for i in range(N):
            num = i+1
            print("Ingrese Precio de elemento", i+1, ":", end="")
            p = round(float(input()), 3)
            print("Ingrese Volumen de elemento", i+1, ":", end="")
            v = round(float(input()), 3)
            print()
            b = p/v
            elements[i].append(num)
            elements[i].append(p)
            elements[i].append(v)
            elements[i].append(b)
    print("Elementos:")
    for j in range(N):
        print("    Num "+str(elements[j][0])+": $"+str(elements[j][1])+", "+str(elements[j][2])+" cm3, beneficio "+str(elements[j][3]))
    elements.sort(key=lambda x: x[3], reverse=True)  # Orders by benefit (higher to lower)
    return elements

def loadBackpack(N, elements, maxVolume, initialTime):
    backpack = []
    partialP = 0
    partialV = 0
    # partialB = 0
    for i in range(N):
        aux = []
        partialP += elements[i][1]
        partialV += elements[i][2]
        # partialB += elements[i][3]
        if partialV <= maxVolume:
            aux.append(elements[i][0])
            aux.append(elements[i][1])
            aux.append(elements[i][2])
            aux.append(elements[i][3])
        else:
            partialP -= elements[i][1]
            partialV -= elements[i][2]
            # partialB -= elements[i][3]
        if aux!=[]:
            backpack.append(aux)
    backpack.sort(key=lambda x: x[0])           # Orders by item number (lower to higher)
    print()
    print("Valor Acumulado de Precios: $" + str(round(partialP, 3)))
    print("Peso Total: " + str(round(partialV, 3)) + " cm3")
    # print("Beneficio acumulado: " + str(round(partialB, 3)))
    print("Elementos cargados:")
    for j in range(len(backpack)):
        print("    Num " + str(backpack[j][0]) + ": $" + str(backpack[j][1]) + ", " + str(backpack[j][2]) + " cm3, beneficio " + str(backpack[j][3]))
    finalTime = time()
    return finalTime-initialTime

# Calculate all the Possible Solutions sub-sets
def calculatePossibleSolutions(elements):
    N = len(elements)
    print("Índice de Combinaciones:")
    combinationsIndex = sum([list(map(list, combinations(elements[0], i))) for i in range(len(elements[0]) + 1)], [])
    print(combinationsIndex)
    solutions = []  # Array of 2^N sub-sets, one for every possible solution
    for x in range(len(combinationsIndex)):
        solutions.append([])
        partialP = 0
        partialV = 0
        for y in range(len(combinationsIndex[x])):
            z = combinationsIndex[x][y]
            partialP += elements[1][z-1]
            partialV += elements[2][z-1]
        solutions[x].append(round(partialP, 3))
        solutions[x].append(round(partialV, 3))
        solutions[x].append(combinationsIndex[x])
    print()
    print("Conjunto de Posibles Soluciones:")
    print("Solución --- Precio --- Volumen --- Elementos")
    for j in range(len(solutions)):
        print("S"+str(j)+": $"+str(solutions[j][0])+", "+str(solutions[j][1])+" cm3, elementos:", solutions[j][2])
    print()
    return solutions


# Exhaustive Search Algorithm and Exhibition of the Best Solution
def findBestSolution(solutions, maxVol, initialTime):
    best = 0
    bestValue = 0
    for i in range(len(solutions)):
        if solutions[i][1] <= maxVol and solutions[i][0] > bestValue:
            bestValue = solutions[i][0]
            best = i
    print("Total de Elementos: ", len(elements[0]))
    print("Peso Máximo de la Mochila: ", maxVol, "gramos")
    print()
    print("La Solución Óptima es: S" + str(best))
    if best != 0:
        print("Valor Acumulado de Precios: $" + str(solutions[best][0]))
        print("Peso Total: " + str(solutions[best][1]) + " cm3")
        print("Elementos:", solutions[best][2])
        for j in range(len(solutions[best][2])):
            k = solutions[best][2][j]-1
            print("    Num "+str(elements[0][k])+": $"+str(elements[1][k])+", "+str(elements[2][k])+" cm3")
    else:
        print("Ningún elemento entra en la mochila")
    finalTime = time()
    return finalTime-initialTime

def menu():
    strs = ('1) Metodo Exhaustivo\n'
            '2) Metodo Greedy\n'
            '3) Salir\n')
    choice = input(strs)
    return int(choice)

# Main Function
if __name__ == '__main__':
    # Important Values
    totalElements = 10  # Amount of Elements for the Problem
    randomCreation = True  # False: You must specify all elements value - True: They will create randomly
    bagMaxVolume = 4200  # Maximum Bag Capacity (in grams)
    maxPriceValue = 6000  # Maximum Money Value for an Element (only in Random Creation)

    while True:
        choice = menu()
        if choice == 1:
            if randomCreation == True:
                initialTime = time()  # Initial Time Mark
                # Generate all the N Elements
                elements = generateElements(totalElements, randomCreation, bagMaxVolume, maxPriceValue)
            else:
                # Generate all the N Elements
                elements = generateElements(totalElements, randomCreation, bagMaxVolume, maxPriceValue)
                initialTime = time()  # Initial Time Mark

            # Calculate all the Possible Solutions
            solutions = calculatePossibleSolutions(elements)

            # Exhaustive Search on the Solutions Set
            totalTime = findBestSolution(solutions, bagMaxVolume, initialTime)

            print()
            print("Solución obtenida correctamente en", totalTime, "segundos")
            break
        elif choice == 2:
            if randomCreation == True:
                initialTime = time()  # Initial Time Mark
                # Generate all the N Elements
                elements = generateElementsForGreedy(totalElements, randomCreation, bagMaxVolume, maxPriceValue)
            else:
                # Generate all the N Elements
                elements = generateElementsForGreedy(totalElements, randomCreation, bagMaxVolume, maxPriceValue)
                initialTime = time()  # Initial Time Mark

            # Executes Greedy method
            totalTime = loadBackpack(totalElements, elements, bagMaxVolume, initialTime)

            print()
            print("Solución obtenida correctamente en", totalTime, "segundos")
            break
        elif choice == 3:
            break





