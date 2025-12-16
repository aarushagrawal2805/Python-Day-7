import os

def rename_file(old_filename, new_filename):
    if not os.path.exists(old_filename):
        return f"Error: File not found."
    try:
        os.rename(old_filename, new_filename)
        return f"Successfully renamed '{old_filename}' to '{new_filename}'."
    except Exception as e:
        return f"An error occurred while renaming: {e}"

old_name = "Sample.txt"
new_name = "File1.txt"
na=rename_file(old_name,new_name)
print(na)