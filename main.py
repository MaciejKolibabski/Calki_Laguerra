import math
import numpy as np
import matplotlib.pyplot as plt

def schemat_hornera(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

#do Newtona-Cotesa
def wartosci(x,  choice):
    if choice == '1':
        return math.exp(-x) * (10 * x - 2)
    elif choice == '2':
        tab = [2, 1, 5, -4, -20]
        return math.exp(-x) * schemat_hornera(tab, len(tab), x)
    elif choice == '3':
        return math.exp(-x) * math.sin(2*x)
    elif choice == '4':
        return math.exp(-x) * math.fabs(math.cos(x**2))

#Do Laguerra
def wartosci1(x, choice):
    if choice == '1':
        return 10 * x - 2
    elif choice == '2':
        tab = [2, 1, 5, -4, -20]
        return schemat_hornera(tab, len(tab), x)
    elif choice == '3':
        return math.sin(2*x)
    elif choice == '4':
        return math.fabs(math.cos(x**2))

def simson(a, b, choice, choice2, wynik, wynik1, n):
    n += 1
    wynik = wynik1
    dx = (np.double(b) - np.double(a)) / (n)
    suma2 = 0
    suma = 0
    for i in range(1,n):
        x = np.double(a) + i * dx
        suma += wartosci(x - dx / 2.0,  choice)
        suma2 += wartosci(x,  choice)

    suma += wartosci(b - dx / 2.0,  choice)
    if (choice2 == '1'):
        wynik1 = (dx / 6.0) * (wartosci(a,  choice) + wartosci(b,  choice) + 2 * suma2 + 4 * suma)

    else:
        wynik1 += (dx / 6.0) * (wartosci(a, choice) + wartosci(b,  choice) + 2 * suma2 + 4 * suma)
    return wynik,wynik1,n

def laguerre(choice, wezly, wspolcz, n, wynik, wynik1):
    wynik = wynik1
    wynik1 = 0
    for i in range(n):
        wynik1 += wspolcz[i] * wartosci1(wezly[i], choice)
    return wynik,wynik1

if __name__ == '__main__':
    tab = [2, 1, 5, -4, -20]
    wynik = 0
    wynik1 = 0

    n = 1

    x1 = [0.585789, 3.414214]
    x2 = [0.415775, 2.294280, 6.289945]
    x3 = [0.322548, 1.745761, 4.536620, 2.395071]
    x4 = [0.263560, 1.413403, 3.596426, 7.085810, 12.640801]
    a1 = [0.853553, 0.146447]
    a2 = [0.711093, 0.278518, 0.010389]
    a3 = [0.603154, 0.357419, 0.038888, 0.000539]
    a4 = [0.521756, 0.398667, 0.075942, 0.003612, 0.000023]
    X = [x1, x2, x3, x4]
    A = [a1, a2, a3, a4]
    print("Wybierz jedna z funkcji:")
    print("1. 10x - 2 ")
    print("2. 2x^4 + x^3 + 5x^2 - 4x - 20 ")
    print("3. sin(2*x) ")
    print("4. |cos(x^2)| ")
    choice = input("Podaj wariant wybranej funkcji: ")
    ile = 0
    print("Wybierz sposób całkowania: ")
    print("1. Określony przedział całkowania")
    print("2. Przedział całkowania [0; infinity]")
    choice2 = input("Podaj wariant całkownaia:  ")
    if ( choice2 == '1'):
         print("Określ przedział: ")
         a = input("Początek przedziału: ")
         b = input("Koniec przedziału:  ")
         eps = input("Podaj dokładnośc:  " )

         while True:
             wynik, wynik1, n=simson(np.double(a),np.double(b),choice,choice2,np.double(wynik),np.double(wynik1),n)
             ile+=1
             if (math.fabs(np.double(wynik) - np.double(wynik1)) < np.double(eps)):
                 print("Wynik dla danego przedziału:")
                 print(wynik1)
                 print("Dla liczby przedziałów")
                 print(ile)
                 break

    elif choice2 == '2' :
         ile = 0
         eps = input("Podaj dokładność:  ")
         a = 0
         wynik1 = 0
         while True:
             wynik, wynik1, n = simson(np.double(a), np.double(a+1), choice, choice2,  np.double(wynik), np.double(wynik1), n)
             a+=1
             ile += 1
             if (math.fabs(np.double(wynik) - np.double(wynik1)) < np.double(eps)):
                 print("Wynik dla danego przedziału:")
                 print(wynik1)
                 print("Dla liczby przedziałów")
                 print(ile)
                 break
         wynik1=0
         wynik=0
         m=1

         while True:
             wynik, wynik1=laguerre(choice,X[m-1],A[m-1],m,wynik,wynik1)
             m+=1
             #print("Lg",wynik,wynik1,m)
             if (math.fabs(wynik1-wynik)<np.double(eps) or m>4):
                 print("Wynika metoda Laguerra ")
                 print(wynik1)
                 print("Dla liczby wezłów: ")
                 print(m-1)
                 break

    # #Dla określonego przediału
    # x = np.linspace(np.double(a), np.double(b), 1000)
    # z = np.vectorize(wartosci1)
    # y = z(x, choice)
    # plt.plot(x, y, 'r-')
    # plt.fill_between(x, y, alpha=0.30 )
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title(choice)
    # plt.show()

    # #Dla przedziału [0; inf)
    # x = np.linspace(0, 10, 1000)
    # z = np.vectorize(wartosci)
    # y = z(x, choice)
    # plt.plot(x, y, 'r-')
    # plt.fill_between(x, y, alpha=0.30)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()
