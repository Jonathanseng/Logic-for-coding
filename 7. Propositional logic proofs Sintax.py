def is_valid_proof(proof):
  """Returns True if proof is a valid proof, False otherwise."""
  if not isinstance(proof, list):
    return False
  for step in proof:
    if step not in ["premise", "inference", "conclusion"]:
      return False
  for i in range(len(proof) - 1):
    if proof[i] == "inference" and proof[i + 1] != "conclusion":
      return False
  return True

def main():
  proof = ["premise", "inference", "P", "premise", "inference", "P and Q"]
  print(is_valid_proof(proof))

if __name__ == "__main__":
  main()
