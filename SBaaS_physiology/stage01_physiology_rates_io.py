# System
import json
from .stage01_physiology_rates_query import stage01_physiology_rates_query
from .stage01_physiology_analysis_query import stage01_physiology_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_physiology_rates_io(stage01_physiology_rates_query,
                                  stage01_physiology_analysis_query,
                                  sbaas_template_io):

    def export_dataStage01PhysiologyRatesAverages_js(self,analysis_id_I,data_dir_I="tmp"):
        """Export data_stage01_physiology_ratesAverages to js file"""
        # get the analysis information
        experiment_ids,sample_name_abbreviations = [],[];
        experiment_ids,sample_name_abbreviations = self.get_experimentIDAndSampleName_analysisID_dataStage01PhysiologyAnalysis(analysis_id_I);
        data_O = [];
        for sna_cnt,sna in enumerate(sample_name_abbreviations):
            data_tmp = [];
            data_tmp = self.get_rows_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologyRatesAverages(experiment_ids[sna_cnt],sna);
            if data_tmp: data_O.extend(data_tmp);
        ## remove js regular expressions
        #for i,d in enumerate(data_O):
        #    data_O[i]['rate_units'] = self.remove_jsRegularExpressions(d['rate_units']);
        # get metabolite ids:
        met_ids_all = [];
        for d in data_O:
            met_ids_all.append(d['met_id']);
        met_ids = list(set(met_ids_all));
        biomass_met_ids = ['biomass','yield_ss'];
        uptakesecretion_met_ids = [x for x in met_ids if not x in biomass_met_ids];
        # visualization parameters
        data1_keys = ['sample_name_abbreviation', 'met_id','rate_units']; #rate_units contain string characters that are registered as regular expressions
        data1_nestkeys = ['met_id'];
        data1_keymap = {'xdata':'met_id','ydata':'rate_average',
                'serieslabel':'sample_name_abbreviation','featureslabel':'met_id',
                'ydatalb':'rate_lb','ydataub':'rate_ub'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                             "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":500,"svgheight":350,"svgy1axislabel":"rate (mmol*gDCW-1*hr-1)",
                  "svgfilters":{'met_id':uptakesecretion_met_ids}
                };
        svgtileparameters1_O = {'tileheader':'Uptake/secretion rates','tiletype':'svg','tileid':"tile1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters1_O.update(svgparameters1_O);
        svgparameters2_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg2',
                  "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                  "svgwidth":500,"svgheight":350,
                  "svgy1axislabel":"rate (hr-1)",
                  #"svgy1axislabel":"rate (hr-1) or yield (gDCW*mmol of C-source)",
                  "svgfilters":{'met_id':biomass_met_ids}
                };
        svgtileparameters2_O = {'tileheader':'Growth rate','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters2_O.update(svgparameters2_O);
        tableparameters1_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableheaders":['experiment_id','sample_name_abbreviation','met_id','rate_average','rate_var','rate_lb','rate_ub','rate_units','n','comment_','used_'],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'tile1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters1_O = {'tileheader':'Uptake/secretion rates','tiletype':'table','tileid':"tile3",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters1_O.update(tableparameters1_O);
        tableparameters2_O = {"tabletype":'responsivetable_01',
                    'tableid':'table2',
                    "tablefilters":None,
                    "tableheaders":['experiment_id','sample_name_abbreviation','met_id','rate_average','rate_var','rate_lb','rate_ub','rate_units','n','comment_','used_'],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'tile1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters2_O = {'tileheader':'Growth rates','tiletype':'table','tileid':"tile4",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters2_O.update(tableparameters2_O);
        parametersobject_O = [svgtileparameters1_O,svgtileparameters2_O,tabletileparameters1_O,tabletileparameters2_O];
        tile2datamap_O = {"tile1":[0],"tile2":[1],"tile3":[0],"tile4":[1]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_physiology_ratesAverages' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);       
    def import_dataStage01PhysiologyRatesAverages_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01PhysiologyRatesAverages(data.data);
        data.clear_data();

    def import_dataStage01PhysiologyRatesAverages_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01PhysiologyRatesAverages(data.data);
        data.clear_data();
   