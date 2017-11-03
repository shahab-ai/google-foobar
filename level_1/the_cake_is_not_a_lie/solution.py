def answer(s):
    PossibleNumOfPieces = []
    for n in range(len(s)):
        NumOfPieces = n + 1
        PossibleNumOfPieces.append(NumOfPieces)
        PieceSize = len(s)/(NumOfPieces)
        sub = s[:PieceSize]
        for i in range(NumOfPieces - 1):
            if s.find(sub, (i+1)*PieceSize, (i+2)*PieceSize) == -1:
                PossibleNumOfPieces.pop()
                break
    return max(PossibleNumOfPieces)
