def indirect_proof(hypothesis, conclusion):
    try:
        proof(hypothesis, conclusion)
    except ValueError:
        return True
    else:
        return False


def proof(hypothesis, conclusion):
    if hypothesis == conclusion:
        return True
    elif hypothesis.startswith("¬"):
        return proof(hypothesis[1:], conclusion)
    elif conclusion.startswith("¬"):
        return proof(hypothesis, conclusion[1:])
    elif hypothesis.startswith("∀"):
        for x in range(10):
            if not proof(hypothesis[1:] + "(x)", conclusion):
                return False
        return True
    elif hypothesis.startswith("∃"):
        for x in range(10):
            if proof(hypothesis[1:] + "(x)", conclusion):
                return True
        return False
    else:
        return False


def main():
    print(indirect_proof("∀x P(x)", "∃x Q(x)"))
    print(indirect_proof("¬∀x P(x)", "∃x Q(x)"))
    print(indirect_proof("∀x P(x)", "¬∃x Q(x)"))
    print(indirect_proof("¬∀x P(x)", "¬∃x Q(x)"))


if __name__ == "__main__":
    main()
