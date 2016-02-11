from .stage01_physiology_analysis_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_physiology_analysis_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_physiology_analysis':data_stage01_physiology_analysis,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_physiology_analysis(self):
        try:
            data_stage01_physiology_analysis.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_physiology_analysis(self):
        try:
            data_stage01_physiology_analysis.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_physiology_analysis(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_physiology_analysis).filter(data_stage01_physiology_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_physiology_analysis).analysis_id.like(analysis_id_I).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01PhysiologyAnalysis(self, data_I):
        '''add rows of data_stage01_physiology_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_physiology_analysis(
                        d['analysis_id'],
                        d['experiment_id'],
                        d['sample_name_short'],
                        d['sample_name_abbreviation'],
                        d['analysis_type'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01PhysiologyAnalysis(self,data_I):
        '''update rows of data_stage01_physiology_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_physiology_analysis).filter(
                            data_stage01_physiology_analysis.id.like(d['id'])).update(
                            {
                            'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name_short':d['sample_name_short'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'analysis_type':d['analysis_type'],
                            'used_':d['used_'],
                            'comment_I':d['comment_I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit(); 
    def get_experimentIDAndSampleName_analysisID_dataStage01PhysiologyAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_physiology_analysis.experiment_id,
                    data_stage01_physiology_analysis.sample_name_abbreviation).filter(
                    data_stage01_physiology_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_physiology_analysis.used_.is_(True)).group_by(
                    data_stage01_physiology_analysis.experiment_id,
                    data_stage01_physiology_analysis.sample_name_abbreviation).order_by(
                    data_stage01_physiology_analysis.experiment_id.asc(),
                    data_stage01_physiology_analysis.sample_name_abbreviation.asc()).all();
            experiment_id_O = []
            sample_name_abbreviation_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);                
            return  experiment_id_O,sample_name_abbreviation_O;
        except SQLAlchemyError as e:
            print(e);