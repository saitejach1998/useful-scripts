
from cryptonita import B
from cryptonita.mod import inv_matrix
import numpy as np


#load ciphertext. load the known plaintext as ImmutableByteString; B('stuff')
ciphertext = B('')
known_plaintext = B('thequickb')
dim = 2
mod = 127 # depends on the charset; 26 - English Alphabet; 127 - Ascii
known_ct = ciphertext[0:9]


P = np.array(list(known_plaintext)).reshape(dim,dim).T
C = np.array(list(known_ct)).reshape(dim,dim).T

'''
C = KP mod m

K = C P(inv) mod m

K is the key used to encrypt
'''
iP = inv_matrix(P, mod) 
K = np.dot(C, iP) % mod

'''
Now we know K. we need P

P = C K(inv) mod m 

'''
iK = inv_matrix(K, mod)



'''

Since Hill cipher is a block cipher, 
it's processed in chunks of n characters 
where n is the n x n matrix used to encrpyt
the plaintext.

'''

cblocks = ciphertext.nblocks(dim)
plaintext = []
for cblk in cblocks:
    ci = np.array(list(cblk)).reshape(dim, 1)
    pi = np.dot(iK, ci) % mod
    plaintext.append(B(list(pi.ravel())))

plaintext = b''.join(plaintext)
print(plaintext.decode())
