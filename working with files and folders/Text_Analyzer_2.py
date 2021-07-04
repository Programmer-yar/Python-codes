                   #Opening multiple files
def count_words(file_name):
    """Counts number of words"""
    try:
        with open(file_name) as file:
            alice_file=file.read()
            
    except FileNotFoundError:
        print("Pllease enter correct file path/name")

    else:
        """Counts approximate number of words"""
        alice_word=alice_file.lower().count('alice')
        print("the word 'alice' occured",alice_word,"times")
        
        alice_word_1=alice_file.lower().count('the')
        print("\nthe word 'the' occured",alice_word_1,"times")
        
        alice_words=alice_file.split()
        print("\nthe approximate words in", file_name, "are", len(alice_words))


file_1="C:\\Users\\Ahmad Yar\\Desktop\\pi.txt"
file_name='alice.txt'
count_words(file_1)
count_words(file_name)

                  #Failing silently
file_2='new file.txt'
try:
    with open(file_2) as file:
        store=file.read()

except FileNotFoundError:
    pass

else:
    store_words=store.split()
    print("\nthe approximate words in", file_2, "are", len(alice_words))
