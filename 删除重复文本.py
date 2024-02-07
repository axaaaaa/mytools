def remove_duplicates(input_file, output_file):
    # 读取输入文件，并去除重复行
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        unique_lines = set(lines)

    # 将去重后的内容写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)

if __name__ == "__main__":
    input_file = input("请输入要处理的文本文件名：")
    output_file = input("请输入保存结果的文本文件名：")
    remove_duplicates(input_file, output_file)
    print("重复文本已删除，并保存到", output_file)
