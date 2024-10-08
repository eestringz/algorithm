def solution(sizes):
    maxWeight, maxHeight = 1,1
    for w, h in sizes:
        larger, smaller = [w, h] if w > h else [h, w]
        maxWeight = max(maxWeight, larger)
        maxHeight = max(maxHeight, smaller)

    return maxWeight * maxHeight
