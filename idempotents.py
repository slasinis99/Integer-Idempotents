from math import sqrt, trunc

def find_idempotents(n: int):
    idem = []
    for i in range(n):
        if (i**2) % n == i:
            idem.append(i)
    if len(idem) == 2:
        print(n)
        return True, idem
    else: return False, idem
 
def is_prime(p: int):
    count = 1
    for i in range(1,trunc(sqrt(p))+1):
        if p % i == 0: count += 1
    if count == 2: return True
   
def verify_idem(n):
    vals = []
    for i in range(1,n):
        if find_idempotents(i)[0]:
            vals.append(i)
    count = 0
    for i in range(2,n):
        if i in vals:
            power = 1
            while is_prime(i):
                if i**power > n:
                    #print(f'{i}^{power} > {n}')
                    break
                else:
                    if not i**power in vals:
                        print(f'{i}^{power} not in set.')
                    else: 
                        print(f'{i}^{power} is in the set.')
                        count += 1
                    power += 1
    print(f'Length of Vals = {len(vals)}, Count = {count}')
    