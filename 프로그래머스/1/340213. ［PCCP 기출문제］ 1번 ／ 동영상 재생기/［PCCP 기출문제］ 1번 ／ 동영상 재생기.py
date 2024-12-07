def time_to_seconds(t):
    return int(t[:2]) * 60 + int(t[3:])

def seconds_to_time(s):
    return f"{s // 60:02}:{s % 60:02}"


def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for i in range(len(commands)):
        if pos >= op_start and pos <= op_end:
            pos = op_end

        if commands[i] == "prev":  # 10초 전으로 이동
            pos = max(0, pos - 10)
        elif commands[i] == "next":  # 10초 후로 이동
            pos = min(video_len, pos + 10)
    
    if pos >= op_start and pos <= op_end:
            pos = op_end

    return seconds_to_time(pos)
