#!/usr/bin/python3
def remove_char_at(srt, n):
    if n < 0 or n >= len(srt):
        return srt
    return srt[:n] + srt[n+1:]
