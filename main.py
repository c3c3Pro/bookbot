from pdb import main

def count(t):
    total_number_of_words = t.split()
    return len(total_number_of_words)

def main():

    file_path = "books/frankenstein.txt"
    with open(file_path, 'r') as f:
    #reads the file frankenstein
        file_contents = f.read()
        print(file_contents)
        number_words = count(file_contents)
        print(f"total number of words: {number_words}")

if __name__ == "__main__":
    main()
