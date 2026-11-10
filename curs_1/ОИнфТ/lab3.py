import numpy as np




def D1F(x, F, h):
    return (F(x + h) - F(x - h)) / (2*h)


def D2F(x, F, h):
    return (F(x + h) - 2 * F(x) + F(x - h)) / h ** 2 




def main():

    print("----- Calculation of derivatives and integrals -----")
    
    (a, b) = [-4, 2]

    h_values = [0.2, 0.1, 0.005]

    m = [10, 20, 40]
    
    F = lambda x: 0.1 * x**3 + x**2 - 10 * np.sin(x)
    dF = lambda x: 0.3 * x**2 + 2 * x - 10 * np.cos(x)
    d2F = lambda x: 0.6x + 2 + 10 * np.sin(x)

    for hp in h_values:

        print(f"Результаты для шага hp({hp})")

        for j in range(1, 22):

            x = a + (j - 1) * (b - a) / 20
            y = F(x)

            d1 = D1F(x, F, hp)
            d2 = D2F(x, F, hp)

            d1t = dF(x)
            d2t = d2F(x)
    
            dif_1F = d1t - d1
            dif_2F = d2t - d2

            print(f"|{}|")


        

 







if __name__ == "__main__":
    main()












