def chess(N, M, board):

    chess_w = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
    ]
    chess_b = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
    ]

    min_repaint = float('inf')
    for i in range(N - 7):
        for j in range(M - 7):
            repaint_w, repaint_b = 0, 0
            for x in range(8):
                for y in range(8):
                    if board[i + x][j + y] != chess_w[x][y]:
                        repaint_w += 1
                    if board[i + x][j + y] != chess_b[x][y]:
                        repaint_b += 1
            
            min_repaint = min(min_repaint, repaint_b, repaint_w)

    return min_repaint

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

print(chess(N, M, board))
