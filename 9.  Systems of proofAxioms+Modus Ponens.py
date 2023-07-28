def is_valid_proof_mp(proof):
  """Returns True if proof is a valid proof using Modus Ponens, False otherwise."""
  if not isinstance(proof, list):
    return False
  for step in proof:
    if step not in ["premise", "inference", "conclusion"]:
      return False
  for i in range(len(proof) - 1):
    if proof[i] == "premise" and proof[i + 1] == "inference" and proof[i + 2] == "conclusion":
      if proof[i + 1] != "P implies Q" or proof[i] != "P":
        return False
  return True

def main():
  proof = ["premise", "inference", "P implies Q", "premise", "inference", "P", "inference", "Q"]
  print(is_valid_proof_mp(proof))

if __name__ == "__main__":
  main()
