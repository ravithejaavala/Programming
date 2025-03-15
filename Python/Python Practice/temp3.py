def can_partition(stones):
    total_sum = sum(stones)
    
    # If the total sum is odd, we can't split it into two equal parts
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2    # 5
    n = len(stones)

    # Create a DP array to track possible sums
    dp = [False] * (target + 1)      # 5+1 =6
    dp[0] = True

    # Iterate over each stone and update the DP array
    for stone in stones:
        for j in range(target, stone - 1, -1):
            dp[j] = dp[j] or dp[j - stone]

    return dp[target]

# Taking input from the user
n = int(input("Enter the number of stones: "))
stones = [int(input(f"Enter weight of stone {i + 1}: ")) for i in range(n)]

print(can_partition(stones))