import os
import shutil

def separate_files(source_dir, dest_dir_lesion, dest_dir_normal):
    # 确保目标目录存在
    if not os.path.exists(dest_dir_lesion):
        os.makedirs(dest_dir_lesion)
    if not os.path.exists(dest_dir_normal):
        os.makedirs(dest_dir_normal)

    # 遍历源目录下的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 文件的路径
            file_path = os.path.join(root, file)
            # 如果文件名包含 "lesion"，则移动到包含 "lesion" 的目录
            if "lesion" in file:
                shutil.move(file_path, dest_dir_lesion)
                print(f"Moved {file_path} to {dest_dir_lesion}")
            # 否则移动到不包含 "lesion" 的目录
            else:
                shutil.move(file_path, dest_dir_normal)
                print(f"Moved {file_path} to {dest_dir_normal}")

# 源目录和目标目录的路径
source_directory = "E:/reproduction/data/PH2Dataset/images"
dest_directory_lesion = "E:/reproduction/data/PH2Dataset/image"
dest_directory_normal = "E:/reproduction/data/PH2Dataset/mask"

# 调用函数分离文件
separate_files(source_directory, dest_directory_lesion, dest_directory_normal)
