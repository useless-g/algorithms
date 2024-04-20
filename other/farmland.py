class Solution:
    def findFarmland(self, land):
        rows, cols = len(land), len(land[0])
        result = []
        for i in range(rows):
            for j in range(cols):
                if land[i][j]:
                    result.append([])
                    result[-1].append(i)
                    result[-1].append(j)

                    ii = i
                    while ii < rows and land[ii][j]:
                        ii += 1
                    ii -= 1

                    jj = j
                    while jj < cols and land[ii][jj]:
                        jj += 1
                    jj -= 1

                    result[-1].append(ii)
                    result[-1].append(jj)

                    for i_ in range(i, ii + 1):
                        for j_ in range(j, jj + 1):
                            land[i_][j_] = 0
        print(land)
        return result

print(Solution().findFarmland([[1,0,0],[0,1,1],[0,1,1]]))