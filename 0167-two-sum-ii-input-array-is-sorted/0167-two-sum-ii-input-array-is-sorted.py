class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                j = numbers.index(target - numbers[i])
                if i!=j:
                    res.append(i+1)
                    res.append(j+1)
                    return sorted(res)
        