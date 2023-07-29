def is_valid_in_finite_universe(formula, universe):
    for interpretation in universe:
        if not evaluate_formula(formula, interpretation):
            return False
    return True


def evaluate_formula(formula, interpretation):
    if formula == "P(x)":
        return interpretation["x"]
    elif formula == "¬P(x)":
        return not interpretation["x"]
    elif formula == "P(x) ∧ Q(x)":
        return interpretation["x"] and interpretation["Q(x)"]
    elif formula == "P(x) ∨ Q(x)":
        return interpretation["x"] or interpretation["Q(x)"]
    elif formula == "∀x P(x)":
        for x in universe:
            if not evaluate_formula("P(x)", interpretation):
                return False
        return True
    elif formula == "∃x P(x)":
        for x in universe:
            if evaluate_formula("P(x)", interpretation):
                return True
        return False
    else:
        raise ValueError("Unknown formula: " + formula)


def main():
    universe = {"a": True, "b": False, "c": True}
    print(is_valid_in_finite_universe("∀x P(x)", universe))
    print(is_valid_in_finite_universe("∃x P(x)", universe))


if __name__ == "__main__":
    main()
