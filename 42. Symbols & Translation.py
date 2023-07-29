def symbols_and_translation():
  """Prints a list of symbols and their translations."""
  
  # Define the symbols and their translations.
  symbols = {
    "∀": "All",
    "∃": "Some",
    "→": "implies",
    "↔": "iff",
    "∨": "or",
    "∧": "and",
    "¬": "not",
  }
  
  # Print the symbols and their translations.
  for symbol, translation in symbols.items():
    print(f"{symbol}: {translation}")

def main():
  symbols_and_translation()

if __name__ == "__main__":
  main()
