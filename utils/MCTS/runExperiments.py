# utils/MCTS/runExperiments.py
from collections import Counter
import random
from utils.MCTS.simulateGame import simulate_game
import time
from typing import Dict, Any

def run_experiments(sims: int,
                    c: float,
                    N: int = 1000,
                    starter: str = 'both'
                   ) -> Dict[str, Any]:
    stats = Counter()
    cost_accum = 0
    t0 = time.time()

    for i in range(N):
        if starter == 'X':
            sp = 'X'
        elif starter == 'O':
            sp = 'O'
        else:
            sp = 'X' if random.random() < 0.5 else 'O'

        result, cost = simulate_game(sims, c, sp)
        stats[result] += 1
        cost_accum += cost

    elapsed = time.time() - t0

    return {
        'wins_X': stats[+1],
        'draws': stats[0],
        'wins_O': stats[-1],
        'avg_cost': cost_accum / N,
        'avg_time_s': elapsed / N
    }