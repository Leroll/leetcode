class Solution(object):
    '''
    给定 m 个数组，每个数组都已经按照升序排好序了。
    现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。
    你的任务就是去找到最大距离

    示例 1：

    输入： 
    [[1,2,3],
    [4,5],
    [1,2,3]]
    输出： 4
    解释：
    一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
    

    注意：

    每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
    所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
    m 个数组中所有整数的范围在 [-10000, 10000] 内。
    '''
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_first, min_second = [10001, -1],[10001, -1]
        max_first, max_second = [-10001, -1],[-10001, -1]

        for idx, a in enumerate(arrays):
            if a[0] < min_first[0]:
                min_second = [min_first[0], min_first[1]]
                min_first = [a[0], idx]
            elif a[0] < min_second[0]:
                min_second = [a[0], idx]

            if a[-1] > max_first[0]:
                max_second = [max_first[0], max_first[1]]
                max_first = [a[-1], idx]
            elif a[-1] > max_second[0]:
                max_second = [a[-1], idx]

        if min_first[1] != max_first[1]:
            result = abs(min_first[0]-max_first[0])
        else:
            temp_1 = abs(min_first[0] - max_second[0])
            temp_2 = abs(min_second[0] - max_first[0])
            result = temp_1 if (temp_1 > temp_2) else temp_2 
        return result
    

if __name__ == '__main__':
    
    test_cases = [
        [[1,5], [3,4]]  # ans: 2
        
    ]  

    for test in test_cases:
        print(Solution().maxDistance(test))