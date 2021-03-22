##############################################
# Publish Notes:
# 
##############################################
# Imports
import sys
import os

# Functions
def convert_local():
    return
def convert_remote():
    return
def set_env_param(paramName,defaultStr):
    param = os.getenv(paramName)
    res = defaultStr if not param else param
    return res

if __name__ == '__main__':
    try:
        # Get parameters from environment 
        local_src_dir = set_env_param('LOCAL_SOURCE_DIR','')
        local_opt_dir = set_env_param('LOCAL_OUTPUT_DIR','')
        remote_src_dir = set_env_param('REMOTE_SOURCE_DIR','')
        remote_opt_dir = set_env_param('REMOTE_OUTPUT_DIR','')
        print(" [*] Starting main")
        main()
        print(' [*] Closing application')
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)