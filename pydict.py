dict_file = "dict.txt"

def create_dictionary():
    try:
        with open(dict_file, "w") as file:
            print("Dictionary file created successfully.")
    except Exception as e:
        print(f"Cannot create dictionary file: {str(e)}")

def add_word_meaning():
    word = input("Enter a word: ").strip().lower()
    meaning = input("Enter its meaning: ").strip()
    
    try:
        with open(dict_file, "a") as file:
            file.write(f"{word}: {meaning}\n")
        print("Word Meaning added successfully.")
    except Exception as e:
        print(f"Cannot add word meaning: {str(e)}")

def search_word_meaning():
    search_word = input("Enter a word to search for its meaning: ").strip().lower()
    
    try:
        with open(dict_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                word, meaning = line.strip().split(": ", 1)
                if word == search_word:
                    print(f"Meaning of {word}: {meaning}")
                    return
            print(f"{search_word} not found in the dictionary.")
    except Exception as e:
        print(f"Error searching for word: {str(e)}")

def remove_word_meaning():
    remove_word = input("Enter a word to remove from the dictionary: ").strip().lower()
    
    try:
        with open(dict_file, "r") as file:
            lines = file.readlines()
        with open(dict_file, "w") as file:
            removed = False
            for line in lines:
                word, _ = line.strip().split(": ", 1)
                if word != remove_word:
                    file.write(line)
                else:
                    removed = True
            if removed:
                print(f"{remove_word} and its meaning removed from the dictionary.")
            else:
                print(f"{remove_word} not found in the dictionary.")
    except Exception as e:
        print(f"Error removing word: {str(e)}")

def main():
    print("Welcome to the BugsMirror Dictionary Tool!\n ~Shivam Shukla \U0001f600")
    
    while True:
        print("\nOptions:")
        print("1. Create Dictionary")
        print("2. Add Word-Meaning Pair")
        print("3. Search Word Meaning")
        print("4. Remove Word-Meaning Pair")
        print("5. Quit")
        
        choice = input("Enter your choice (1 or 2 or 3 or 4 or 5): ").strip()
        
        if choice == "1":
            create_dictionary()
        elif choice == "2":
            add_word_meaning()
        elif choice == "3":
            search_word_meaning()
        elif choice == "4":
            remove_word_meaning()
        elif choice == "5":
            print("Quit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
