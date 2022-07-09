import json

if __name__ == "__main__":
    with open('./data/index.json') as f_index:
        idx = json.load(f_index)
        preds = idx['predictions']
        diff_comp = preds[-2:]

    qual_shifts = {}
    for be_af, sign in zip(diff_comp, [-1, 1]):
        with open(f"./data/{be_af}") as fin:
            pred = json.load(fin)
            its = pred['iterations']
            for team, outcomes in pred['team_outcomes'].items():
                val = qual_shifts.get(team, 0)
                qual_shifts[team] = val + sign * (outcomes['points_qual'] / its)

    print("Shifts in direct (points) qualification chances")
    for team, shift in sorted(qual_shifts.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"{team}: {int(shift * 10000)/100}%")

