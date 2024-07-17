import os
import shutil

def copy_with_metadata(src, dst):
    if os.path.isdir(src):
        # 创建目标目录
        if not os.path.exists(dst):
            os.makedirs(dst)
        # 复制目录元数据
        shutil.copystat(src, dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            copy_with_metadata(s, d)
    else:
        # 复制文件内容和元数据
        shutil.copy2(src, dst)
        st = os.stat(src)
        os.chmod(dst, st.st_mode)
        if hasattr(os, 'chown'):
            os.chown(dst, st.st_uid, st.st_gid)
        os.utime(dst, (st.st_atime, st.st_mtime))

# 使用示例
source_directory = 'shutil教程'
destination_directory = 'destination_directory'
copy_with_metadata(source_directory, destination_directory)

print(f"Directory {source_directory} copied to {destination_directory} with all metadata preserved.")
