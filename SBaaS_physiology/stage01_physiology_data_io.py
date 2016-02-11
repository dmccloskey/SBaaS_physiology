# System
import json
from .stage01_physiology_data_query import stage01_physiology_data_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_physiology_data_io(stage01_physiology_data_query,
                                  sbaas_template_io):

    def import_dataStage01PhysiologyData_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01PhysiologyData(data.data);
        data.clear_data();

    def import_dataStage01PhysiologyData_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01PhysiologyData(data.data);
        data.clear_data();
   