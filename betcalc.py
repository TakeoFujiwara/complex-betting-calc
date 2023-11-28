import sys

ODDSFILE = sys.argv[1]
PROFIT_RATE = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
BET_UNIT = int(sys.argv[3]) if len(sys.argv) > 3 else 100

odds = []
total_budget = 0

with open(ODDSFILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
        odds_data = line.split()
        odds.append({
            'target': odds_data[0],
            'odds': float(odds_data[1]),
            'bet': BET_UNIT,
            'back': int(float(odds_data[1]) * BET_UNIT)
        })
        total_budget += BET_UNIT

while True:
    is_completed = True
    for odds_item in odds:
        if odds_item['back'] < total_budget * PROFIT_RATE:
            odds_item['bet'] += BET_UNIT
            odds_item['back'] = int(odds_item['bet'] * odds_item['odds'])
            total_budget += BET_UNIT
            is_completed = False
        else:
            pass

        if total_budget > 100000:
            print('Too much budget')
            sys.exit(-1)

    if is_completed:
        print(f'Total Budget : {total_budget}')
        for odds_item in odds:
            print('{:<10} {:>4d} {:>6d}'.format(odds_item['target'], odds_item['bet'], odds_item['back']))
        break
