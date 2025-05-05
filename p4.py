import sys  # to read from a nd write to standard input/output
from io import StringIO  # Simulates input/output streams in memory

#reads each line (a student and score), calculates the grade, and emits (name, grade)
def mapper():    
    for line in sys.stdin:
        line = line.strip()   # removes leading/trailing whitespace
        if not line:          # Skips empty lines
            continue
        parts = line.split()   # Splits the line by spaces
        if len(parts) != 2:    # Expects two parts (e.g., Alice 87). If not, skip
            continue
        name, score = parts    # extract name and score
        score = float(score)   
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'F'
        print(f"{name}\t{grade}")   # Emits a key-value output

# reducer does nothing just prints what it receives
# the job is just assigning and showing grades — no grouping or aggregation needed.
def reducer():
    for line in sys.stdin:
        print(line.strip())

def main():
    print("Enter student name and score separated by space (Press Enter without input to stop):")
    input_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        input_lines.append(line)

    # Prepare mapper input
    sys.stdin = StringIO("\n".join(input_lines))  # Redirects sys.stdin to simulate input to the mapper
    mapper_output = StringIO()   # Redirects sys.stdout so we can capture the mapper's output

    # Run Mapper
    print("\nRunning Mapper...")
    sys.stdout = mapper_output  # Redirects sys.stdout so we can capture the mapper's output
    mapper()
    
    # Prepare reducer input
    sys.stdin = StringIO(mapper_output.getvalue())   # Sets mapper output as input to the reducer
    sys.stdout = sys.__stdout__    # Restores normal stdout

    # Run Reducer
    print("\nRunning Reducer...")
    reducer()

if __name__ == "__main__":
    main()