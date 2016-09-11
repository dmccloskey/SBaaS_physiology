import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_physiology')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

# make the physiology_data
from SBaaS_physiology.stage01_physiology_data_execute import stage01_physiology_data_execute
physdata01 = stage01_physiology_data_execute(session,engine,pg_settings.datadir_settings);
physdata01.initialize_supportedTables();
physdata01.initialize_tables();

## export the data
#physdata01.export_dataStage01PhysiologyData_js("ALEsKOs01_0_11_evo04tpiA",data_dir_I="tmp")

# make the rates tables
from SBaaS_physiology.stage01_physiology_rates_execute import stage01_physiology_rates_execute
physrates01 = stage01_physiology_rates_execute(session,engine,pg_settings.datadir_settings);

# export the data
physrates01.export_dataStage01PhysiologyRates_js("ALEsKOs01_0_11_evo04tpiA",data_dir_I="tmp")

