from sage.crypto.util import random_blum_prime, ascii_to_bin, bin_to_ascii
def genP(p):
    a = p -1
    div =  prime_divisors(a)
    gens =[]
    for i in range(2,p):
        for j in range(0, len(div)):
            k = (i^(a/div[j])) % p
            #print "i = ", i,   " k = ",k
            if (k == 1):
                test = 0
                break
            else:
                test = 1
        if test == 1:
            gens.append(i)
    print ("dzielniki pierwsze dla p = ", p, "to ", div)
    return gens
p = random_blum_prime(2 ** 7 + 1, 2 ** 8 - 1)
gens = genP(p)
print ("generatory dla p = ", p, " to ",  gens)
print ("liczba generatorów dla p = ", p, " wynosi ", len(gens))
#a =5; c =17; N = 32; Xn = []; xn = 0;
n = len(gens)*(euler_phi(p))
m =32768
Xn = []
xn = 1
for i in range(0, len(gens)):
    for j in range(0,  p):
        xn = (gens[i]^j)% p
        Xn.append((xn + i )% p)
 #print Xn
 #point([(n, (a*n+c)%N) for n in range(1,m)],title='LCM PRNG %d,a = 5, c = 0,m = 32',size=25,color='red').show(frame=True)
 #point([(m, Xn[m]) for m in range(0,m-1)],title='LCM PRNG a = 5,c = 0, m = 32',size=25,color='blue'
point([(m, Xn[m%n]) for m in range(0,m)],legend_label = 'Xi+1= ? ', legend_color = 'green',title ='LCM PRNG p = ?',size=5,color='green')
