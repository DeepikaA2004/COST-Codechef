def can_attend_concert(X):
    total_cost = X * 4
    if total_cost <= 1000:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X for each test case
    X = int(input())
    
    # Check if they can attend the concert
    result = can_attend_concert(X)
    
    # Print the result
    print(result)
