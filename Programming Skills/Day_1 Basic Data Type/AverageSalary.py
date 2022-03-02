class Solution:
    def average(self, salary) -> float:
        min, max = 1000000, 0
        sum = 0
        for i in salary:
            if i < min:
                min = i
            elif i > max:
                max = i
            sum += i
        return (sum-max-min)/(len(salary)-2)