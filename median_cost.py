def median_cost(arr, n, d) -> int:
    mu = (n-1)//2+1 + d
    sum1 = 0
    sum2 = 0

    for i in range(1,mu):
        sum1 += arr[i-1]

    for i in range(mu, (n)+1):
        sum2 += arr[i-1]

    total_sum = sum2- sum1 + (-1 + 2*d) * arr[mu-1]
    return total_sum

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    d = 2
    cost = median_cost(arr, n, d)
    print("Total cost with distance " + str(d) + " is: " + str(cost))
