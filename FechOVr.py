import subprocess
import time
import win32gui
import pyautogui

def open_and_wait(path, wait_time):
    subprocess.Popen(path)
    time.sleep(wait_time)

def close_process_by_name(process_name):
    subprocess.run(['taskkill', '/F', '/IM', process_name])

def get_top_window():
    return win32gui.GetForegroundWindow()

def click_and_type(window, x, y, text):
    win_x, win_y, win_width, win_height = win32gui.GetWindowRect(window)
    click_x, click_y = win_x + x, win_y + y
    pyautogui.click(click_x, click_y)
    time.sleep(0.5) # INCREASE IF REPLACING FOV VALUE FAILS
    pyautogui.typewrite(text)
    pyautogui.press('enter')

# FOV VALUE FROM FOV_Settings.txt - Configure within file directory
with open('FOV_Settings.txt', 'r') as file:
    FOV = float(file.read().strip())

echo_vr_path = r'C:\Program Files\Oculus\Software\Software\ready-at-dawn-echo-arena\bin\win10\echovr.exe'
print(f"{echo_vr_path} launching")
open_and_wait(echo_vr_path, 5)
echo_vr_window = get_top_window()
oculus_debug_tool_path = r'C:\Program Files\Oculus\Support\oculus-diagnostics\OculusDebugTool.exe'
print(f"{oculus_debug_tool_path} launching")
print(f"Oculus Debug Tool Delay Activated")
open_and_wait(oculus_debug_tool_path, 0.5)
oculus_debug_tool_window = get_top_window()
print("Clicking on position")
print("Replacing FOV values")
click_and_type(oculus_debug_tool_window, 275, 168, f"{FOV}; {FOV}")
print(f"Changed FOV Value To {FOV}")
close_process_by_name('echovr.exe')
close_process_by_name('OculusDebugTool.exe')
print("All tasks terminated")
time.sleep(2)
print("Re-launching Echo VR")
subprocess.run([r'explorer', echo_vr_path], shell=True)
print("YIPEE!")
print("Contact @MilkyBoiVR on Discord if errors = true :)")
