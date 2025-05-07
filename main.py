# compare_algorithms.py

from utils.minimaxNormal.runExperimients import run_experiments as run_mm
from utils.alphaBetaPruning.runExperiments import run_experiments as run_ab
from utils.MCTS.runExperiments             import run_experiments as run_mc

def main():
    # Definimos nuestras 6 variantes:
    experiments = [
        # ('V1', run_mm, {'depth': 3}),
        # ('V2', run_mm, {'depth': 5}),
        # ('V3', run_ab, {'depth': 3}),
        # ('V4', run_ab, {'depth': 5}),
        ('V5', run_mc, {'sims': 200, 'c': 1.0}),
        ('V6', run_mc, {'sims': 500, 'c': 1.414}),
    ]

    results = []
    for tag, fn, params in experiments:
        for starter in ['X', 'O']:
            # Ejecutamos N=1000 partidas alternando (o fijando) quién empieza
            res = fn(**params, N=1000, starter=starter)
            results.append({
                'Var':        tag,
                'Algoritmo':  fn.__module__.split('.')[-2],  # minimaxNormal | alphaBetaPruning | MCTS
                'Starter':    starter,
                **params,
                'Vict_X':     res['wins_X'],
                'Empates':    res['draws'],
                'Vict_O':     res['wins_O'],
                'Costo_avg':  f"{res['avg_cost']:.1f}",
                'Tiempo_avg': f"{res['avg_time_s']:.3f}s"
            })

    # Cabecera de la tabla Markdown
    header = (
        "| Var | Algoritmo   | Parámetros         | Starter | Vict_X | Empates | Vict_O | Costo_avg | Tiempo_avg |\n"
        "|:---:|:------------|:-------------------|:--------|-------:|--------:|-------:|----------:|-----------:|\n"
    )

    lines = [header]
    
    # Filas
    for r in results:
        # Construimos la columna Parámetros
        if 'depth' in r:
            p = f"k={r['depth']}"
        else:
            p = f"sims={r['sims']}, C={r['c']}"
        line = (
            f"| {r['Var']} "
            f"| {r['Algoritmo']:<12} "
            f"| {p:<17} "
            f"| {r['Starter']:^6} "
            f"| {r['Vict_X']:>6} "
            f"| {r['Empates']:>7} "
            f"| {r['Vict_O']:>6} "
            f"| {r['Costo_avg']:>9} "
            f"| {r['Tiempo_avg']:>10} |"
        )
        lines.append(line + "\n")

    with open("results.md", "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    main()
