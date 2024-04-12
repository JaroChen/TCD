import time
import tracemalloc
from Assignment_3.tic_tac_toe.game_q_automated import TicTacToe

def performance_analysis(games_to_play=250):
    results = {'A_win': 0, 'B_win': 0, 'draw': 0}
    total_time = 0
    total_memory = 0

    tracemalloc.start()  # 开始跟踪内存分配

    for _ in range(games_to_play):
        game = TicTacToe()  # 初始化游戏
        start_time = time.time()  # 记录游戏开始时间
        game.play_game()  # 开始游戏

        # 记录结果
        if game.current_player == 'A' and game.check_winner():
            results['A_win'] += 1
        elif game.current_player == 'B' and game.check_winner():
            results['B_win'] += 1
        elif game.check_draw():
            results['draw'] += 1

        end_time = time.time()
        total_time += (end_time - start_time)  # 累计运行时间

        current, peak = tracemalloc.get_traced_memory()  # 获取内存占用信息
        tracemalloc.reset_peak()  # 重置峰值内存占用信息
        total_memory += peak  # 累加内存占用

    tracemalloc.stop()  # 停止内存跟踪

    # 打印统计结果
    print(f"Total games: {games_to_play}")
    print(f"A wins: {results['A_win']} ({(results['A_win'] / games_to_play) * 100}%)")
    print(f"B wins: {results['B_win']} ({(results['B_win'] / games_to_play) * 100}%)")
    print(f"Draws: {results['draw']} ({(results['draw'] / games_to_play) * 100}%)")
    print(f"Average time per game: {total_time / games_to_play} seconds")
    print(f"Total memory used: {total_memory / games_to_play} bytes")

if __name__ == "__main__":
    performance_analysis()
