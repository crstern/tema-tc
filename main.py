# #example for direct left recursion
# gram = {"A":["Aa","Ab","c","d"]
# }
# example for indirect left recursion
# neterminali = ["S", "A", "B", "C"]
# terminali = ["a", "b", "c", "d", "g", "h", "lambda"]
# start = "S"
# prod = {
#     "S": ["ACB", "Cbb", "Ba"],
#     "A": ["da", "Bc"],
#     "B": ["g", "!"],
#     "C": ["h", "!"]
# }
start = "E"
lambda_var = "ł"
neterminali = ["E", "D", "T", "W", "F"]
terminali = ["a", "(", ")", lambda_var, "*", "+"]
productii = {
    "E": ["TD"],
    "D": ["+TD", lambda_var],
    "T": ["FW"],
    "W": ["*FW", lambda_var],
    "F": ["(E)", "a"]
}


def get_first(prod, elem):
    first = set()
    if elem not in neterminali:
        first.add(elem)
        return first
    for s in prod[elem]:
        if s[0] not in neterminali:
            first.add(s[0])
        else:
            first_s = get_first(prod, s[0])
            first = first.union(first_s)
    return first

def union(setA, setB):
    n = len(setA)
    setA |= setB
    return len(setA) != n

def get_follows(productii, start):
    follow = {i : set() for i in neterminali}
    follow[start] = set("$")
    epsilon = set(lambda_var)
    while True:
        updated = False
        for nt in neterminali:
            follow_nt = follow[nt]
            for expresie in productii[nt]:
                for i in range(len(expresie)):
                    if expresie[i] in neterminali:
                        nt_expresie = expresie[i]
                        if i == len(expresie) - 1:
                            updated |= union(follow[nt_expresie], follow_nt)
                        else:
                            found = False
                            for j in range(i + 1, len(expresie)):
                                nt_urmator = expresie[j]
                                if lambda_var in firsts[nt_urmator]:
                                    updated |= union(follow[nt_expresie], firsts[nt_urmator].difference(epsilon))
                                else:
                                    found = True
                                    updated |= union(follow[nt_expresie], firsts[nt_urmator])
                                    break
                            if not found:
                                updated |= union(follow[nt_expresie], follow_nt.difference(epsilon))




        if not updated:
            return follow


firsts = {}
print("First:")
for s in neterminali + terminali:
    firsts[s] = get_first(productii, s)
    print(s, firsts[s])

follows = get_follows(productii, start)
print("================================")
print("Follow:")
for p in follows:
    print(p, follows[p])