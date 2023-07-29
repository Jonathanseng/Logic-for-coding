def thought_sense_reference(word, thought, sense, reference):
    if word == thought:
        return "The word and the thought are identical."
    elif word == sense:
        return "The word and the sense are identical."
    elif word == reference:
        return "The word and the reference are identical."
    else:
        return "The word, the thought, and the reference are distinct."


def main():
    print(thought_sense_reference("dog", "dog", "dog", "dog"))
    print(thought_sense_reference("dog", "the concept of a dog", "a four-legged mammal", "a specific dog named Spot"))
    print(thought_sense_reference("dog", "the word 'dog'", "a four-legged mammal", "a specific dog named Spot"))


if __name__ == "__main__":
    main()
