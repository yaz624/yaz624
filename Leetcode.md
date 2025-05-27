<font color="red"> 5.26 </font>

##  274: H_index
Input: citations = [3,0,6,1,5]
Output: 3
```
range(start, stop, step)
```
## 135: candy
有几个n孩子站成一排。每个孩子都被分配了一个整数数组中的评分值ratings。您将根据以下要求向这些孩子分发糖果：
1. 每个孩子必须至少有一颗糖果。
2. 评分较高的孩子比邻居的孩子获得更多的糖果。
```
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
   
        i = 1
   
        # pivot
        for i in range(n):
            if ratings[i] > ratings [i-1]:
                left[i] = left[i-1] + 1

        for i in range(n-2,-1,-1)
            if ratings[i] > ratings[i+1]
                right[i] = right[i-1] + 1
        total = 0
        for i in range(n):
            total += max(left[i], right [i])
        return total
```
