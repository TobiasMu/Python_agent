# %%
import os

def get_files_info(working_directory, directory=None):
    if os.path.isdir(working_directory) is not True:
      return f"{working_directory} is not a directory"

    try:
        path_to_dir = os.path.join(working_directory, directory)
    except Exception as e:
        return e

    if os.path.isdir(path_to_dir) is not True:
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    print(path_to_dir)

    return "what"
# %%
get_files_info("test","testdirr" )
