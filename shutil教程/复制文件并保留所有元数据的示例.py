import os
import shutil
import stat

def copy_with_metadata(src, dst):
    # 复制文件内容和时间戳
    shutil.copy2(src, dst)

    # 获取源文件的元数据
    st = os.stat(src)
    
    # 复制文件权限
    os.chmod(dst, st.st_mode)
    
    # 复制文件所有权
    if hasattr(os, 'chown'):
        os.chown(dst, st.st_uid, st.st_gid)

    # 复制文件的访问时间和修改时间
    os.utime(dst, (st.st_atime, st.st_mtime))

# 使用示例
source_file = 'shutil教程/复制文件.py'
destination_file = 'destination.txt'
copy_with_metadata(source_file, destination_file)

print(f"File {source_file} copied to {destination_file} with all metadata preserved.")
