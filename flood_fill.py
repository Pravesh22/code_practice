"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-18
"""
from typing import List


# 733. Flood Fill
# For question please go through this link https://leetcode.com/problems/flood-fill/
class Solution:

    def process(self, image: List[List[int]], sr: int, sc: int, color: int, rows: int, cols: int, source: int):
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
            return
        elif source != image[sr][sc]:
            return
        image[sr][sc] = color
        self.process(image, sr - 1, sc, color, rows, cols, source)
        self.process(image, sr + 1, sc, color, rows, cols, source)
        self.process(image, sr, sc - 1, color, rows, cols, source)
        self.process(image, sr, sc + 1, color, rows, cols, source)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        cols = len(image[0])
        rows = len(image)
        source = image[sr][sc]
        self.process(image, sr, sc, color, rows, cols, source)
        return image


if __name__ == '__main__':
    solution = Solution()
    _image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    _sr = 1
    _sc = 1
    _color = 2
    result = solution.floodFill(_image, _sr, _sc, _color)
    print(result)
