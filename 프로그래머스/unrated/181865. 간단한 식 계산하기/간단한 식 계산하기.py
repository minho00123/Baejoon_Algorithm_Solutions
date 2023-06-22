def solution(binomial):
    binomial = binomial.split()
    exp = binomial[1]
    n1 = int(binomial[0])
    n2 = int(binomial[2])
    if exp == '+':
        return n1 + n2
    elif exp == '-':
        return n1 - n2
    elif exp == '*':
        return n1 * n2