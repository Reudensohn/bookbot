def main():
    #liest das buch und gibt es aus
    with open("/home/reudensohn/workspace/github.com/reudensohn/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #teilt die wörter und zählt sie. gibt sie aus
        words = list(file_contents.split())
        #print(len(words))
        #zählt die buchstaben und gibt ihre anzahl einzeln aus
        alphabet = {}
        for letter in file_contents:
            lowercase_letter = letter.lower()
            if lowercase_letter.isalpha():
                alphabet[lowercase_letter] = alphabet.get(letter, 0) + 1
        #print(alphabet)
        #gibt einen schönen report aus
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} found in the document")
        print("")
        for letters in alphabet:
            print(f"the {letters} character was found {alphabet[letters]} times")
        print("--- End report ---")
main()