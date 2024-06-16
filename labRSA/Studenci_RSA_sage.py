#print q
print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#from sage.crypto.stream
#file = open("H:/DCD/PRNG_projekt/RSA/daneRSA_test_BBS_16.txt", "w")
size = 64
for i in range(1 , 10):
    p = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
    q = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
#print psage: sage: from sage.crypto.util import random_blum_prime, ascii_to_bin, bin_to_ascii

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXXXXXXXXXX"
 #from sage.crypto.stream
 #file = open("H:/DCD/PRNG_projekt/RSA/daneRSA_test_BBS_16.txt", "w")
 size = 64
for i in range(1 , 2):
    p = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
    q = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
 #print p
 #print q
    rsa = RSA(p, q)
 #msg = "The quick brown fox jumps over the lazy dog"
    msg = "Hello World !"
    res = rsa.encrypt(msg)
    linia = ( i, p, q, res)

  #   linia = (res,  i)
  #   file.writelines(str(linia) +"\n")
    print linia
     #file.write(str(res)  + "\n")
  #   file.writelines(str(linia) + "\n")
     #print rsa.decrypt(res, len(msg))
    print msg

 #   linia = (res,  i)
 #   file.writelines(str(linia) +"\n")
    print linia
    #file.write(str(res)  + "\n")
 #   file.writelines(str(linia) + "\n")
    #print rsa.decrypt(res, len(msg))
print msg

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#from sage.crypto.stream
#file = open("H:/DCD/PRNG_projekt/RSA/daneRSA_test_BBS_16.txt", "w")
size = 64
for i in range(1 , 10):
    p = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
    q = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
#print p
#print q
    rsa = RSA(p, q)
#msg = "The quick brown fox jumps over the lazy dog"
    msg = "Hello World"
    res = rsa.encrypt(msg)
    linia = ( i, p, q, res)

 #   linia = (res,  i)
 #   file.writelines(str(linia) +"\n")
    print linia
    #file.write(str(res)  + "\n")
 #   file.writelines(str(linia) + "\n")
    #print rsa.decrypt(res, len(msg))
print msg

