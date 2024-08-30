from pdb import main

def count(t):
    total_number_of_words = t.split()
    return len(total_number_of_words)

def sorted_list(dict):
    return dict[0]

def print_letter_count(counting_letters):
    #convert dictionary to a list of tupels  
    new_sorted_list=list(counting_letters.items())
    #sorted that list based on the key part of the list in an ascending order
    new_sorted_list.sort(reverse=True,key=sorted_list)    
    #iterate through the list 
    for key, value in new_sorted_list:
        print(f"The {key} character was found {value} times.\n")

def counting_char(text):
    #initialise an empty dictionary
    num_letters = {}
    #convert an entire text to lower case
    lower_text_case = text.lower()  
    #check whether each character is an alphabet
    #if that character is already added to the dictionary, then increment the count by one
    #otherwise start counting the iteration from one
    for char in lower_text_case:
        if char.isalpha():
            if char in num_letters:
                num_letters[char] += 1
            else:
                num_letters[char] = 1

    print_letter_count(num_letters)


def main():

    file_path = "books/frankenstein.txt"
    with open(file_path, 'r') as f:
    #reads the file frankenstein
        file_contents = f.read()
    #prints the word count of the text
        print(file_contents)
        number_words = count(file_contents)
    #word count
        print("\n--- Begin report of books/frankenstein.txt ---")
        print(f"{number_words} words found in the document\n")
    #counting number of occurrences of each letter
        counting_char(file_contents)
    #end the report
        print("\n--- End report ---")

if __name__ == "__main__":
    main()
