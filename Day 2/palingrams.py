"""Load a text file as a list.
   Arguments:
   -text file name (and directory path, if needed)
   Exceptions:
   -IOError if filename not found.
   Returns:
   -A list of all words in a text file in lower case.
   Requires-import sys
   """
import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e,file),file = sys.stderr)
        sys.exit(1)

def main():
    word_list = set(load('Day 2/dictionary.txt'))
    palingrame_list = []
    #palindrome_word = [x for x in word_list if x[::-1] == x]
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end>1:
            for i in range(end):
                if word[i:]==rev_word[:end-i] and rev_word[end-i:] in word_list:
                    palingrame_list.append((word,rev_word[end-i:]))
                if word[:i]==rev_word[end-i:] and rev_word[:end-i] in word_list:
                    palingrame_list.append((rev_word[:end-i],word))

    palingrams_sorted = sorted(palingrame_list)
    #print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
    #for first, second in palingrams_sorted: print("{} {}".format(first, second))
if __name__ == "__main__":
    main()