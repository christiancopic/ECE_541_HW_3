from control.matlab import *

def main():
    #Problem 1

    A1 = [[-100, 0],  [-10, 2]]
    B1 = [[1],[0]]
    C1 = [[0,1]]
    D1 = [0]

    SS1 = ss(A1,B1,C1,D1)
    print("Problem 1: \n")
    print(tf(SS1))
    print("\n\n")

    #Problem 2

    A2 = [[1, 2], [0, 0]]
    B2 = [[0],[1]]
    C2 = [[1,0]]
    D2 = [0]

    SS2 = ss(A2,B2,C2,D2)
    print("Problem 2: \n")
    print(tf(SS2))
    print("\n\n")

    #Problem 3

    A3 = [[-4, -2, 0],  [2, -1, 0], [4, 1, 0]]
    B3 = [[0],[1], [0]]
    C3 = [[0,0, 1]]
    D3 = [0]

    SS3 = ss(A3,B3,C3,D3)
    print("Problem 3: \n")
    print(tf(SS3))
    print("\n\n")


if __name__ == '__main__':
    main()