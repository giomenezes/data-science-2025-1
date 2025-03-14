velocity_test = [50000, 75000, 100000]

def sum_of_n_init(n):
    acumul_acelerate = 0
    for i in range(1, n+1):
        acumul_acelerate = acumul_acelerate + i
    return acumul_acelerate

for i in velocity_test:
    print(sum_of_n_init(i))