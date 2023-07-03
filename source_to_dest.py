"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-07
"""
from typing import List

"""
Given the list of edges(source, target), find the order of each node.
Example: [{source:"a", target:"b"}, {source:"b", target:"c"}, {source:"b", target:"d"}, {source:"c", target: "e"}]
Output: {a: 1, b: 2, c: 3, d: 3, e: 4}
"""


def solution(data: List[dict]):
    for d in data:
        pass
    return "hi"


if __name__ == '__main__':
    _data = [{"source": "a", "target": "b"}, {"source": "b", "target": "c"}, {"source": "b", "target": "d"},
              {"source": "c", "target": "e"}]
    result = solution(_data)
    print(result)
