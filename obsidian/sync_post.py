import os
import shutil

# Paths
source_dir = "C:/Users/qpt/Documents/Obsidian Vault/posts"
destination_dir = "./content/blogs"

# Ensure destination directory exists
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)


# Sync function
def sync_directories(src, dest):
    # Copy files and directories
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

    # Delete files and directories in destination that are not in source
    for item in os.listdir(dest):
        dest_path = os.path.join(dest, item)
        src_path = os.path.join(src, item)

        if not os.path.exists(src_path):
            if os.path.isdir(dest_path):
                shutil.rmtree(dest_path)
            else:
                os.remove(dest_path)


# Perform sync
sync_directories(source_dir, destination_dir)

print("Directories synced successfully.")
