def first(n, lst):
    if len(lst) < n:
        return lst
    else:
        return lst[:n]


def rateStack(stack):
    sums = [
        sum(map(lambda x : len(x), 
                _getAscendingSequences(stack.stack.copy())
            )), 
        sum(map(lambda x : len(x), 
                _getDescendingSequences(stack.stack.copy())
            ))
        ]
    return max(sums)+(0.2*min(sums))


def _getAscendingSequences(numbers, n=[], numbers_copy=[]):
    sequences = []
    current_sequence = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_sequence.append(numbers[i])
        else:
            sequences.append(current_sequence)
            current_sequence = [numbers[i]]
    sequences.append(current_sequence)

    del current_sequence, i

    returnObj = []
    for sequence in sequences:
        valid=True
        sequenceGap = list(range(min(sequence), max(sequence)+1))
        for i in sequence:sequenceGap.remove(i)
        for i in sequenceGap:
            if i in numbers or i in n:
                valid = False
                break
        if valid:
            returnObj.append(sequence)
        else:
            new_n = numbers_copy+numbers
            for j in sequence: new_n.remove(j)
            sequence.insert(_getInsertIndex(sequence, i), -1)
            returnObj += _getAscendingSequences(sequence, new_n, numbers)

    for i in range(len(returnObj)):
        returnObj[i] = list(filter(lambda x: x != -1 ,returnObj[i]))
    return [lst for lst in returnObj if len(lst) > 1]


def _getDescendingSequences(numbers):
    numbers.reverse()
    listreverse = _getAscendingSequences(numbers)
    for i in listreverse:i.reverse()
    return listreverse


def _getInsertIndex(l, number):
    for i in range(len(l)-1):
        if(l[i]<number<l[i+1]): return i+1
