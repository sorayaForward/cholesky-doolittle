
import math
import numpy as np


def Cholesky_Decomposition(matrix, n):
 
    lower = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    #Decomposer la matrice vers triangulaire inferieur
    
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0
 
            #sommer la diagonale
            if (j == i):
                for k in range(j):
                    sum1 += pow(lower[j][k], 2)
                lower[j][j] = int(math.sqrt(matrix_a[j][j] - sum1))
            else:
                for k in range(j):
                    sum1 += (lower[i][k] *lower[j][k])
                if(lower[j][j] > 0):
                    lower[i][j] = int((matrix_a[i][j] - sum1) / lower[j][j])
 
    # Affichage de L et sa transposé
    print("Triangulaire Inferieur Rt\tTranspose R")
    for i in range(n):
         
        #L
        for j in range(n):
            print(lower[i][j], end = "\t")
        print("", end = "\t")
         
        #Transposé de L
        for j in range(n):
            print(lower[j][i], end = "\t")
        print("")
 
#main
answer = "o"
while(answer=="o" or answer=="O"):
    bool=True
    print("\nDonner le nombre de lignes=collonnes de votre matrice\n")
    while bool:  
        try:
            n=int(input())
            if n<=0:
                raise ValueError
            else:
                bool=False     

        except ValueError:
            print("svp saissiez un nombre entier positive non nul")
            bool=True    
    #initialiser la matrices a des 1 partout
    matrix_a =np.array([[1 for x in range(n)]for y in range(n)])
    array_a=np.arange(n)
    #demander les valeurs de la matrice
    bool=True
    print(">La matrice")
    for i in range(0,n):
            print("\n>Donner la ligne "+str(i+1))
            for j in range(0,n):
                while(bool):
                    try:
                        matrix_a[i,j]=int(input("T["+str(i+1)+"]["+str(j+1)+"] = "))
                        bool=False
                    except ValueError:
                            print("Svp saissiez un nombre\n")
                            bool=True
                bool=True      


    Cholesky_Decomposition(matrix_a, n)
    answer = input("\n>Voulez vous echelonner une autre matrice ? ( o/n )")    

 
