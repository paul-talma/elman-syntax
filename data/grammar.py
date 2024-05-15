import random

random.seed(0)

# number of sentences to generate
num_sentences = 10_000

# define categories
N_HUM = ["man", "woman", "boy", "girl"]
N_AGRESS = ["dragon", "monster", "lion"]
N_ANIM = N_HUM + N_AGRESS + ["cat", "mouse", "dog"]
N_FRAG = ["glass", "plate"]
N_FOOD = ["cookie", "bread", "sandwich"]
N_INANIM = N_FRAG + N_FOOD + ["book", "rock", "car"]
V_INTRAN = ["think", "sleep", "exist"]
V_TRAN = ["see", "chase", "like"]
V_AGPAT = ["move", "break"]
V_PERCEPT = ["smell", "see"]
V_DESTROY = ["break", "smash"]
V_EAT = ["eat"]

# define templates
templates = []
templates.append([N_HUM, V_EAT, N_FOOD])
templates.append([N_HUM, V_PERCEPT, N_INANIM])
templates.append([N_HUM, V_DESTROY, N_FRAG])
templates.append([N_HUM, V_INTRAN])
templates.append([N_HUM, V_TRAN, N_HUM])
templates.append([N_HUM, V_AGPAT, N_INANIM])
templates.append([N_HUM, V_AGPAT])
templates.append([N_ANIM, V_EAT, N_FOOD])
templates.append([N_ANIM, V_TRAN, N_ANIM])
templates.append([N_ANIM, V_AGPAT, N_INANIM])
templates.append([N_ANIM, V_AGPAT])
templates.append([N_INANIM, V_AGPAT])
templates.append([N_AGRESS, V_DESTROY, N_FRAG])
templates.append([N_AGRESS, V_EAT, N_HUM])
templates.append([N_AGRESS, V_EAT, N_ANIM])
templates.append([N_AGRESS, V_EAT, N_FOOD])

# same as: vocab = set([word for temp in templates for cat in temp for word in cat])
vocab = set(sum(sum(templates,[]),[]))
print("vocab size", len(vocab))

with open("data/elman_sentences.txt", "w") as fid:
    for i in range(num_sentences):
        T = random.choice(templates)
        S = []
        for mylist in T:
            S.append(random.choice(mylist))
        fid.write(" ".join(S) + "\n")

