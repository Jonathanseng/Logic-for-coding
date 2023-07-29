def sorites(property, start, end):
  """Prints a Sorites argument."""
  
  # Print the premises of the Sorites argument.
  for i in range(start, end + 1):
    print(f"A {property} with {i} grains of sand is a heap.")
  
  # Print the conclusion of the Sorites argument.
  print(f"A {property} with 1 grain of sand is a heap.")

def main():
  sorites("grains of sand", 1, 100)

if __name__ == "__main__":
  main()
