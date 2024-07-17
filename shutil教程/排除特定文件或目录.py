import shutil
import fnmatch

def ignore_files(dir, files):
    # 定义要忽略的模式
    ignore_patterns = ['file2.txt', 'dir2', '*复制*.py']
    ignore_list = []
    for pattern in ignore_patterns:
        ignore_list.extend(fnmatch.filter(files, pattern))
    return ignore_list

source_dir = 'shutil教程'
destination_dir = 'shutil教程222'

shutil.copytree(source_dir, destination_dir, ignore=ignore_files)

print("Directory copied with specified files and directories ignored.")
