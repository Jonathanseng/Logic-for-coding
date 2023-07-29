import matplotlib.pyplot as plt
import matplotlib_venn as venn

def venn_diagram(subsets, set_labels):
  """Creates a Venn diagram."""
  
  # Create the figure.
  fig = plt.figure(figsize=(10, 10))
  
  # Create the Venn diagram.
  ax = venn.venn2(subsets=subsets, set_labels=set_labels, alpha=0.5)
  
  # Show the figure.
  plt.show()

def main():
  # Create the subsets.
  subsets = (10, 20, 15)
  
  # Create the set labels.
  set_labels = ("A", "B")
  
  # Create the Venn diagram.
  venn_diagram(subsets, set_labels)

if __name__ == "__main__":
  main()
