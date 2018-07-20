from dbconnector import GetCursor

with GetCursor() as cur:
    # Step 1: create rating dict
    query = 'SELECT * FROM rating'
    cur.execute(query)

    # [[<user>, <item>, <weight>]] -> {<user>: [[<item>, <weight>]]}
    rating_dict = dict()

    for row in cur:
        rating_dict.setdefault(row[0], []).append(row[1:3])

    # Step 2: calculate predictions for each user
    query = ('SELECT usera, userb, sim FROM usersim UNION '
             'SELECT userb, usera, sim FROM usersim ORDER BY usera')
    cur.execute(query)

    # MAE values
    mae_sum = 0
    mae_num = 0

    current_user = None
    known_items = None
    # pred_dict:: {<item>: [<rating_sum>, <sim_sum>]}
    pred_dict = None

    # row:: [<user_a>, <user_b>, <sim>]
    for row in cur:
        if row[0] != current_user:
            if current_user:
                # Calculate MAE
                for cor in rating_dict[current_user]:
                    if cor[0] in pred_dict:
                        pred_pair = pred_dict[cor[0]]
                        mae_sum += abs(cor[1] - pred_pair[0] / pred_pair[1])
                        mae_num += 1
                print(current_user)
                print(mae_sum / mae_num)
            current_user = row[0]
            pred_dict = dict()
            known_items = list(zip(*rating_dict[row[0]]))[0]

        # pair:: [<item>, <weight>]
        for pair in rating_dict[row[1]]:
            if pair[0] in known_items:
                pred_val = pred_dict.setdefault(pair[0], [0, 0])
                pred_val[0] += row[2] * pair[1]
                pred_val[1] += row[2]
