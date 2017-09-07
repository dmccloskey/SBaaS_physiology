import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
#sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_remote.ini';
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

# make the rates tables
from SBaaS_physiology.stage01_physiology_rates_execute import stage01_physiology_rates_execute
physrates01 = stage01_physiology_rates_execute(session,engine,pg_settings.datadir_settings);
physrates01.initialize_supportedTables();
physrates01.initialize_tables();

#snastr = 'OxicWtGlcDil0p25,OxicWtGlcDil0p32,OxicWtGlcDil0p45,OxicWtGlcDil0p58'
snastr = 'OxicWtGlcDil0p25,OxicWtGlcDil0p33,OxicWtGlcDil0p46,OxicWtGlcDil0p59'
sna = snastr.split(',')

metstr = 'ac,biomass,glc-D,yield'
met = metstr.split(',')

physrates01.execute_calculateRatesAverages(
    'chemoNLim01',
    sample_name_abbreviations_I = sna,
    met_ids_I = met
    )