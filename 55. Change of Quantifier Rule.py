def change_of_quantifier(formula):
    if formula.startswith("∀"):
        return "∃" + formula[1:]
    elif formula.startswith("∃"):
        return "∀" + formula[1:]
    else:
        return formula


def main():
    print(change_of_quantifier("∀x P(x)"))
    print(change_of_quantifier("∃x P(x)"))
    print(change_of_quantifier("P(x)"))


if __name__ == "__main__":
    main()
