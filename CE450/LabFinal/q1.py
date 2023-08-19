from math import exp

if __name__ == "__main__":
    T: list[float] = [100.0 * (1 - exp((-(t / 10.0) - 12.06) / 10.0))
                      for t in range(0, 42, 2)]
    E: list[float] = [100.0 - t for t in T]
    deltaU: list[float] = [0, 0]
    for i in range(2, len(E)):
        deltaU.append(8 * (E[i] - E[i - 1]) + 5 * E[i] +
                      1.6 * (E[i] - 2 * E[i - 1] + E[i - 2]))
    U: list[float] = [0, 120.0]
    for i in range(2, len(deltaU)):
        U.append(U[-1] + deltaU[i])
    print(U)
