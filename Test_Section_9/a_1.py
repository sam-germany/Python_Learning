import os
import shutil


import variables

class A_1:

    source_path ="/Pro_2_Testing/files_folder/space_!"
    destination_path ="/Pro_2_Testing/files_folder/space_2"
    pcl_type = 'start'
    sequencing_mode = 'meta'


    def create_test_config_impl(self, source_path, destination_path):

        config_path = os.path.expandvars(self.source_path, self.destination_path)
        test_config_path = os.path.expandvars(destination_path)
        # backup original config
        shutil.copyfile(config_path, test_config_path)


    def  (self, destination_path, variables.pc)
