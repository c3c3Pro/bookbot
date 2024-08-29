from pdb import main

def main():

    file_path = "books/frankenstein.txt"
    with open(file_path, 'r') as f:
    #write the code here 
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()
