def getInversions(arr, n):
    # Write your code here.
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            if i < j and arr[i] > arr[j]:
                ans.append([arr[i], arr[j]])
    return len(ans)


print(getInversions([3, 2, 1], 3))
