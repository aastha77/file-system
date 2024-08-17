#!/usr/bin/env python
# coding: utf-8

# # Advance python

# # Assignment - 3

# # Assignment: File Synchronizer

# In[34]:


import os
import shutil

def synchronize_directories(source_dir, dest_dir, delete_extra=False):
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        print("Invalid source or destination directory.")
        return

    for root, _, files in os.walk(source_dir):
        for filename in files:
            src_path = os.path.join(root, filename)
            dest_path = os.path.join(dest_dir, filename)

            if os.path.exists(dest_path):
                src_mtime = os.stat(src_path).st_mtime
                dest_mtime = os.stat(dest_path).st_mtime

                if src_mtime > dest_mtime:
                    shutil.copy2(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)

    if delete_extra:
        for root, _, files in os.walk(dest_dir):
            for filename in files:
                dest_path = os.path.join(root, filename)
                src_path = os.path.join(source_dir, filename)

                if not os.path.exists(src_path):
                    os.remove(dest_path)

    print("Synchronization completed successfully!")

# Example usage
source_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
destination_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
synchronize_directories(source_directory, destination_directory, delete_extra=True)


#  The provided Python code synchronizes files between two directories by copying new or updated files from the 
# source to the destination while preserving metadata. 

# In[30]:


import os
import shutil

def synchronize_directories(source_dir, dest_dir):
    # List files in source and destination directories
    source_files = set(os.listdir(source_dir))
    dest_files = set(os.listdir(dest_dir))

    # Identify new or updated files
    new_or_updated_files = source_files - dest_files

    # Copy new or updated files to destination
    for filename in new_or_updated_files:
        src_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        shutil.copy2(src_path, dest_path)  # Use shutil.copy2 for metadata preservation


    # Print summary and confirmation
    print(f"{len(new_or_updated_files)} files copied.")
    print("Synchronization completed successfully!")

# Example usage
source_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
destination_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
synchronize_directories(source_directory, destination_directory)


# # Function Purpose:
# The synchronize_directories function takes two directory paths (source_dir and dest_dir) as input.
# It ensures that both directories exist.
# It compares file modification times between the source and destination directories.
# 
# 
# Traverse the directory tree using os.walk.
# Compare file modification times (st_mtime) to determine if a file needs updating.
# Use shutil.copy2 to copy files while preserving metadata.
# 
# Call synchronize_directories with your desired source and destination directories.

# In[32]:


import os
import shutil

def synchronize_directories(source_dir, dest_dir):
    # Validate directory paths
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        print("Invalid source or destination directory.")
        return

    # Traverse the directory tree
    for root, _, files in os.walk(source_dir):     #os.walk to traverse the directory tree and process files incrementally.
        for filename in files:
            src_path = os.path.join(root, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Check if file exists in destination
            if os.path.exists(dest_path):
                src_mtime = os.stat(src_path).st_mtime
                dest_mtime = os.stat(dest_path).st_mtime

                # Update if source file is newer
                if src_mtime > dest_mtime:
                    shutil.copy2(src_path, dest_path)
            else:
                # Copy new file to destination
                shutil.copy2(src_path, dest_path)

    print("Synchronization completed successfully!")

# Example usage
source_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
destination_directory = "C:\\Users\\DELL\\ADVANCE PYTHON"
synchronize_directories(source_directory, destination_directory)


# In[ ]:




