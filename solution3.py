def solution(N):
    alphabet = 'abcdefghijklmno'
    alphabet_length = len(alphabet)
    result = ""

    for i in range(N):
        result += alphabet[i % alphabet_length]

    return result

# Test cases
print(solution(3))   # Output: "abc"
print(solution(5))   # Output: "abcde"
print(solution(30))  # Output: "abcdefghijklmnoabcdefghijklmno"
