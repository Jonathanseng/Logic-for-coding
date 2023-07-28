def soundness(axioms, theorems):
  """Returns True if all theorems are sound, False otherwise."""
  for theorem in theorems:
    if not is_valid_proof(["axiom"] + axioms + ["inference", theorem]):
      return False
  return True

def consistency(axioms):
  """Returns True if axioms are consistent, False otherwise."""
  for formula in axioms:
    if not is_satisfiable([formula]):
      return False
  return True

def maximality_consistent(axioms, theorems):
  """Returns True if axioms are maximally consistent, False otherwise."""
  for formula in theorems:
    if not is_satisfiable([formula] + axioms):
      return False
  return True

def monotonicity(axioms, theorems1, theorems2):
  """Returns True if theorems1 implies theorems2, False otherwise."""
  for theorem in theorems2:
    if not is_valid_proof(["axiom"] + axioms + ["inference", theorem]):
      return False
  return True

def main():
  axioms = ["P implies Q", "Q implies R"]
  theorems1 = ["P implies R"]
  theorems2 = ["P implies Q", "Q implies R", "P implies R"]
  print(soundness(axioms, theorems1))
  print(consistency(axioms))
  print(maximality_consistent(axioms, theorems1))
  print(monotonicity(axioms, theorems1, theorems2))

if __name__ == "__main__":
  main()
