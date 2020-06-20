def solution(board, moves):
    answer = 0
    count = 0
    basket = []
    for integer in moves:
        for i in board:
            if(i[integer-1] == 0 ):
                print("empty")
            else:
                basket.append(i[integer-1])
                i[integer-1]=0
                print("moved")
                if len(basket)>1:
                    if basket[-1] == basket[-2]:
                        print(basket[-1],basket[-2])
                        basket.pop()
                        basket.pop()                        
                        print("deleted")
                        count += 2
                break
    answer = count
        # for i in range(len(board)):
        #     # print(i)
        #     for j in range(len(board[i])):
        #         print(board[i][j])            
    return answer