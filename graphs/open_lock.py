# https://leetcode.com/problems/open-the-lock
class Solution:
    def openLock(self, deadends, target) -> int:
        target = tuple(map(int, list(target)))
        deadends = set(list(map(lambda x: tuple(map(int, list(x))), deadends)))
        if target in deadends:
            return -1
        # print(deadends)
        locks = {0: {(0, 0, 0, 0)}}
        i = -1
        watched = set()
        while any(locks.values()):
            i += 1
            locks[i + 1] = set()
            for _ in range(len(locks[i])):
                lock = locks[i].pop()
                if lock in deadends:
                    continue
                if lock == target:
                    return i
                watched.add(lock)

                if ((lock[0] + 1) % 10, lock[1], lock[2], lock[3]) not in watched:
                    locks[i + 1].add(((lock[0] + 1) % 10, lock[1], lock[2], lock[3]))
                if ((lock[0] - 1) % 10, lock[1], lock[2], lock[3]) not in watched:
                    locks[i + 1].add(((lock[0] - 1) % 10, lock[1], lock[2], lock[3]))
                if (lock[0], (lock[1] + 1) % 10, lock[2], lock[3]) not in watched:
                    locks[i + 1].add((lock[0], (lock[1] + 1) % 10, lock[2], lock[3]))
                if (lock[0], (lock[1] - 1) % 10, lock[2], lock[3]) not in watched:
                    locks[i + 1].add((lock[0], (lock[1] - 1) % 10, lock[2], lock[3]))
                if (lock[0], lock[1], (lock[2] + 1) % 10, lock[3]) not in watched:
                    locks[i + 1].add((lock[0], lock[1], (lock[2] + 1) % 10, lock[3]))
                if (lock[0], lock[1], (lock[2] - 1) % 10, lock[3]) not in watched:
                    locks[i + 1].add((lock[0], lock[1], (lock[2] - 1) % 10, lock[3]))
                if (lock[0], lock[1], lock[2], (lock[3] + 1) % 10) not in watched:
                    locks[i + 1].add((lock[0], lock[1], lock[2], (lock[3] + 1) % 10))
                if (lock[0], lock[1], lock[2], (lock[3] - 1) % 10) not in watched:
                    locks[i + 1].add((lock[0], lock[1], lock[2], (lock[3] - 1) % 10))
        return -1


print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
print(Solution().openLock(["8888"], "0009"))
print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
