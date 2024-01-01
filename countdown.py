import time
import ctypes
import os

from tkinter import simpledialog

def get_user_input():
    video_path = simpledialog.askstring("", "Video path:")

    hour = simpledialog.askstring("", "Hour:")
    minute = simpledialog.askstring("", "Minute:")
    second = simpledialog.askstring("", "Second:")

    if video_path:
        os.startfile(video_path)
        ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0x20, 0, 0x2, 0)

    if hour and minute and second:
        return abs(int(hour)), abs(int(minute)), abs(int(second))
    else: return -1, 0, 0
    

if __name__ == '__main__':
    start_hour, start_min, start_sec = get_user_input()
    if start_hour == -1: exit()
    print(f'Will press spacebar at {start_hour}:{start_min}:{start_sec}')

    before_sec = -1

    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        if minute == start_min and hour == start_hour and second == start_sec:
            ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x20, 0, 0x2, 0)
            break

        if before_sec != second:
            print(f'{hour}:{minute}:{second}')
            before_sec = second