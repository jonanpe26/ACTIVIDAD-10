def invertir(c, i=0):
    if i == len(c):
        return ""
    return invertir(c, i + 1) + c[i]}

