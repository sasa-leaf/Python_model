def luck():
    from fortune import get_fortune as gf
    score = gf()
    print('今日の運勢は… ',str(score))