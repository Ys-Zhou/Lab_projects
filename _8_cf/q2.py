from dbconnector import GetCursor

with GetCursor() as cur:
    # Step 1: create similarity dict
    query = 'SELECT * FROM artsim'
    cur.execute(query)

    # [[<item>, <item>, <sim>]] -> {<item_a>: [[<item_b>, <sim>]]}
    sim_dict = dict()

    for row in cur:
        sim_dict.setdefault(row[0], []).append(row[1:3])
        sim_dict.setdefault(row[1], []).append([row[0], row[2]])

    # Step 2: calculate predictions for each user
    query = 'SELECT * FROM rating ORDER BY uid'
    cur.execute(query)

    # MAE values
    mae_sum = 0
    mae_num = 0

    current_user = None
    known_items = None
    # pred_dict:: {<item>: [<rating_sum>, <sim_sum>]}
    pred_dict = None

    # row:: [<user>, <item_a>, <weight>]
    for row in cur:
        if row[0] != current_user:
            if current_user:
                # Calculate MAE
                for cor in known_items:
                    if cor[0] in pred_dict:
                        pred_pair = pred_dict[cor[0]]
                        mae_sum += abs(cor[1] - pred_pair[0] / pred_pair[1])
                        mae_num += 1
                print(current_user)
                print(mae_sum / mae_num)
            current_user = row[0]
            known_items = []
            pred_dict = dict()

        known_items.append(row[1:3])

        if row[1] in sim_dict:
            # pair:: [<item_b>, <sim>]
            for pair in sim_dict[row[1]]:
                pred_val = pred_dict.setdefault(pair[0], [0, 0])
                pred_val[0] += row[2] * pair[1]
                pred_val[1] += pair[1]
