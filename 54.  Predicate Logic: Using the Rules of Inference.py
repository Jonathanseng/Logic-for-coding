def is_valid(formula1, formula2):
    if formula1 == formula2:
        return True
    elif formula1 == "¬P(x)" and formula2 == "P(x)":
        return False
    elif formula1 == "P(x) ∧ Q(x)" and formula2 == "P(x)":
        return True
    elif formula1 == "P(x) ∧ Q(x)" and formula2 == "Q(x)":
        return True
    elif formula1 == "P(x) ∨ Q(x)" and formula2 == "P(x)":
        return True
    elif formula1 == "P(x) ∨ Q(x)" and formula2 == "Q(x)":
        return True
    elif formula1 == "¬P(x)" and formula2 == "P(x) ∨ Q(x)":
        return True
    elif formula1 == "P(x)" and formula2 == "P(x) ∧ Q(x)":
        return True
    else:
        return False


def main():
    print(is_valid("P(x)", "P(x)"))
    print(is_valid("¬P(x)", "P(x)"))
    print(is_valid("P(x) ∧ Q(x)", "P(x)"))
    print(is_valid("P(x) ∧ Q(x)", "Q(x)"))
    print(is_valid("P(x) ∨ Q(x)", "P(x)"))
    print(is_valid("P(x) ∨ Q(x)", "Q(x)"))
    print(is_valid("¬P(x)", "P(x) ∨ Q(x)"))
    print(is_valid("P(x)", "P(x) ∧ Q(x)"))


if __name__ == "__main__":
    main()
