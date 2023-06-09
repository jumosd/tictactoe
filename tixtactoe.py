import random


class Tic_Tac_Toe:
 
    # 게임판 생성
    def __init__(self):
        self.board = []

    # 게임판 초기화
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
            self.board.append(row)
            
    # 첫 플레이어 선택
    def select_first_player(self):
        if random.randint(0,1) == 0 :
            return "X"
        else:
            return "O"
        
    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row][col] = player
        
    # 승리 상태 확인    
    def is_win(self, player):
        
        n = len(self.board) # 2차원 보드의 갯수를 샘
        
        #행확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win == True:
                return win
            
        #열확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win
            
        #대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win
        

        return False

    #잔여 빈칸 여부 확인
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True
        
    # 플레이어 변경
    def next_player(self, player):
        if player == 'O':
            return 'X'
        else :
            return 'O'
    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end =" ")
            print()
    # 게임 시작
    def start(self):
        #게임판 만들기
        self.create_board()
        # 게임판 보여주기
        self.show_board()
       
        #플레이어 만들기
        player = self.select_first_player()

        while True:
            # 플레이어 설정
            if player == "X":
                print("컴퓨터 차례입니다.")
            else :
                print("사용자 차례입니다.")
            # 게임판 보여주기
            self.show_board()

            # 사용자 입력대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == "X" :
                #randint메소드는 1~3까지 로 입력한다 
                #0을 제와한이유는 사용자와 동일하게 하기위함이다
                while True:
                    row = random.randint(1,3)
                    col = random.randint(1,3)
                    if self.board[row -1][col -1] == "*":
                        break
                print("컴퓨터가 행"+str(row)+", 열"+str(col)+ "을/를 선택했습니다.")
                print()

            else:
                row,col =  list(map(int,input("선택한 위치를 입력하세요").split(" ")))
                print("사용자가 행"+str(row)+", 열"+str(col)+ " 을/를 선택했습니다.")
                print()
            
            # row, col 입력값이 0,0 인경우 게임 종료
            if row == 0 and col == 0 :
                break
            
            # 입력된 위치표시
            self.mark_spot(row -1, col -1, player)
            self.show_board()

            # 현재 플레이어가 이겼는지 확인
            if self.is_win(player) == True :
                if player == 'X':
                    print("컴퓨터가 이겼습니다.")
                else :
                    print("사용자가 이겼습니다.")
                break

            #게임판 가득찼는지 확인
            if self.is_board_full() ==True:
                print("무승부 입니다.")
                break

            #플레이어 변경
            player = self.next_player(player)

        print()
        self.show_board()

TTT = Tic_Tac_Toe()

TTT.start()
