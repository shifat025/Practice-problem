def generate_door_mat(N, M):
    # Calculate the middle row index
    middle_index = N // 2

    # Generate the top part
    for i in range(middle_index):
        # Calculate number of patterns and dashes
        num_patterns = 2 * i + 1
        num_dashes = (M - 3 * num_patterns) // 2
        # Create the row
        row = '-' * num_dashes + '.|.' * num_patterns + '-' * num_dashes
        print(row)
    
    # Print the middle row with "WELCOME"
    print('WELCOME'.center(M, '-'))

    # Generate the bottom part (mirror of the top part)
    for i in range(middle_index - 1, -1, -1):
        # Calculate number of patterns and dashes
        num_patterns = 2 * i + 1
        num_dashes = (M - 3 * num_patterns) // 2
        # Create the row
        row = '-' * num_dashes + '.|.' * num_patterns + '-' * num_dashes
        print(row)

# Sample input
N, M = map(int, input().split())
generate_door_mat(N, M)
