import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)    #Splits the line into two parts: word and count using the tab character, 1 means split only once
    
    try:                
        count = int(count)       #Tries to convert the count string to an integer
    except ValueError:           #If it fails (bad input format), it skips that line
        continue
    
    if current_word == word:
        current_count += count   #If we're still on the same word as the previous line, increment the count.

    else:
        if current_word:
            print(f"{current_word}\t{current_count}")      #If the word changes, print the final count of the previous word
        current_word = word     #Reset current_word and current_count for the new word

        current_count = count

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")