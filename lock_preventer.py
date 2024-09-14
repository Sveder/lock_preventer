import time
import win32api
import win32con
from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


SLEEP_TIME = 60 * 4


def is_sound_playing():
    # Get all active audio sessions
    sessions = AudioUtilities.GetAllSessions()
    
    # Check if any audio session is currently playing
    for session in sessions:
        if session.State == 1:  # 1 means the session is active
            return True
    
    return False


def prevent_lock():
    # Send F15 key up to prevent lock
    win32api.keybd_event(win32con.VK_F15, 0, win32con.KEYEVENTF_KEYUP, 0)


def main():
    while True:
        if is_sound_playing():
            print("Sound is currently playing")
            prevent_lock()
        else:
            print("No sound is playing")
        
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
