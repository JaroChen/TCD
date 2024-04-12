# 性能分析和比较的脚本
import time
import tracemalloc
from Assignment_3.tic_tac_toe.game import tic_tac_toe, initialize_board, check_winner, check_draw
from Assignment_3.tic_tac_toe.game_automated import tic_tac_toe_automated


def performance_analysis(games_to_play=250):
    results = {'A_win': 0, 'B_win': 0, 'draw': 0}
    total_time = 0                            #  definite time
    total_memory = 0                          #  definite memory
    global nodes_evaluated
    total_nodes_evaluated = 0                 #  definite node (minmax search)


    tracemalloc.start()  # 开始跟踪内存分配

    for i in range(games_to_play):
        nodes_evaluated = 0  # 重置节点计数器
        start_time = time.time()  # 记录游戏开始时间
        board = initialize_board()  # 初始化棋盘
        result = tic_tac_toe_automated()  # run the game_automated


        # 1)Record results
        if result == "A wins":
            results['A_win'] += 1
        elif result == "B wins":
            results['B_win'] += 1
        elif result == "draw":
            results['draw'] += 1

        # 2)Record results and node counts
        total_nodes_evaluated += nodes_evaluated

        end_time = time.time()
        total_time += (end_time - start_time)  # 3)Accumulated Runtime

        current, peak = tracemalloc.get_traced_memory()  # 4)Getting Memory Usage Information
        tracemalloc.reset_peak()  # 重置峰值内存占用信息
        total_memory += peak  # 累加内存占用

    tracemalloc.stop()  # 停止内存跟踪

    # 打印统计结果
    print(f"Total games: {games_to_play}")
    print(f"A wins(Alpha-Beta Minmax): {results['A_win']} ({(results['A_win'] / games_to_play) * 100}%)")
    # print(f"B wins(Oppoent): {results['B_win']} ({(results['B_win'] / games_to_play) * 100}%)")
    print(f"Draws: {results['draw']} ({(results['draw'] / games_to_play) * 100}%)")
    print(f"Average time per game: {total_time / games_to_play} seconds")
    print(f"Total memory used: {total_memory / games_to_play} bytes")
    # print(f"Average nodes evaluated per game: {total_nodes_evaluated / games_to_play}")

# 5)Stability and robustness testing
def stability_and_robustness_test(games_to_play=10000):

    game_count = 0
    try:
        while game_count < games_to_play:    # 假设你有一个计数器
            tic_tac_toe_automated()  # 或任何长时间运行的代码
            game_count += 1  # 增加游戏计数
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(f"Stability and robustness testing：Completed {game_count} games without interruption.")

if __name__ == "__main__":
    performance_analysis()
    stability_and_robustness_test()

