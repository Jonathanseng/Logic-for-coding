def truth_value(formula, model):
  """Returns the truth value of formula in model, or None if formula is not a propositional logic formula."""
  if not is_formula(formula):
    return None
  elif formula in ["True", "False"]:
    return formula == "True"
  elif formula == "not":
    return not truth_value(formula[1], model)
  elif formula == "and":
    return truth_value(formula[0], model) and truth_value(formula[1], model)
  elif formula == "or":
    return truth_value(formula[0], model) or truth_value(formula[1], model)
  else:
    raise ValueError(f"Invalid formula: {formula}")

def main():
  model = {"P": True, "Q": False}
  print(truth_value("P", model))
  print(truth_value("not P", model))
  print(truth_value("P and Q", model))
  print(truth_value("P or Q", model))

if __name__ == "__main__":
  main()
