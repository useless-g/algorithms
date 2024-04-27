# https://leetcode.com/problems/freedom-trail
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        key_len = len(key)
        ring_len = len(ring)
        rings = {1: {(0, 0)}}  # 1 steps: 0 is center, 0 is key position we look for
        i = 0
        watched = set()
        while any(rings.values()):
            i += 1
            rings[i + 1] = set()
            for _ in range(len(rings[i])):
                center, key_position = rings[i].pop()
                watched.add((center, key_position))
                if ring[center] == key[key_position]:
                    if key_position + 1 == key_len:
                        return i
                    if (center, key_position + 1) not in watched:
                        rings[i + 1].add((center, key_position + 1))  # push the button

                if ((center - 1) % ring_len, key_position) not in watched:
                    rings[i + 1].add(((center - 1) % ring_len, key_position))  # go left
                if ((center + 1) % ring_len, key_position) not in watched:
                    rings[i + 1].add(((center + 1) % ring_len, key_position))  # go right


print(Solution().findRotateSteps("godding", "gd"))
