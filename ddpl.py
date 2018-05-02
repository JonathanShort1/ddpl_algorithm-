import re

#negate the unit clause
def negate(cl):
    a = cl[1:-1]
    if len(a) == 2:
        return "(" + a[1] + ")"
    else:
        return "(¬" + a + ")"

# get a unit clause
def getUnitClause(clauses):
    if clauses:
        for cl in clauses:
            if len(cl) <= 4:
                return cl
    return None

# get a unit clause from the first composite clause
def getFirstUnitClause(clauses):
    if clauses:
        c = clauses[0]
        if c[1] == "¬":
            return "(" + c[1:3] + ")"
        else:
            return "(¬" + c[1] + ")"
    return None

# if the negated unit clause is present
def isNegate(c, a):
    if negate(a) in c:
        li = list(c.replace(negate(a), "")) # remove negated unit
        li_new = []
        if (len(li) > 0):
            if li[0] == "|": li = li[1:] # remove leading or
            if li[-1] == "|": li = li[:-1] # remove trailing or
            li_new = [li[0]]
            for i in range(1, len(li)): # remove double or from middle of clause
                if not (li[i - 1] == "|" and li[i] == "|"):
                    li_new.append(li[i])
        return "".join(li_new)
    return c

# peform unit propagation on the set of conjuective clauses
def unit_prop(clauses, a):
    if a is None: return []
    clauses[:] = [cl for cl in clauses if not a in cl]
    clauses[:] = [isNegate(cl, a) for cl in clauses]
    return clauses

# perform the DDPL algorithm on the set on clauses in CNF
def ddpl(clauses):
    if len(clauses) == 0: # all clauses have been reduced
        return True
    if "" in clauses: # the empty clause has been reached! contradiction
        return False
    x = getUnitClause(clauses)
    if x  is not None: # propagate unit clause
        return ddpl(unit_prop(clauses, x))
    else:
       a = getFirstUnitClause(clauses) # select a random unit clause
       return ddpl(unit_prop(clauses, a)) or ddpl(unit_prop(clauses, negate(a)))

def main():
    clauses= [
        "(¬y)|(w)",
        "(¬w)|(z)",
        "(u)",
        "(¬u)|(¬v)",
        "(¬u)|(x)",
        "(¬x)|(y)|(w)",
        "(¬w)|(¬z)|(v)"
    ]
    print(ddpl(clauses))

if __name__ == "__main__":
    main()
