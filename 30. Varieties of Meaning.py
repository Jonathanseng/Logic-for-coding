def varieties_of_meaning(sentence):
  """
  This function takes a sentence as input and returns a list of the different
  varieties of meaning that the sentence can have.

  The different varieties of meaning are:
    * Denotation: The literal meaning of the sentence.
    * Connotation: The implied meaning of the sentence.
    * Illocutionary force: The purpose of the sentence.
    * Pragmatic meaning: The meaning of the sentence in context.

  Args:
    sentence: The sentence to be analyzed.

  Returns:
    A list of the different varieties of meaning that the sentence can have.
  """

  denotation = sentence
  connotation = ""
  illocutionary_force = ""
  pragmatic_meaning = ""

  # Denotation

  denotation = sentence.split(".")[0]

  # Connotation

  for word in sentence.split(" "):
    if word in ["good", "bad", "beautiful", "ugly"]:
      connotation = connotation + " " + word

  # Illocutionary force

  if sentence.endswith("?"):
    illocutionary_force = "Question"
  elif sentence.endswith("!"):
    illocutionary_force = "Command"
  else:
    illocutionary_force = "Statement"

  # Pragmatic meaning

  if sentence.startswith("I"):
    pragmatic_meaning = "Self-referential"
  else:
    pragmatic_meaning = "Addressee-directed"

  return [denotation, connotation, illocutionary_force, pragmatic_meaning]

sentence = "I think that you are beautiful."

print(varieties_of_meaning(sentence))
