import random as ran
import sys
import json

def assemble(*args):
    return(" ".join(args))

def NP(T,N):
    return assemble(T,N)

def VP(Verb,NP):
    return assemble(Verb,NP)

def sentence(NP,VP):
    return assemble(NP,VP)

def list_load(fileName, listName):
    print(fileName, listName)

    with open( fileName, mode='r') as f:
      # Read JSON file and store its content in an Python variable
      # By using json.load() function
      json_data = json.load(f)
      
      # So now json_data contains list of dictionaries
      # (because every JSON is a valid Python dictionary)
      # We start to iterate over each dictionary in our list
      for json_dict in json_data:
          # We append each name value to our result list
          listName.append(json_dict['value'])

def loop(X):
    L = ['school', 'station', 'office', 'shop']

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

##############################################
# MAINLINE
##############################################

# Then we create a result list, in which we will store our names
result_list = []
A = []
N = []
T = []
Verb = []

list_load('adjectives.json', A)
list_load('nouns.json', N)
list_load('articles.json', T)
list_load('verbs.json', Verb)

print(Verb)
print()

# Shorter solution by using list comprehension
# --------------------------------------------
# result_list = [json_dict['value'] for json_dict in json_data]
# print(result_list)  # ['Hurzuf', 'Novinki']

#sys.exit()

loop(int(sys.argv[1]))

