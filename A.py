import re
from sympy import symbols, Not


def main():
    expr_string = '~x ^ (y & z) ^ (x & z & ~y)'  # alternatively s = input()
    syms = [symbols(i) for i in set(re.findall('\w', expr_string))]
    expr = eval(expr_string, {i.name: i for i in syms})

    if expr.subs({i.name: False for i in syms}):
        print(expr_string == '1')
        return

    args = []
    for arg in expr.args:  # ~y&z like terms
        args.append((set(map(str, arg.args)), arg))  # ({"~y", "z"} set, ~y&z)

    min_args = []
    for i in args:
        for j in args:
            if j[0] < i[0]:  # not minimal
                break
        else:
            min_args.append(i[1])
    
    all_atoms = set(syms)

    for min_arg in min_args:
        other_atoms = all_atoms - min_arg.atoms()
        d = {i: arg.func != Not for arg in min_arg.args for i in arg.atoms()}
        for other_atom in other_atoms:
            if expr.subs({other_atom: True, **d}).simplify() != True:
                print('Non monotonous')
                return

main()
