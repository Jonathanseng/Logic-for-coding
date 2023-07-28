def proof_system(formulas):
  """Returns True if formulas is provable, False otherwise."""
  if not isinstance(formulas, list):
    return False
  if len(formulas) == 0:
    return True
  if "for all x" in formulas or "exists x" in formulas:
    return False
  if formulas[0] == "not" and formulas[1] in formulas:
    return False
  for rule in rules:
    if rule[0] == formulas[0]:
      if all(rule[1] in formulas for rule[1] in rule[1:]):
        return True
  return False

rules = [
    (["P"], ["P"]),
    (["P", "Q"], ["P or Q"]),
    (["P", "Q"], ["P and Q"]),
    (["not P"], ["P implies Q"]),
    (["P implies Q", "Q"], ["P"]),
    (["for all x, P(x)"], ["P(a)"]),
    (["P(x)"], ["for all x, P(x)"])
  ]

def main():
  formulas = ["for all x, P(x)", "P(a)"]
  print(proof_system(formulas))
  print(universal_generalization(formulas))

def universal_generalization(formulas):
  """Returns a list of formulas that are universally generalized from formulas."""
  if not isinstance(formulas, list):
    return []
  if "for all x" in formulas:
    return formulas
  return formulas + [formula.replace("x", "a") for formula in formulas]

if __name__ == "__main__":
  main()
