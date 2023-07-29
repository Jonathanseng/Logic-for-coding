import re

def rules_and_fallacies():
  """Prints a list of rules and fallacies."""
  
  # Define the rules and fallacies.
  rules = ["All A are B.", "No A are B.", "Some A are B.", "Some A are not B."]
  fallacies = ["Ad hominem", "Appeal to authority", "Bandwagon fallacy", "False dichotomy", "Straw man fallacy"]
  
  # Print the rules and fallacies.
  print("Rules:")
  for rule in rules:
    print(rule)
  print("\nFallacies:")
  for fallacy in fallacies:
    print(fallacy)

def main():
  rules_and_fallacies()

if __name__ == "__main__":
  main()
