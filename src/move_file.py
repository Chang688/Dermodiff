import os
import shutil
import re

def move_files(source_dir, dest_dir):
    # 遍历源目录下的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 源文件的路径
            if re.search(r'R1|R2', file):
                continue
            source_file_path = os.path.join(root, file)
            # 目标文件的路径，使用 os.path.basename 获取文件名
            dest_file_path = os.path.join(dest_dir, os.path.basename(file))
            try:
                # 移动文件
                shutil.move(source_file_path, dest_file_path)
                print(f"Moved {source_file_path} to {dest_file_path}")
            except Exception as e:
                print(f"Failed to move {source_file_path}: {e}")

# 源目录和目标目录的路径
source_directory = "E:/reproduction/data/PH2Dataset/PH2 Dataset images"
destination_directory = "E:/reproduction/data/PH2Dataset/images"

# 如果目标目录不存在，则创建它
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# 调用函数移动文件
move_files(source_directory, destination_directory)
