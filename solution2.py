def solution(A):
    # Dictionary to store numbers based on their digit sum
    digit_sum_dict = {}

    # Variable to store the maximum sum
    max_sum = -1

    # Iterate through the array
    for num in A:
        # Calculate digit sum for the current number
        current_sum = sum(int(digit) for digit in str(num))

        # Check if there's a number with the same digit sum in the dictionary
        if current_sum in digit_sum_dict:
            # Update the maximum sum if needed
            max_sum = max(max_sum, num + digit_sum_dict[current_sum])

        # Update the dictionary with the current number
        digit_sum_dict[current_sum] = max(digit_sum_dict.get(current_sum, 0), num)

    return max_sum

# Examples
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))  # Output: 102
print(solution([51, 32, 43]))  # Output: -1
