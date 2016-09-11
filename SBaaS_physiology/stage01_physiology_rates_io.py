# System
import json
from .stage01_physiology_rates_query import stage01_physiology_rates_query
from .stage01_physiology_analysis_query import stage01_physiology_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable

class stage01_physiology_rates_io(stage01_physiology_rates_query,
                                  stage01_physiology_analysis_query,
                                  sbaas_template_io):

    def export_dataStage01PhysiologyRatesAverages_js_v01(self,analysis_id_I,data_dir_I="tmp"):
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
        data1_keys = ['experiment_id','sample_name_abbreviation', 'met_id','rate_units'];
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
        filtermenuobject_O = None;
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = filtermenuobject_O);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());  
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

        # visualization parameters
        data1_keys = ['experiment_id','sample_name_abbreviation', 'met_id','rate_units'];
        data1_nestkeys = ['met_id'];
        data1_keymap = {'xdata':'met_id','ydata':'rate_average',
                'serieslabel':'sample_name_abbreviation','featureslabel':'met_id',
                'ydatalb':'rate_lb','ydataub':'rate_ub'};
        
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
                svgtype='verticalbarschart2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='met_id',
                svgy1axislabel='Rate',
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
    def export_dataStage01PhysiologyRates_js(self,analysis_id_I,data_dir_I="tmp"):
        """Export data_stage01_physiology_rates to js file"""
        # get the analysis information
        sample_name_shorts = [];
        sample_name_shorts = self.get_rows_analysisID_dataStage01PhysiologyAnalysis(analysis_id_I);
        data_O = [];
        for sns_cnt,sns in enumerate(sample_name_shorts):
            data_tmp = [];
            data_tmp = self.get_rows_experimentIDAndSampleNameShort_dataStage01PhysiologyRates(sns['experiment_id'],sns['sample_name_short']);
            if data_tmp: 
                for d in data_tmp:
                    d['sample_name_abbreviation'] = sns['sample_name_short'];
                    d['rate_lb'] = None
                    d['rate_ub'] = None
                    if not d['std_err'] is None:
                        d['rate_lb'] = d['rate']-d['std_err']
                        d['rate_ub'] = d['rate']+d['std_err']
                    data_O.append(d);

        # visualization parameters
        data1_keys = ['experiment_id','sample_name_abbreviation','sample_name_short', 'met_id','rate_units'];
        data1_nestkeys = ['met_id'];
        data1_keymap = {
            'xdata':'met_id',
            'ydata':'rate',
            'ydatamean':'rate',
            'serieslabel':'sample_name_short',
            'featureslabel':'met_id',
            'ydatalb':'rate_lb',
            'ydataub':'rate_ub'
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
                svgtype='boxandwhiskersplot2d_02',
                tabletype='responsivetable_01',
                svgx1axislabel='met_id',
                svgy1axislabel='Rate',
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
   