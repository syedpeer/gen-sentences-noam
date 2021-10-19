import random as ran
import sys

def assemble(*args):
    return(" ".join(args))

def NP(T,N):
    return assemble(T,N)

def VP(Verb,NP):
    return assemble(Verb,NP)

def sentence(NP,VP):
    return assemble(NP,VP)

def loop(X):
    T = ['the','their','our','his','her']
    N = ['man','woman', 'boy', 'girl', 'son', 'daughter', \
         'uncle', 'aunt', 'father', 'mother']
    L = ['school', 'station', 'office', 'shop']
    A = ['tall', 'short', 'fat', 'slim', 'old', 'young']
    Verb = ['hit','pushed','healed','tore','treated','scolded','ran to']

    for i in range(X):
        T1, T2 = ran.choice(T), ran.choice(T)
        if (T2 == T1):
            T2 = ran.choice(T)
        A1, A2 = ran.choice(A), ran.choice(A)
        if (A2 == A1):
            A2 = ran.choice(A)
        N1, N2 = ran.choice(N), ran.choice(N)
        if (N2 == N1):
            N2 = ran.choice(N)

        T1 = NP(T1,A1) # add adjecive after article
        T2 = NP(T2,A2) # add adjecive after article

        Verb1 = ran.choice(Verb)

        NP1 = NP(T1,N1)
        NP2 = NP(T2,N2)
        VP1 = VP(Verb1, NP2)
        print(sentence(NP1,VP1))

loop(int(sys.argv[1]))

