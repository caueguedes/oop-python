def tally():
    score = 0
    while True:
        increment = yield score
        score += increment


white_sox = tally()
blue_jays = tally()

next(white_sox)  # 0
next(blue_jays)  # 0

white_sox.send(3)  # 3
blue_jays.send(2)  # 2

white_sox.send(2)  # 5
blue_jays.send(4)  # 6