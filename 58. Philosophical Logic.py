def is_valid_argument(premises, conclusion):
    for interpretation in generate_all_interpretations():
        if not evaluate_formula(premises, interpretation) or not evaluate_formula(conclusion, interpretation):
            return False
    return True


def generate_all_interpretations():
    yield {}
    for x in range(2):
        interpretation = {"x": x}
        for y in range(2):
            yield interpretation.copy()
            interpretation["y"] = y


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
        for x in interpretation:
            if not evaluate_formula("P(x)", interpretation):
                return False
        return True
    elif formula == "∃x P(x)":
        for x in interpretation:
            if evaluate_formula("P(x)", interpretation):
                return True
        return False
    else:
        raise ValueError("Unknown formula: " + formula)


def main():
    premises = ["P(x) ∨ Q(x)", "¬Q(x)"]
    conclusion = "P(x)"
    print(is_valid_argument(premises, conclusion))


if __name__ == "__main__":
    main()
