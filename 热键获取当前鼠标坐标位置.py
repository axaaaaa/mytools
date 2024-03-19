import pyautogui
import pyperclip
import keyboard

def copy_mouse_position():
    # 获取当前鼠标的坐标
    x, y = pyautogui.position()
    
    # 将坐标字符串化并复制到剪切板
    position_str = f"{x},{y}"
    pyperclip.copy(position_str)
    print(f"鼠标坐标 {position_str} 已复制到剪切板。")

# 监听按键事件
keyboard.add_hotkey('1', copy_mouse_position)

# 让程序持续运行，直到按下'q'键退出
print("按下数字键盘1获取鼠标坐标并复制到剪切板，按下 'q' 键退出程序。")
keyboard.wait('q')
