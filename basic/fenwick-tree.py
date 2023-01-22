from typing import List


# 教程: https://www.bilibili.com/video/BV12a411i7rP/?spm_id_from=333.788.recommend_more_video.0

class FenwickTree:
    def __init__(self, nums: List[int]):
        self.tree = [0 for _ in range(len(nums) + 1)]

        for i, num in enumerate(nums):
            self.update(i + 1, num)

    def update(self, index: int, value: int):
        while index < len(self.tree):
            self.tree[index] += value
            print(f'self.tree={self.tree}, [index={index}], value={value}')
            print(f"before index={('000' + bin(index)[2:])[-4:]} index10={index}")
            index += (index & -index)
            print(f" after index={('000'+bin(index)[2:])[-4:]} index10={index}")
        print('**************************************************')
    def query(self, index: int):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= (index & -index)
        return total


# tree = FenwickTree([5, 2, 9, -3, 5, 20, 10, -7, 2, 3])
tree = FenwickTree([5, 2, 9, -3])
print(tree.query(3))
