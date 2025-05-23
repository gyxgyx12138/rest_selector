import random
def select_rest_option():
    rest_options = [
        "打飞机",
        "晒太阳",
        "收缩盆底肌",
        "听听音乐",
        "闭眼冥想",
        "抽烟（如果有烟的话）",
        "看看帅哥图片"
    ]
    
    selected_option = random.choice(rest_options)
    print(f"今天你的休息方式是：{selected_option}")

if __name__ == "__main__":
    select_rest_option()