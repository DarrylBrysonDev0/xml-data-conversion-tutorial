##############################################
# Publish Notes:
# 
##############################################
# Imports
import sys
import os

# XML Structure Class
## class represents the structure and handler methods
class Xml_Parser:
    def __init__(self):
        self.ResultAr = []
        return

# Functions
def convert_local_dir(source_dir: str, target_dir: str) -> None:
    # Get list of files to convert
    # For each file
    data = convert_file_to_obj(source_dir)
    ## Validate structure
    ## Apply class
    ## Filter field
    return
def convert_remote_dir(source_dir: str, target_dir: str, conn_dict: dict) -> None:
    # Connect to sftp server
    # Get list of files to convert
    # For each file
    # Download file locally
    return
def convert_file_to_obj(conv_f):
    try:
        with open(conv_f) as f:
            data = json.load(f)
            producer.send(topic,value=data)
            # print(str(msg_file))
            msg_cnt+=1
    except Exception as err:
        print()
        print("An error occurred while reading file {0}".format(fo))
        print(str(err))
        traceback.print_tb(err.__traceback__)
    return res
def set_env_param(paramName,defaultStr):
    param = os.getenv(paramName)
    res = defaultStr if not param else param
    return res

if __name__ == '__main__':
    try:
        # Get parameters from environment 
        local_src_dir = set_env_param('LOCAL_SOURCE_DIR','')
        local_opt_dir = set_env_param('LOCAL_OUTPUT_DIR','')

        # SFTP connection details 
        sftp_address = set_env_param('SFTP_HOST_ADDRESS','')
        sftp_usr = set_env_param('SFTP_USER','')
        sftp_pwd = set_env_param('SFTP_PASSWORD','')
        sftp_conn_dict = {
            'host'=sftp_address
            ,'usr'=sftp_usr
            ,'pwd'=sftp_pwd
        }

        remote_src_dir = set_env_param('REMOTE_SOURCE_DIR','')
        remote_opt_dir = set_env_param('REMOTE_OUTPUT_DIR','')

        # Convert local directory of xml files
        convert_local(local_src_dir,local_opt_dir)

        # Convert remote directory of xml files
        convert_remote(remote_src_dir,remote_opt_dir, sftp_conn_dict)
        print(" [*] Starting main")
        main()
        print(' [*] Closing application')
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)