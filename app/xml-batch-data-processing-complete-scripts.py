# imports
import xml.etree.ElementTree as ET
import uuid
import pandas as pd
import glob

# Parsing class
class Xml_Parser:
    def __init__(self):
        self.ResultAr = []
        return
    def parse_datafiles(self,file_id,rootElem):
        res = []
        for data_file in rootElem.findall('DataFile'):
            file_ar = self.parse_file(data_file)
            res += file_ar
        return res
    def parse_file(self, data_file):
        
        file_ar = []
        m_id = data_file.find('machine_id').text
        test_id = data_file.find('test_id').text
        tech_id = data_file.find('technician').text
        test_routine = data_file.find('test_routine').text
        batched = data_file.find('batched').text
        
        header_ar = [m_id, test_id, tech_id, test_routine, batched]
        
        loc_ar = self.parse_measurement_location(data_file, 'loc_1')
        file_ar.append(header_ar + loc_ar)
        
        loc_ar = self.parse_measurement_location(data_file, 'loc_2')
        file_ar.append(header_ar + loc_ar)
        
        return file_ar
    def parse_measurement_location(self, dataFile, loc_name):
        res = []
        measurement_loc = dataFile.find(loc_name)
        measurement_loc_id = measurement_loc.tag
        x_m = measurement_loc.find('x_offset').text
        y_m = measurement_loc.find('y_offset').text
        z_m = measurement_loc.find('z_offset').text
        
        return [measurement_loc_id,x_m,y_m,z_m]

# Conversion executor function
def convert_xml_to_list(file_path):
    with open(file_path) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        parser_obj = Xml_Parser()
        xml_list = parser_obj.parse_datafiles(f,root)
    return xml_list

# Batch executor
def batch_convert_xml_to_df(xml_dir, dataset_columns,file_limit=-1):
    i=0
    converted_dataset = []
    # Recursively convert each target file
    for filepath in glob.iglob(xml_dir, recursive=True):
        c_ds = convert_xml_to_list(filepath)
        converted_dataset+=c_ds

        i+=1
        if (i >= file_limit) and (file_limit>=0): break
    
    df = pd.DataFrame(converted_dataset, columns = dataset_columns) 
    return df

if __name__ == '__main__':
    # Constaints 
    measurement_file_path = '/home/GenStore/sample-data-set/auto-gen/xml/*.xml'
    measurement_columns = ['machine_id','test_id','technician','test_routine','batched','measurement_location_id','x_offset','y_offset','z_offset']
    file_process_limit = 20 # Set to -1 for unlimited

    converted_file_dir = '/home/GenStore/sample-data-set/auto-gen/converted'

    lab_measurement_df = batch_convert_xml_to_df(measurement_file_path, measurement_columns, file_process_limit)

    # Save dataset to csv using unique name
    destPath = '/'.join([converted_file_dir,str(uuid.uuid4().hex)])
    destPath = '.'.join([destPath,'csv'])

    lab_measurement_df.to_csv(destPath, index = False, header=True)

