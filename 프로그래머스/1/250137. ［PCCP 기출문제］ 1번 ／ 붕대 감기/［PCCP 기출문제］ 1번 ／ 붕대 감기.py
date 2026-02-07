def solution(bandage, health, attacks):
    t, x, y = bandage
    cur = health
    prev = 0          # 직전 공격 시간
    success = 0        # 연속 성공 시간

    for at, dmg in attacks:
        delta = at - prev - 1  # 공격 사이에 회복 가능한 초 수

        if delta > 0:
            total = success + delta
            cur += delta * x + (total // t) * y
            cur = min(health, cur)
            success = total % t

        # 공격 받는 순간
        cur -= dmg
        if cur <= 0:
            return -1

        prev = at
        success = 0  # 공격으로 연속 성공 끊김

    return cur