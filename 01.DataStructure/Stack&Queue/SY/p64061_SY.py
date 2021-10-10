# p64061_SY
def solution(board, moves):
    answer = 0

    # 1. board 쪼개서 바구니 만들기
    size = len(board[0])
    basket = []  # 5X5 크기의 바구니
    nums_tmp = []
    for b in board:
        for bb in b:
            nums_tmp.append(bb)  # board의 숫자가 한 줄로 쌓임
    for i in range(size):
        basket.append(nums_tmp[i::size])

    # 2. moves 실행
    stack = []
    for m in moves:
        i = 0
        while i < size:
            if basket[m-1][i] != 0:
                if len(stack) == 0:  # stack이 비어있는 경우
                    stack.append(basket[m-1][i])
                else:
                    if basket[m-1][i] == stack[-1]:
                        stack.pop(-1)
                    else:
                        stack.append(basket[m-1][i])
                basket[m-1][i] = 0
                i = size
            i += 1
    answer = stack.pop(-1)

    return answer
