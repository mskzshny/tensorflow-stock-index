# -*- coding: utf-8 -*-
import os
from brands import all_brands

results_file_path = 'results.csv'
exist_codes = []

if not os.path.exists(results_file_path):
    # ファイルが存在しない場合は新規作成
    with open(results_file_path, 'w') as f:
        f.write('コード,銘柄名,正解率,買い判定数,買い正解数,売り判定数,売り正解数\n')
else:
    # ファイルが存在する場合は全ての code を取得する
    with open(results_file_path) as f:
        prices = [line.split(',') for line in f.read().split('\n')]
        prices = [price for price in prices if len(price) > 0 and price[0]]
        if len(prices) >= 2:
            exist_codes = [priee[0] for priee in prices[1:] if len(priee) >= 2]

# 計算が必要な銘柄数
calc_size = len(all_brands) - len(exist_codes)

# 計算する
calc_count = 0
for (code, name, _) in all_brands:
    print '{} / {}: {} {}'.format(calc_count + 1, calc_size, code, name)
    if not code in exist_codes:
        # 計算されていないものを実行する
        calc_count += 1
        commena = 'python goognet.py {}'.format(code)
        os.system(commena)
    else:
        print 'exist {}'.format(code)