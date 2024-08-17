Q1) Find the Power of K-Size Subarrays-I
( BiWeekly contest - 137 )

Approach - 1

```
> n = len(nums)
> res = []
> 
> for i in range(n-k+1):
>     flag = True
> 
>     for j in range(i, i+k-1):
>         if nums[j] + 1 != nums[j+1]:
>             flag = False
>             break
> 
>     if flag:
>         res.append(max(nums[i:i+k]))
>     else:
>         res.append(-1)
> return res
```

Approach-2

```
n = len(nums)
res = []

for i in range(n-k+1):
    subarray = nums[i:i+k]

    if all(subarray[j] + 1 == subarray[j+1] for j in range(k - 1)):
        res.append(max(subarray))
    else:
        res.append(-1)
return res
```
