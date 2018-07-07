from dbconnector import GetCursor

with GetCursor() as cur:
    # Step 1: create rating dict
    query = 'SELECT * FROM rating'
    cur.execute(query)

    # [[<user>, <item>, <weight>]] -> {<user>: [(<item>, <weight>)]}
    rating_dict = dict()

    for row in cur:
        rating_dict.setdefault(row[0], []).append(row[1:3])

    # Step 2: calculate predictions for each user
    query = ('SELECT usera, userb, sim FROM usersim UNION '
             'SELECT userb, usera, sim FROM usersim ORDER BY usera')
    cur.execute(query)

    current_user = None
    known_items = None
    # pred_dict:: {<item>: [<rating_sum>, <sim_sum>]}
    pred_dict = None

    # row:: [<user_a>, <user_b>, <sim>]
    for row in cur:
        if row[0] != current_user:
            if current_user:
                pred_list = [[k, v[0] / v[1]] for k, v in pred_dict.items()]
                pred_list.sort(key=lambda x: x[1], reverse=True)
                print(current_user)
                print(pred_list[:5])
            current_user = row[0]
            pred_dict = dict()
            known_items = list(zip(*rating_dict[row[0]]))[0]

        # pair:: [<item>, <weight>]
        for pair in rating_dict[row[1]]:
            if pair[0] not in known_items:
                pred_val = pred_dict.setdefault(pair[0], [0, 0])
                pred_val[0] += row[2] * pair[1]
                pred_val[1] += row[2]
