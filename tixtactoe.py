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
        pass
    # 첫 플레이어 선택
    def select_first_player(self):
        pass
    # 기호 표시
    def mark_spot(self, row, col, player):
        pass
    # 승리 상태 확인    
    def is_win(self, player):
        pass
    #잔여 빈칸 여부 확인
    def is_board_full(self):
        pass
    # 플레이어 변경
    def next_player(self, player):
        pass
    # 현재 게임판 상태 출력
    def show_board(self):
        pass
    # 게임 시작
    def start(self):
        pass


# 게임 생성

#게임 시작