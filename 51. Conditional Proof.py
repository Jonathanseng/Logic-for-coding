def conditional_proof(premises, goal):
  """Prints the conditional proof for the premises and goal."""
  
  # Check if the premises and goal are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  if not re.match(r"(A|E)I|O", goal):
    return None
  
  # Initialize the proof.
  proof = []
  
  # Add the premises to the proof.
  for premise in premises:
    proof.append(premise)
  
  # Try to prove the goal using the rules of inference.
  while goal not in proof:
    for rule in ["Modus Ponens", "Modus Tollens", "Contradiction", "Simplification", "Conjunction", "Addition", "Double Negation", "Tautology", "De Morgan's I", "De Morgan's II", "Commutation", "Associativity", "Distribution"]:
      if rule == "Modus Ponens":
        if proof[-1] == "P implies Q" and "P" in proof:
          proof.append("Q")
      elif rule == "Modus Tollens":
        if proof[-1] == "P implies Q" and "not Q" in proof:
          proof.append("not P")
      elif rule == "Contradiction":
        if "P" in proof and "not P" in proof:
          proof.append("True")
      elif rule == "Simplification":
        if proof[-1] == "P and Q":
          proof.append("P")
      elif rule == "Conjunction":
        if "P" in proof and "Q" in proof:
          proof.append("P and Q")
      elif rule == "Addition":
        if "P" in proof:
          proof.append("P or Q")
        elif "Q" in proof:
          proof.append("P or Q")
      elif rule == "Double Negation":
        if proof[-1] == "not not P":
          proof.append("P")
      elif rule == "Tautology":
        if proof[-1] == "P or not P":
          proof.append("True")
      elif rule == "De Morgan's I":
        if proof[-1] == "not (P or Q)":
          proof.append("not P and not Q")
      elif rule == "De Morgan's II":
        if proof[-1] == "not (P and Q)":
          proof.append("not P or not Q")
      elif rule == "Commutation":
        if proof[-1] == "P or Q":
          proof.append("Q or P")
      elif rule == "Associativity":
        if proof[-1] == "(P or Q) or R":
          proof.append("P or (Q or R)")
        elif proof[-1] == "(P and Q) and R":
          proof.append("(P and R) and Q")
        elif proof[-1] == "P or (Q and R)":
          proof.append("(P or Q) and R")
  
  # Print the proof.
  print("Proof:")
  for line in proof:
    print(line)

def main():
  premises = ["P implies Q", "P", "Therefore, Q"]
  goal = "Q"
  conditional_proof(premises, goal)

if __name__ == "__main__":
  main()
