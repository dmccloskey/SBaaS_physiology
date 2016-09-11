#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_physiology_data_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_physiology_data_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_physiology_data':data_stage01_physiology_data,
                        };
        self.set_supportedTables(tables_supported);
    def reset_dataStage01_physiology_data(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_physiology_data).filter(data_stage01_physiology_data.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_physiology_data).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def add_dataStage01PhysiologyData(self, data_I):
        '''add rows of data_stage01_physiology_data'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_physiology_data(d
                        #d['experiment_id'],
                        #d['sample_id'],
                        ##d['sample_name_short'],
                        ##d['time_point'],
                        ##d['sample_date'],
                        #d['met_id'],
                        #d['data_raw'],
                        #d['data_corrected'],
                        #d['data_units'],
                        #d['data_reference'],
                        #d['used_'],
                        #d['notes']
                        );
                    #d['comment_']
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01PhysiologyData(self,data_I):
        '''update rows of data_stage01_physiology_data'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_physiology_data).filter(
                            #data_stage01_physiology_data.id == d['id'],
                            data_stage01_physiology_data.experiment_id.like(d['experiment_id']),
                            data_stage01_physiology_data.sample_id.like(d['sample_id']),
                            data_stage01_physiology_data.met_id.like(d['met_id']),
                            data_stage01_physiology_data.data_units.like(d['data_units']),
                            data_stage01_physiology_data.data_reference.like(d['data_reference'])).update(
                            {
                            'experiment_id':d['experiment_id'],
                            'sample_id':d['sample_id'],
                            #'sample_name_short':d['sample_name_short'],
                            #'time_point':d['time_point'],
                            #'sample_date':d['sample_date'],
                            'met_id':d['met_id'],
                            'data_raw':d['data_raw'],
                            'data_corrected':d['data_corrected'],
                            'data_units':d['data_units'],
                            'data_reference':d['data_reference'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query sample names from data_stage01_physiology_data
    def get_sampleNameShort_experimentID(self,experiment_id_I,exp_type_I):
        '''Querry sample name short (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_short).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_short).order_by(
                    sample_description.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample IDs from data_stage01_physiology_data
    def get_sampleIDs_experimentID(self,experiment_id_I,exp_type_I):
        '''Querry sample ids (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_physiology_data.sample_id).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id)).group_by(
                    data_stage01_physiology_data.sample_id).order_by(
                    data_stage01_physiology_data.sample_id.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query met_ids from data_stage01_physiology_data
    def get_metIDs_experimentIDAndSampleNameShort(self,experiment_id_I,exp_type_I,sample_name_short_I):
        '''Querry met_ids by sample name short that are used from
        the experiment'''
        try:
            met_ids = self.session.query(data_stage01_physiology_data.met_id).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(sample_name_short_I)).group_by(
                    data_stage01_physiology_data.met_id).order_by(
                    data_stage01_physiology_data.met_id.asc()).all();
            met_ids_O = [];
            for met in met_ids: met_ids_O.append(met.met_id);
            return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample_date and data_corrected from data_stage01_physiology_data
    def get_sampleDateAndDataCorrected_experimentIDAndSampleNameShortAndMetIDAndDataUnits(self,experiment_id_I,exp_type_I,sample_name_short_I,met_id_I,data_units_I):
        '''Querry time and data_corrected by sample name short that are used from
        the experiment sorted by time'''
        try:
            data = self.session.query(sample_description.sample_date,
                    data_stage01_physiology_data.data_corrected).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.met_id.like(met_id_I),
                    data_stage01_physiology_data.data_units.like(data_units_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(sample_name_short_I)).order_by(
                    sample_description.sample_date.asc()).all();
            sample_date_O = [];
            data_corrected_O = [];
            for d in data: 
                sample_date_O.append(d.sample_date);
                data_corrected_O.append(d.data_corrected);
            return sample_date_O,data_corrected_O;
        except SQLAlchemyError as e:
            print(e)
    def get_sampleDateAndDataCorrectedAndSampleIDs_experimentIDAndSampleNameShortAndMetIDAndDataUnits(self,experiment_id_I,exp_type_I,sample_name_short_I,met_id_I,data_units_I):
        '''Querry time and data_corrected by sample name short that are used from
        the experiment sorted by time'''
        try:
            data = self.session.query(sample_description.sample_date,
                    data_stage01_physiology_data.data_corrected,
                    data_stage01_physiology_data.sample_id).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.met_id.like(met_id_I),
                    data_stage01_physiology_data.data_units.like(data_units_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(sample_name_short_I)).order_by(
                    sample_description.sample_date.asc()).all();
            sample_date_O = [];
            data_corrected_O = [];
            sample_id_O = [];
            for d in data: 
                sample_date_O.append(d.sample_date);
                data_corrected_O.append(d.data_corrected);
                sample_id_O.append(d.sample_id);
            return sample_date_O,data_corrected_O,sample_id_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleDateAndDataCorrected_experimentIDAndSampleNameShort(self,experiment_id_I,sample_name_short_I,data_units_I=['mM','OD600']):
        '''Query time and data_corrected by sample name short that are used from
        the experiment sorted by time'''
        try:
            data = self.session.query(sample_description.sample_date,
                    sample_description.sample_name_short,
                    sample_description.sample_name_abbreviation,
                    data_stage01_physiology_data.id,
                    data_stage01_physiology_data.data_corrected,
                    data_stage01_physiology_data.experiment_id,
                    data_stage01_physiology_data.sample_id,
                    data_stage01_physiology_data.met_id,
                    data_stage01_physiology_data.data_units,
                    data_stage01_physiology_data.data_reference).filter(
                    data_stage01_physiology_data.experiment_id.like(experiment_id_I),
                    data_stage01_physiology_data.data_units.in_(data_units_I),
                    data_stage01_physiology_data.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(data_stage01_physiology_data.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(sample_name_short_I)).order_by(
                    data_stage01_physiology_data.experiment_id.asc(),
                    data_stage01_physiology_data.data_units.asc(),
                    data_stage01_physiology_data.met_id.asc(),
                    sample_description.sample_date.asc()).all();
            rows_O = [d._asdict() for d in data];
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
            