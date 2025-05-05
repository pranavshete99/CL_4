import sys
from io import StringIO     #Used to simulate input/output streams  

# Define matrix dimensions
m = 2  # i: 1 to m (row of A)
n = 2  # k: 1 to n (columns of A / rows of B)
p = 2  # j: 1 to p (column of B)

def mapper():
    for line in sys.stdin:
        line = line.strip()     #strip() removes whitespace or newline characters
        matrix, i, j, value = line.split("\t")   #Splits the line into components, matrix will be either "A" or "B"
        i, j, value = int(i), int(j), float(value)    #Parses row (i), column (j), and value

        if matrix == "A":
            for k in range(1, p + 1):  # p columns in B
                print(f"{i}\t{k}\tA\t{j}\t{value}")

        #For each A[i][j], it contributes to all columns k in the result matrix, so emit:
        # Key: (i, k)
        # Tag: 'A'
        # j: index from A
        # value: value from A

        elif matrix == "B":
            for k in range(1, m + 1):  # m rows in A
                print(f"{k}\t{j}\tB\t{i}\t{value}")

def reducer():
    A_elements = {}    #Sets up storage for values from matrices A and B, grouped by (i, j)
    B_elements = {}

    for line in sys.stdin:
        line = line.strip()
        i, j, matrix, k, value = line.split("\t")    #Each line has keys (i, j) and a matrix tag 'A' or 'B', index k, and value
        i, j, k, value = int(i), int(j), int(k), float(value)   #Parses the mapper’s output

        if matrix == "A":
            if (i, j) not in A_elements:
                A_elements[(i, j)] = {}
            A_elements[(i, j)][k] = value
        # For each result matrix cell (i, j), stores all A and B values it needs:
        # A contributes A[i][k]
        # B contributes B[k][j]
        # Stored using k as intermediate index

        elif matrix == "B":
            if (i, j) not in B_elements:
                B_elements[(i, j)] = {}
            B_elements[(i, j)][k] = value

    for i in range(1, m + 1):          #Loops over every cell (i, j) in result matrix C
        for j in range(1, p + 1):
            result = 0
            for k in range(1, n + 1):        #For each cell C[i][j], loops over all k = 1 to n
                a_val = A_elements.get((i, k), {}).get(k, 0)     #gets: A[i][k] from A_elements[(i,k)] and
                b_val = B_elements.get((k, j), {}).get(k, 0)     #    :B[k][j] from B_elements[(k,j)]
                result += a_val * b_val             #Multiplies and adds to result
            print(f"{i}\t{j}\t{result}")

def main():
    input_data = [
        "A\t1\t1\t1.0",
        "A\t1\t2\t2.0",
        "A\t2\t1\t3.0",
        "A\t2\t2\t4.0",
        "B\t1\t1\t5.0",
        "B\t1\t2\t6.0",
        "B\t2\t1\t7.0",
        "B\t2\t2\t8.0"
    ]

    # Simulate mapper  
    # Feeds input to the mapper().
    # Redirects output to mapper_output
    sys.stdin = StringIO("\n".join(input_data))
    mapper_output = StringIO()
    sys.stdout = mapper_output
    mapper()

    # Simulate reducer
    #Feeds mapper output to reducer()
    #prunts final result
    sys.stdin = StringIO(mapper_output.getvalue())
    sys.stdout = sys.__stdout__
    reducer()

if __name__ == "__main__":
    main()