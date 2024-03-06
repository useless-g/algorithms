# from pprint import pprint

board = [list(input().strip()) for _ in range(8)]
answer = [[0 for _ in range(8)] for _ in range(8)]
# pprint(board)

for i in range(8):
    for j in range(8):
        if board[i][j] == "R":
            answer[i][j] = 1
            for ii in range(i + 1, 8):
                if board[ii][j] == "*":
                    answer[ii][j] = 1
                else:
                    break
            for ii in range(i - 1, -1, -1):
                if board[ii][j] == "*":
                    answer[ii][j] = 1
                else:
                    break
            for jj in range(j + 1, 8):
                if board[i][jj] == "*":
                    answer[i][jj] = 1
                else:
                    break
            for jj in range(j - 1, -1, -1):
                if board[i][jj] == "*":
                    answer[i][jj] = 1
                else:
                    break
        elif board[i][j] == "B":
            answer[i][j] = 1
            for ii, jj in zip(range(i - 1, -1, -1), range(j-1, -1, -1)):
                if board[ii][jj] == "*":
                    answer[ii][jj] = 1
                else:
                    break
            for ii, jj in zip(range(i-1, -1, -1), range(j + 1, 8)):
                if board[ii][jj] == "*":
                    answer[ii][jj] = 1
                else:
                    break
            for ii, jj in zip(range(i+1, 8), range(j + 1, 8)):
                if board[ii][jj] == "*":
                    answer[ii][jj] = 1
                else:
                    break
            for ii, jj in zip(range(i+1, 8), range(j - 1, -1, -1)):
                if board[ii][jj] == "*":
                    answer[ii][jj] = 1
                else:
                    break

s = 0
for i in range(8):
    for j in range(8):
        s += answer[i][j]
# pprint(answer)
print(64 - s)


