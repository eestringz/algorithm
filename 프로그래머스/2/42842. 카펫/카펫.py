def solution(brown, yellow):
    r = ((brown - 4) + (((4 - brown) ** 2 - 16 * yellow) ** 0.5)) / 4
    c = yellow / r

    return [r + 2, c + 2]