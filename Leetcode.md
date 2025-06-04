# <font color="red"> 5.26 </font>

##  274: H_index
Input: citations = [3,0,6,1,5]
Output: 3
```
range(start, stop, step)
```
# <font color="red"> 5.27 </font>
## 135: candy (greedy 左右双遍历)
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
## Roman
列表 ([])： 强调顺序和通过数字索引访问。
字典 ({})： 强调键-值映射和通过键访问。
集合 ({})： 强调唯一性和快速成员检测。
“键”是离散符号／非整数 → 用 dict. roman_map = {'I':1, 'V':5, …}  
“键”是连续整数范围 → 优先用列表／数组
            [
                (1000, "M"),  # 元组：第一个元素是整数 1000，第二个元素是字符串 "M"
                (900,  "CM"), # 元组：900 → "CM"
            ]

# Reverse Words 列表
    print(my_string[::-1])  # 输出: olleh (字符串反转)
    class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return -1
        
        w = s.split()
        w.reverse()
        output = []

        for i in range(len(w)):
            output.append(w[i])
        return " ".join(output)

# 209 Minimum Size Subarray Sum:

"Minimum Size Subarray Sum" 题目中的数组 nums 不保证是排序的，而且它要求的是连续子数组，这通常需要使用**滑动窗口（Sliding Window）**算法，而不是从两端向中间靠拢的双指针。
并非所有滑动窗口问题都需要将结果变量初始化为 float('inf')。这取决于你要找的是什么：

寻找“最大”值：如果你要寻找最大长度、最大和、最大数量等，那么你应该将存储最大值的变量初始化为 0 或 float('-inf')（负无穷大），以确保任何正向结果都能被记录下来。


# Foundation         
1. 可以用逗号分隔：print("Output:", i) 2.或者用 f-string:print(f"Output: {i}")
   append()是Python中列表（list）的一个方法，用于在列表末尾添加新的元素。
