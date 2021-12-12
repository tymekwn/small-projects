def differentiation(termlist):
    derivations = range(int(input("Number of derivations?")))
    for _ in derivations:
        for i in termlist:
            i[0] = i[0]*i[1]
            i[1] = i[1]-1
    return termlist

def makelist(terms,termlist):
    coeff = int(input(f"Enter Coefficient"))
    power = int(input(f"Enter power"))
    termlist.append([coeff,power])
    newterms = differentiation(termlist) if terms-1 <= 0 else makelist(terms-1,termlist)
    return newterms

def main():
    terms = int(input("Number of terms?"))
    termlist = []
    newterms = makelist(terms,termlist)
    for i in termlist: print(f"{i[0]}x^{i[1]}")

if __name__ == "__main__":main()
    
    
    
