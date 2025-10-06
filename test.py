from itertools import combinations as cb

dice_index_combi = tuple(cb(range(10), 5))
print(len(dice_index_combi))


def get_dice_result_index(length):
    seq, result = [], []
    def find():
        if len(seq) == length:
            result.append(seq.copy())
            return
        for i in range(0, 6):
            seq.append(i)
            find()
            seq.pop()
    find()
    return result

print(len(get_dice_result_index(5)))