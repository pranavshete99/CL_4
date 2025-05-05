import sys     #used to access command-line arguments and read from standard input.

# Pass the target word as an argument (optional)
target_word = sys.argv[1].lower() if len(sys.argv) > 1 else None
# sys.argv[1]: Takes the target word from the command line.
# .lower(): Converts it to lowercase to make the matching case-insensitive.
# If no word is passed, target_word becomes None

if not target_word:
    print("Error: No target word specified.", file=sys.stderr)
    sys.exit(1)

for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    # Convert line to lowercase
    line = line.lower()
    # Split the line into words
    words = line.split()
    # Emit (target_word, 1) only if target word is found

    for word in words:
        if word == target_word:
            print(f"{target_word}\t1")



# to run execute: type input.txt | python mapper.py hello | sort | python reducer.py