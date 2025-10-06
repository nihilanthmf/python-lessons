def check_winners(scores, student_score):
    scores = sorted(scores)
    for i in range(len(scores)):
        if scores[i] == student_score and i >= len(scores) - 3:
            print("Вы в тройке победителей!")
            return
    print("Вы не попали в тройку победителей.")

check_winners([1, 2,3,4,5,6,7], 5)
        