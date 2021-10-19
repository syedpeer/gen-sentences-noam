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
        'ball', 'monkey', 'computer', 'guitar', 'fire']
    Verb = ['hit','polished','healed','tore','treated','coded','ran']

    for i in range(X):
        N1, N2 = ran.choice(N), ran.choice(N)
        T1, T2 = ran.choice(T), ran.choice(T)
        Verb1 = ran.choice(Verb)

        NP1 = NP(T1,N1)
        NP2 = NP(T2,N2)
        VP1 = VP(Verb1, NP2)
        print(sentence(NP1,VP1))

loop(int(sys.argv[1]))

