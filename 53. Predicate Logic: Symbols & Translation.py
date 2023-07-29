def translate_predicate(predicate):
    if predicate == "P(x)":
        return "x is a person"
    elif predicate == "Q(x)":
        return "x is a dog"
    elif predicate == "R(x, y)":
        return "x is taller than y"
    else:
        raise ValueError("Unknown predicate: " + predicate)


def translate_formula(formula):
    if formula == "P(x)":
        return translate_predicate("P(x)")
    elif formula == "Q(x)":
        return translate_predicate("Q(x)")
    elif formula == "R(x, y)":
        return translate_predicate("R(x, y)")
    elif formula == "P(x) ∧ Q(x)":
        return "x is a person and x is a dog"
    elif formula == "P(x) ∨ Q(x)":
        return "x is a person or x is a dog"
    elif formula == "¬P(x)":
        return "x is not a person"
    elif formula == "P(x) → Q(x)":
        return "if x is a person then x is a dog"
    elif formula == "P(x) ↔ Q(x)":
        return "x is a person if and only if x is a dog"
    else:
        raise ValueError("Unknown formula: " + formula)


print(translate_formula("P(x)"))
print(translate_formula("Q(x)"))
print(translate_formula("R(x, y)"))
print(translate_formula("P(x) ∧ Q(x)"))
print(translate_formula("P(x) ∨ Q(x)"))
print(translate_formula("¬P(x)"))
print(translate_formula("P(x) → Q(x)"))
print(translate_formula("P(x) ↔ Q(x)"))
