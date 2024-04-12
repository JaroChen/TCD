import time
import tracemalloc
from Assignment_3.connect_4.game_automated import connect_four_automated, initialize_board

def performance_analysis(games_to_play=1):
    results = {'A_win': 0, 'B_win': 0, 'draw': 0}
    total_time = 0
    total_memory = 0

    tracemalloc.start()  # 开始跟踪内存分配

    for i in range(games_to_play):
        start_time = time.time()  # 记录游戏开始时间
        board = initialize_board()  # 初始化棋盘
        result = connect_four_automated()  # 运行游戏自动化

        if result == "A wins":
            results['A_win'] += 1
        elif result == "B wins":
            results['B_win'] += 1
        elif result == "draw":
            results['draw'] += 1

        end_time = time.time()
        total_time += (end_time - start_time)  # 累加运行时间

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

def stability_and_robustness_test(games_to_play=10000):
    game_count = 0
    try:
        while game_count < games_to_play:
            connect_four_automated()  # 运行游戏
            game_count += 1
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(f"Stability and robustness testing：Completed {game_count} games without interruption.")

if __name__ == "__main__":
    performance_analysis()
    stability_and_robustness_test()
