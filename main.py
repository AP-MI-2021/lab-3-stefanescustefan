def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True


def get_longest_all_primes(lst):
    """
    Determina cea mai lunga subsecventa formata doar din numere prime

    :param lst: O lista de numere naturale
    :return: Cea mai lunga subsecventa formata doar din numere prime
    """
    start = -1
    subsequence_max = []
    for i in range(len(lst)):
        if is_prime(lst[i]):
            if start == -1:
                start = i
            if len(subsequence_max) < i - start + 1:
                subsequence_max = lst[start:i+1]
        else:
            start = -1

    return subsequence_max


def test_get_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([4, 10, 1]) == []
    assert get_longest_all_primes([1, 7, 3, 4, 5]) == [7, 3]
    assert get_longest_all_primes([4, 3, 5, 9, 11, 13, 3]) == [11, 13, 3]


def is_equal_int_real(x):
    s = str(x)
    i, r = s.split(".")
    if i == r:
        return True
    else:
        return False


def get_longest_equal_int_real(lst):
    """
    Determina cea mai lunga subsecventa in care toate numerele au partea intreaga egala cu cea fractionara

    :param lst: O lista de numere reale
    :return: Cea mai lunga subsecventa in care toate numerele au partea intreaga egala cu cea fractionara
    """
    start = -1
    subsequence_max = []
    for i in range(len(lst)):
        if is_equal_int_real(lst[i]):
            if start == -1:
                start = i
            if len(subsequence_max) < i - start + 1:
                subsequence_max = lst[start:i + 1]
        else:
            start = -1

    return subsequence_max


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([1.03, 2.5]) == []
    assert get_longest_equal_int_real([0.99, 99.99, 3.3]) == [99.99, 3.3]
    assert get_longest_equal_int_real([12.12, 1.1, 0.3]) == [12.12, 1.1]
    assert get_longest_equal_int_real([2.3, 3.2, 97.97]) == [97.97]


def is_power_of_k(n, k):
    """
    Determina daca n poate fi scris ca x**k, x natural

    :param x: Un numar natural
    :param k: Exponentul
    :return: True, daca n poate fi scris ca x**k, False in caz contrar
    """
    if n**(1/k) == int(n**(1/k)):
        return True
    else:
        return False


def get_longest_powers_of_k(lst, k):
    """
    Determina cea mai lunga subsecventa in care toate numerele au radacini de ordin k naturale

    :param lst: O lista de numere intregi
    :param k: Exponentul
    :return: Cea mai lunga subsecventa in care toate numerele au radacini de ordin k naturale
    """
    start = -1
    subsequence_max = []
    for i in range(len(lst)):
        if is_power_of_k(lst[i], k):
            if start == -1:
                start = i
            if len(subsequence_max) < i - start + 1:
                subsequence_max = lst[start:i + 1]
        else:
            start = -1

    return subsequence_max


def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([7, 23, 10], 2) == []
    assert get_longest_powers_of_k([5, 25, 7, 36, 49, 16], 2) == [36, 49, 16]
    assert get_longest_powers_of_k([27, 8, 1, 10, 1], 3) == [27, 8, 1]
    assert get_longest_powers_of_k([16, 1, 5, 81], 4) == [16, 1]


def main():
    test_get_longest_all_primes()
    test_get_longest_equal_int_real()
    test_get_longest_powers_of_k()
    end = False
    l = []
    while not end:
        print("1. Cititi lista")
        print("2. Determinati cea mai lunga subsecventa de numere prime")
        print("3. Determinati cea mai lunga subsecventa de numere pt care p.f. egala cu p.i.")
        print("4. Determinati cea mai lunga subsecventa de numere care au radacini de ordin k intregi")
        print("x. Iesire")
        optiune = input("Optiune: ")
        if optiune == '1':
            l = input("Dati numerele separate prin virgula: ").split(",")
        elif optiune == '2':
            l_nr = []
            for x in l:
                l_nr.append(int(x))
            print(get_longest_all_primes(l_nr))
        elif optiune == '3':
            l_float = []
            for x in l:
                l_float.append(float(x))
            print(get_longest_equal_int_real(l_float))
        elif optiune == '4':
            k = int(input("Dati un numar k: "))
            l_nr = []
            for x in l:
                l_nr.append(int(x))
            print(get_longest_powers_of_k(l_nr, k))
        elif optiune == 'x':
            end = True


if __name__ == '__main__':
    main()
