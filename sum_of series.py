def SeriesSum(n):
    sum_of_series = 0
    for i in range(1, n + 1):
        sum_of_series += i

    print("The sum of the series is:", sum_of_series)


n = int(input("Enter a positive integer: "))
SeriesSum(n)
