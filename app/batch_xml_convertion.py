##############################################
# Publish Notes:
# 
##############################################
# Imports
import sys
import os

# XML Structure Class

####################################################################
##### REF: https://code.activestate.com/recipes/410469-xml-as-dictionary/
import cElementTree as ElementTree

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})
####################################################################


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
            tree = ET.parse(f)
            root = tree.getroot(root)
            
            dr = XmlDictConfig()
            
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