from dbconnector import GetCursor

with GetCursor() as cur:
    # Create rating_dict
    query = 'SELECT * FROM rating'
    cur.execute(query)

    # [[<user>, <item>, <weight>]] -> {<user>: [(<item>, <weight>)]}
    rating_dict = dict()
    for row in cur:
        rating_dict.setdefault(row[0], []).append(row[1:3])


def upred(user_a: int, rec_limit: int) -> list:
    # known items
    known_tuple = list(zip(*rating_dict[user_a]))[0]

    # pred_dict:: {<item>: [<rating_sum>, <sim_sum>]}
    pred_dict = dict()

    with GetCursor() as cur1:
        query1 = ('SELECT userb, sim FROM usersim WHERE usera = %d UNION '
                  'SELECT usera, sim FROM usersim WHERE userb = %d') % (user_a, user_a)
        cur1.execute(query1)

        # row1:: [<user_b>, <sim>]
        for row1 in cur1:
            # pair:: [<item>, <weight>]
            for pair in rating_dict[row1[0]]:
                if pair[0] not in known_tuple:
                    pred_list = pred_dict.setdefault(pair[0], [0, 0])
                    pred_list[0] += row1[1] * pair[1]
                    pred_list[1] += row1[1]

    pred_list = [[k, v[0] / v[1]] for k, v in pred_dict.items()]
    pred_list.sort(key=lambda x: x[1], reverse=True)
    return pred_list[:rec_limit]


for user in rating_dict.keys():
    print(user)
    print(upred(user, 5))
