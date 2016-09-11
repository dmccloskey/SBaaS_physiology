# System
import json
from .stage01_physiology_data_query import stage01_physiology_data_query
from .stage01_physiology_analysis_query import stage01_physiology_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable

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

    
    def export_dataStage01PhysiologyData_js(self,
            analysis_id_I,
            data_units_I=['mM','OD600'],
            data_dir_I="tmp"
            ):
        """
        Export data_stage01_physiology_data to js file
        
        """

        physiology_analysis_query = stage01_physiology_analysis_query(self.session,self.engine,self.settings);

        # get the analysis information
        sample_name_shorts = [];
        sample_name_shorts = physiology_analysis_query.get_rows_analysisID_dataStage01PhysiologyAnalysis(analysis_id_I);
        data_O = [];
        #TODO optimize to a single query
        for sns_cnt,sns in enumerate(sample_name_shorts):
            data_tmp = [];
            data_tmp = self.get_sampleDateAndDataCorrected_experimentIDAndSampleNameShort(sns['experiment_id'],sns['sample_name_short'],data_units_I=data_units_I);
            for d in data_tmp:
                d['sample_date'] = d['sample_date'].year*8765.81277 + \
                    d['sample_date'].month*730.484  + d['sample_date'].day*365.242 + \
                    d['sample_date'].hour + d['sample_date'].minute / 60. + \
                    d['sample_date'].second / 3600.; #convert using datetime object
                data_O.append(d);

        # visualization parameters
        data1_keys = ['experiment_id',
                      'sample_id',
                      'sample_name_short',
                      'sample_name_abbreviation',
                      'sample_date',
                      'met_id',
                      'data_units'
                      ];
        #TODO xaxis = time
        #TODO seperate plot for each metabolite
        data1_nestkeys = ['met_id'];
        data1_keymap = {
            'xdata':'sample_date',
            'ydata':'data_corrected',
            'serieslabel':'sample_name_short',
            'featureslabel':'sample_id',
            };
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=None,
                data_table=None,
                svgtype='scatterplot2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='time (hrs)',
                svgy1axislabel='data_corrected',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap], #calculated on the fly
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0], #calculated on the fly
                svgfilters=None,
                svgtileheader='Physiological data',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                             "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            'colclass':"col-sm-8"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects()); 
   