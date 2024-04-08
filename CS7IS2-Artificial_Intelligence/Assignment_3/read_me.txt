AI_Games_Project/
│
├── tic_tac_toe/
│   ├── __init__.py
│   ├── game.py              # Tic Tac Toe 游戏逻辑
│   ├── minimax.py           # Minimax 算法实现，针对 Tic Tac Toe
│   └── q_learning.py        # Q-Learning 算法实现，针对 Tic Tac Toe
│
├── connect_4/
│   ├── __init__.py
│   ├── game.py              # Connect 4 游戏逻辑
│   ├── minimax.py           # Minimax 算法实现，针对 Connect 4
│   └── q_learning.py        # Q-Learning 算法实现，针对 Connect 4
│
├── opponents/
│   ├── __init__.py
│   ├── tic_tac_toe_opponent.py  # Tic Tac Toe 的默认对手实现
│   └── connect_4_opponent.py    # Connect 4 的默认对手实现
│
├── utils/
│   ├── __init__.py
│   └── common_functions.py      # 可能被游戏或算法共用的功能
│
├── tests/
│   ├── __init__.py
│   ├── test_tic_tac_toe.py
│   └── test_connect_4.py
│
├── analysis/
│   └── performance_analysis.py  # 性能分析和比较的脚本
│
└── demos/
    └── game_demos.py            # 游戏演示脚本
