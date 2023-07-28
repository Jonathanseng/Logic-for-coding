def definable(structure, formula):
  """Returns True if formula is definable in structure, False otherwise."""
  if not isinstance(formula, str):
    return False
  if formula in structure:
    return True
  if len(formula) == 2 and formula[0] in ["x", "f"]:
    return formula[0] in structure
  if len(formula) == 3 and formula[0] == "and":
    return definable(structure, formula[1]) and definable(structure, formula[2])
  if len(formula) == 3 and formula[0] == "or":
    return definable(structure, formula[1]) or definable(structure, formula[2])
  if len(formula) == 3 and formula[0] == "not":
    return not definable(structure, formula[1])
  return False

def main():
  structure = {"x": True, "y": False}
  formulas = [
    "x",
    "y",
    "x and y",
    "x or y",
    "not x",
    "not y"
  ]
  for formula in formulas:
    print(definable(structure, formula))

if __name__ == "__main__":
  main()
