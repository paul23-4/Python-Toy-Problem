def solution(A):
    n = len(A)
    target = 10
    total_moves = 0
    
    for i in range(n-1):
        diff = A[i] - target
        
        if diff > 0:
            A[i] -= diff
            A[i+1] += diff
            total_moves += diff
        
        elif diff < 0:
            diff = abs(diff)
            if diff > A[i+1]:
                return -1
            A[i] += diff
            A[i+1] -= diff
            total_moves += diff
    
    if A[-1] != target:
        return -1
    
    return total_moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
