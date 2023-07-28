def is_valid_proof_predicate(proof):
  """Returns True if proof is a valid proof, False otherwise."""
  if not isinstance(proof, list):
    return False
  for step in proof:
    if step not in ["premise", "inference", "conclusion"]:
      return False
  for i in range(len(proof) - 1):
    if proof[i] == "premise" and proof[i + 1] == "inference" and proof[i + 2] == "conclusion":
      if proof[i + 1] != "P(x)" or proof[i] != "x = 1":
        return False
  return True

def main():
  proof = ["premise", "inference", "P(x)", "premise", "inference", "x = 1", "inference", "P(1)"]
  print(is_valid_proof_predicate(proof))

if __name__ == "__main__":
  main()
