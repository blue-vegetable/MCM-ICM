G.add_nodes_from(
    [(item[2],
             dict(type=item[2][-2], x=float(average_postion[average_postion['ID'] ==
                  item[2]].x), y=float(average_postion[average_postion['ID'] == item[2]].y)),
     (item[3],
            dict(type=item[3][-2], x=float(average_postion[average_postion['ID'] == item[3]].x), y=float(average_postion[average_postion['ID'] == item[3]].y))])
