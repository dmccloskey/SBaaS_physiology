#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_physiology_rates_postgresql_models import *
from .stage01_physiology_data_postgresql_models import *
from .stage01_physiology_analysis_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_physiology_rates_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_physiology_rates':data_stage01_physiology_rates,
                    'data_stage01_physiology_ratesAverages':data_stage01_physiology_ratesAverages,
                        };
        self.set_supportedTables(tables_supported);
    def reset_dataStage01_physiology_rates(self,experiment_id_I = None,sample_name_shorts_I=[],met_ids_I=[]):
        try:
            if experiment_id_I and sample_name_shorts_I and met_ids_I:
                for sns in sample_name_shorts_I:
                    for met in met_ids_I:
                        reset = self.session.query(data_stage01_physiology_rates).filter(data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                                                                                     data_stage01_physiology_rates.sample_name_short.like(sns),
                                                                                     data_stage01_physiology_rates.met_id.like(met)).delete(synchronize_session=False);
            elif experiment_id_I and sample_name_shorts_I:
                for sns in sample_name_shorts_I:
                    reset = self.session.query(data_stage01_physiology_rates).filter(data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                                                                                     data_stage01_physiology_rates.sample_name_short.like(sns)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_physiology_rates).filter(data_stage01_physiology_rates.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_physiology_ratesAverages(self,experiment_id_I = None,sample_name_abbreviations_I=[],met_ids_I=[]):
        try:
            if experiment_id_I and sample_name_abbreviations_I and met_ids_I:
                for sns in sample_name_abbreviations_I:
                    for met in met_ids_I:
                        reset = self.session.query(data_stage01_physiology_ratesAverages).filter(data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                                                                                             data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sna),
                                                                                             data_stage01_physiology_ratesAverages.met_id.like(met)).delete(synchronize_session=False);
            elif experiment_id_I and sample_name_abbreviations_I:
                for sna in sample_name_abbreviations_I:
                    reset = self.session.query(data_stage01_physiology_ratesAverages).filter(data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                                                                                             data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sna)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_physiology_ratesAverages).filter(data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01PhysiologyRatesAverages(self, data_I):
        '''add rows of data_stage01_physiology_ratesAverages'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_physiology_ratesAverages(d
                        #d['experiment_id'],
                        #d['sample_name_abbreviation'],
                        #d['met_id'],
                        #d['n'],
                        #d['slope_average'],
                        #d['intercept_average'],
                        #d['rate_average'],
                        #d['rate_var'],
                        #d['rate_lb'],
                        #d['rate_ub'],
                        #d['rate_units'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01PhysiologyRatesAverages(self,data_I):
        '''update rows of data_stage01_physiology_ratesAverages'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_physiology_ratesAverages).filter(
                            data_stage01_physiology_ratesAverages.id.like(d['id'])).update(
                            {
                            'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'met_id':d['met_id'],
                            'n':d['n'],
                            'slope_average':d['slope_average'],
                            'intercept_average':d['intercept_average'],
                            'rate_average':d['rate_average'],
                            'rate_var':d['rate_var'],
                            'rate_lb':d['rate_lb'],
                            'rate_ub':d['rate_ub'],
                            'rate_units':d['rate_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query sample names from data_stage01_physiology_rates
    def get_sampleNameAbbreviations_experimentID_dataStage01PhysiologyRates(self,experiment_id_I,exp_type_I):
        '''Querry sample name abbreviations (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(data_stage01_physiology_rates.sample_name_short)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndMetID_dataStage01PhysiologyRates(self,experiment_id_I,exp_type_I,sample_name_abbreviation_I,met_id_I):
        '''Querry sample name short that are used from
        the experiment'''
        try:
            #sample_names = self.session.query(sample_description.sample_name_short).filter(
            #        data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
            #        data_stage01_physiology_rates.used_.is_(True),
            #        experiment.id.like(experiment_id_I),
            #        experiment.exp_type_id == exp_type_I,
            #        experiment.sample_name.like(data_stage01_physiology_data.sample_id),
            #        experiment.sample_name.like(sample.sample_name),
            #        sample.sample_id.like(sample_description.sample_id),
            #        sample_description.sample_name_short.like(data_stage01_physiology_rates.sample_name_short),
            #        data_stage01_physiology_rates.met_id.like(met_id_I),
            #        sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
            #        sample_description.sample_name_short).order_by(
            #        sample_description.sample_name_short.asc()).all();
            sample_names = self.session.query(data_stage01_physiology_rates.sample_name_short).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    data_stage01_physiology_analysis.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_analysis.sample_name_short.like(data_stage01_physiology_rates.sample_name_short),
                    data_stage01_physiology_rates.met_id.like(met_id_I),
                    data_stage01_physiology_analysis.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_physiology_rates.sample_name_short).order_by(
                    data_stage01_physiology_rates.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentID_dataStage01PhysiologyRates(self,experiment_id_I):
        '''Querry sample name short (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_short).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True)).group_by(
                    sample_description.sample_name_short).order_by(
                    sample_description.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query metIDs from data_stage01_physiology_rates
    def get_metIDs_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologyRates(self,experiment_id_I,exp_type_I,sample_name_abbreviation_I):
        '''Querry met_ids that are used from
        the experiment'''
        try:
            met_ids = self.session.query(data_stage01_physiology_rates.met_id).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.sample_name_short.like(data_stage01_physiology_rates.sample_name_short)).group_by(
                    data_stage01_physiology_rates.met_id).order_by(
                    data_stage01_physiology_rates.met_id.asc()).all();
            met_ids_O = [];
            for met in met_ids: met_ids_O.append(met.met_id);
            return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDs_experimentIDAndSampleNameShort_dataStage01PhysiologyRates(self,experiment_id_I,sample_name_short_I):
        '''Querry met_ids that are used from
        the experiment'''
        try:
            met_ids = self.session.query(data_stage01_physiology_rates.met_id).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    data_stage01_physiology_rates.sample_name_short.like(sample_name_short_I)).group_by(
                    data_stage01_physiology_rates.met_id).order_by(
                    data_stage01_physiology_rates.met_id.asc()).all();
            met_ids_O = [];
            for met in met_ids: met_ids_O.append(met.met_id);
            return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query rate from data_stage01_physiology_rates
    def get_rateData_experimentIDAndSampleIDAndMetID_dataStage01PhysiologyRates(self,experiment_id_I,sample_id_I,met_id_I):
        '''Querry rate data by sample id and met id that are used from
        the experiment'''
        #1 check if the sample is a technical replicate
        try:
           tech = self.session.query(sample_description.istechnical,
                                     sample_description.sample_replicate_biological,
                                     sample_description.sample_date,
                                     sample_description.sample_name_abbreviation,
                                     sample_description.sample_desc,
                                     sample_description.time_point,
                                     experiment.exp_type_id).filter(
                    sample_description.sample_id.like(sample_id_I),
                    sample.sample_id.like(sample_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name)).first();
           technical_O = False;
           sample_replicate_biological_O = None;
           sample_name_abbreviation_O = None;
           sample_description_O = None;
           sample_date_O = None;
           time_point_O = None;
           exp_type_id_O = None;
           if tech:
               technical_O = tech.istechnical;
               sample_replicate_biological_O = tech.sample_replicate_biological;
               sample_date_O = tech.sample_date;
               sample_name_abbreviation_O = tech.sample_name_abbreviation;
               sample_description_O = tech.sample_desc
               time_point_O = tech.time_point;
               exp_type_id_O = tech.exp_type_id;
        except SQLAlchemyError as e:
           print(e);
        #2 if the sample is a technical replicate, get the biological replicate
        if technical_O:
            try:
               sample_id = self.session.query(sample_description.sample_id).filter(
                        sample_description.sample_name_abbreviation.like(sample_name_abbreviation_O),
                        sample_description.sample_desc.like(sample_description_O),
                        sample_description.time_point.like(time_point_O),
                        sample_description.istechnical.is_(False),
                        sample_description.sample_replicate_biological == sample_replicate_biological_O,
                        sample_description.sample_date == sample_date_O,
                        sample_description.sample_replicate == sample_replicate_biological_O,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.exp_type_id == exp_type_id_O).first();
               sample_id_I = None;
               if sample_id: sample_id_I = sample_id.sample_id
            except SQLAlchemyError as e:
                print(e);
        #3 query the data
        try:
            data = self.session.query(data_stage01_physiology_rates.slope,
                    data_stage01_physiology_rates.intercept,
                    data_stage01_physiology_rates.r2,
                    data_stage01_physiology_rates.rate,
                    data_stage01_physiology_rates.rate_units,
                    data_stage01_physiology_rates.p_value,
                    data_stage01_physiology_rates.std_err).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.met_id.like(met_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_id_I),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_physiology_rates.sample_name_short.like(sample_description.sample_name_short)).first();
            slope, intercept, r2, rate, rate_units, p_value, std_err = None,None,None,None,None,None,None;
            if data: 
                slope, intercept, r2, rate, rate_units, p_value, std_err = data.slope, data.intercept, data.r2, data.rate, data.rate_units, data.p_value, data.std_err;
            return slope, intercept, r2, rate, rate_units, p_value, std_err;
        except SQLAlchemyError as e:
            print(e);
    def get_rateData_experimentIDAndSampleNameShortAndMetID_dataStage01PhysiologyRates(self,experiment_id_I,sample_name_short_I,met_id_I):
        '''Querry rate data by sample name short and met id that are used from
        the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_rates.slope,
                    data_stage01_physiology_rates.intercept,
                    data_stage01_physiology_rates.r2,
                    data_stage01_physiology_rates.rate,
                    data_stage01_physiology_rates.rate_units,
                    data_stage01_physiology_rates.p_value,
                    data_stage01_physiology_rates.std_err).filter(
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.met_id.like(met_id_I),
                    data_stage01_physiology_rates.used_.is_(True),
                    data_stage01_physiology_rates.sample_name_short.like(sample_name_short_I)).first();
            slope, intercept, r2, rate, rate_units, p_value, std_err = None,None,None,None,None,None,None;
            if data: 
                slope, intercept, r2, rate, rate_units, p_value, std_err = data.slope, data.intercept, data.r2, data.rate, data.rate_units, data.p_value, data.std_err;
            return slope, intercept, r2, rate, rate_units, p_value, std_err;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleNameShort_dataStage01PhysiologyRates(self,experiment_id_I,sample_name_short_I):
        '''Querry rows by sample name abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_rates).filter(
                    data_stage01_physiology_rates.sample_name_short.like(sample_name_short_I),
                    data_stage01_physiology_rates.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_rates.used_.is_(True)).all();
            data_O = [d.__repr__dict__() for d in data]
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    
    # query sample names from data_stage01_physiology_rates
    def get_sampleNameAbbreviations_experimentID_dataStage01PhysiologyRatesAverages(self,experiment_id_I):
        '''Querry sample name abbreviations (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_physiology_ratesAverages.sample_name_abbreviation).filter(
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True)).group_by(
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation).order_by(
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e)
    # query met_ids from data_stage01_physiology_rates
    def get_metIDs_experimentID_dataStage01PhysiologyRatesAverages(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry sample name abbreviations (i.e. unknowns) that are used from
        the experiment'''
        try:
            met_id = self.session.query(data_stage01_physiology_ratesAverages.met_id).filter(
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True),
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_physiology_ratesAverages.met_id).order_by(
                    data_stage01_physiology_ratesAverages.met_id.asc()).all();
            met_id_O = [];
            for sn in met_id: met_id_O.append(sn.met_id);
            return met_id_O;
        except SQLAlchemyError as e:
            print(e)
            
    # query rate from data_stage01_physiology_ratesAverages
    def get_rateData_experimentIDAndSampleIDAndMetID_dataStage01PhysiologyRatesAverages(self,experiment_id_I,sample_id_I,met_id_I):
        '''Querry rate data by sample id and met id that are used from
        the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_ratesAverages.slope_average,
                    data_stage01_physiology_ratesAverages.intercept_average,
                    data_stage01_physiology_ratesAverages.rate_average,
                    data_stage01_physiology_ratesAverages.rate_units,
                    data_stage01_physiology_ratesAverages.rate_var).filter(
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.met_id.like(met_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_id_I),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sample_description.sample_name_abbreviation)).first();
            slope_average, intercept_average, rate_average, rate_units, rate_var = None,None,None,None,None;
            if data: 
                slope_average, intercept_average, rate_average, rate_units, rate_var = data.slope_average, data.intercept_average, data.rate_average, data.rate_units, data.rate_var;
            return slope_average, intercept_average, rate_average, rate_units, rate_var;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologyRatesAverages(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows by sample name abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_ratesAverages).filter(
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True)).all();
            data_O = []
            if data: 
                for d in data:
                    data_O.append({'experiment_id':d.experiment_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    'met_id':d.met_id,
                    'n':d.n,
                    'slope_average':d.slope_average,
                    'intercept_average':d.intercept_average,
                    'rate_average':d.rate_average,
                    'rate_var':d.rate_var,
                    'rate_lb':d.rate_lb,
                    'rate_ub':d.rate_ub,
                    'rate_units':d.rate_units,
                    'used_':d.used_,
                    'comment_':d.comment_})
            return data_O;
        except SQLAlchemyError as e:
            print(e);
            
    ## Query from data_stage01_physiology_ratesAverages:
    # query met_ids from data_stage01_physiology_ratesAverages
    def get_metID_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologyRatesAverages(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rate data by sample id and met id that are used from
        the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_ratesAverages.sample_name_abbreviation,
                    data_stage01_physiology_ratesAverages.met_id).filter(
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True),
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation,
                    data_stage01_physiology_ratesAverages.met_id).order_by(
                    data_stage01_physiology_ratesAverages.met_id.asc()).all();
            met_id_O = [];
            if data: 
                for d in data:
                    met_id_O.append(d.met_id);
            return met_id_O;
        except SQLAlchemyError as e:
            print(e);
    # query rate from data_stage01_physiology_ratesAverages
    def get_rateData_experimentIDAndSampleNameAbbreviationAndMetID_dataStage01PhysiologyRatesAverages(self,experiment_id_I,sample_name_abbreviation_I,met_id_I):
        '''Querry rate data by sample id and met id that are used from
        the experiment'''
        try:
            data = self.session.query(data_stage01_physiology_ratesAverages.slope_average,
                    data_stage01_physiology_ratesAverages.intercept_average,
                    data_stage01_physiology_ratesAverages.rate_average,
                    data_stage01_physiology_ratesAverages.rate_lb,
                    data_stage01_physiology_ratesAverages.rate_ub,
                    data_stage01_physiology_ratesAverages.rate_units,
                    data_stage01_physiology_ratesAverages.rate_var).filter(
                    data_stage01_physiology_ratesAverages.met_id.like(met_id_I),
                    data_stage01_physiology_ratesAverages.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_ratesAverages.used_.is_(True),
                    data_stage01_physiology_ratesAverages.sample_name_abbreviation.like(sample_name_abbreviation_I)).first();
            slope_average, intercept_average, rate_average, rate_lb, rate_ub, rate_units, rate_var = None,None,None,None,None,None,None;
            if data: 
                slope_average, intercept_average,\
                    rate_average, rate_lb, rate_ub, rate_units, rate_var = data.slope_average, data.intercept_average,\
                    data.rate_average, data.rate_lb, data.rate_ub, data.rate_units, data.rate_var;
            return slope_average, intercept_average, rate_average, rate_lb, rate_ub, rate_units, rate_var;
        except SQLAlchemyError as e:
            print(e);
