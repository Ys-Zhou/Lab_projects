from dbconnector import GetCursor

with GetCursor() as cur:
    # Step 1: create similarity dict
    query = 'SELECT * FROM artsim'
    cur.execute(query)

    # [[<item>, <item>, <sim>]] -> {<item_a>: [(<item_b>, <sim>)]}
    sim_dict = dict()

    for row in cur:
        sim_dict.setdefault(row[0], []).append([row[1], row[2]])
        sim_dict.setdefault(row[1], []).append([row[0], row[2]])

    # Step 2: calculate predictions for each user
    query = 'SELECT * FROM rating ORDER BY uid'
    cur.execute(query)

    current_user = None
    known_items = None
    # pred_dict:: {<item>: [<rating_sum>, <sim_sum>]}
    pred_dict = None

    # row:: [<user>, <item_a>, <weight>]
    for row in cur:
        if row[0] != current_user:
            if current_user:
                pred_list = [[k, v[0] / v[1]] for k, v in pred_dict.items() if k not in known_items]
                pred_list.sort(key=lambda x: x[1], reverse=True)
                print(current_user)
                print(pred_list[:5])
            current_user = row[0]
            known_items = []
            pred_dict = dict()

        known_items.append(row[1])

        # pair:: [<item_b>, <sim>]
        for pair in sim_dict[row[1]]:
            pred_val = pred_dict.setdefault(pair[0], [0, 0])
            pred_val[0] += row[2] * pair[1]
            pred_val[1] += pair[1]
