# 导入pytchat库
import pytchat

# 创建一个pytchat对象，指定要获取弹幕的直播间ID
# 您可以从YouTube直播间的URL中找到这个ID
# 例如：https://www.youtube.com/watch?v=xxxxxxxxxxx
# 那么ID就是xxxxxxxxxxx
#https://www.youtube.com/watch?v=yRhl8Q4h_zI
chat = pytchat.create(video_id="yRhl8Q4h_zI")

# 循环获取并打印弹幕，直到直播结束或出现错误
while chat.is_alive():
    try:
        # 获取一批弹幕数据（默认为100条）
        data = chat.get()
        # 遍历每条弹幕数据
        for item in data.items:
            # 打印弹幕作者的昵称和内容
            print(f"{item.author.name}: {item.message}")
    except Exception as e:
        # 打印错误信息并退出循环
        print(f"Error: {e}")
        break
