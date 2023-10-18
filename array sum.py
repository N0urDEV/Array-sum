N = int(input("Enter the size of the arrays: "))
T1 = []
T2 = []
print("Enter values for array T1:")
T1 = [int(input()) for _ in range(N)]
print("Enter values for array T2:")
T2 = [int(input()) for _ in range(N)]
T = [T1[i] + T2[i] for i in range(N)]
print("Resulting array T:", T)
