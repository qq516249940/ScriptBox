import shutil,os

def restore_directory(backup_dir, restore_dir):
    # 列出备份目录下的所有备份
    backups = sorted(os.listdir(backup_dir))
    
    # 获取最新的备份
    latest_backup = backups[-1]
    latest_backup_path = os.path.join(backup_dir, latest_backup)
    
    # 恢复目录
    shutil.copytree(latest_backup_path, restore_dir)
    print(f"Restored {restore_dir} from {latest_backup_path}")

# 使用示例
restore_directory('shutil教程222', '恢复备份目录')
