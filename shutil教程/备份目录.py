import shutil
import datetime

def backup_directory(source_dir, backup_dir):
    # 创建带有时间戳的备份目录名
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f"{backup_dir}/backup_{timestamp}"
    
    # 复制目录
    shutil.copytree(source_dir, backup_name)
    print(f"Backup of {source_dir} created at {backup_name}")

# 使用示例
backup_directory('shutil教程', 'shutil教程222')
