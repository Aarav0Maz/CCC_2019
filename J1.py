def ScoreCalculator(A0, A9, A8, B7, B6, B5):
    apple_score = A0 * 3 + A9 * 2 + A8 * 1

    banana_score =  B7 * 3 +  B6 * 2 + B5 * 1

    if apple_score > banana_score:
        return "A"
    elif apple_score == banana_score:
        return "T"
    elif apple_score < banana_score:
        return "B"


def main():
    A1 = int(input().strip())
    A2 = int(input().strip())
    A3 = int(input().strip())    

    B1 = int(input().strip())
    B2 = int(input().strip())
    B3 = int(input().strip())

    winner = ScoreCalculator(A1, A2, A3, B1, B2, B3)
    print(winner)





if __name__ == "__main__":
    main()