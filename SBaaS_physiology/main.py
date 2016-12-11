import sys
# sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
# filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_remote.ini';
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


physiology_sna = [
'OxicEvo04pgiEvo01J01EcoliGlc',
'OxicEvo04pgiEvo02J01EcoliGlc',
'OxicEvo04pgiEvo03J01EcoliGlc',
'OxicEvo04pgiEvo04J01EcoliGlc',
'OxicEvo04pgiEvo05J01EcoliGlc',
'OxicEvo04pgiEvo06J01EcoliGlc',
'OxicEvo04pgiEvo07J01EcoliGlc',
'OxicEvo04pgiEvo08J01EcoliGlc',
'OxicEvo04ptsHIcrrEvo01J01EcoliGlc',
'OxicEvo04ptsHIcrrEvo02J01EcoliGlc',
'OxicEvo04ptsHIcrrEvo03J01EcoliGlc',
'OxicEvo04ptsHIcrrEvo04J01EcoliGlc',
'OxicEvo04pgiEvo01J02EcoliGlc',
'OxicEvo04pgiEvo02J02EcoliGlc',
'OxicEvo04pgiEvo03J02EcoliGlc',
'OxicEvo04pgiEvo04J02EcoliGlc',
'OxicEvo04pgiEvo05J02EcoliGlc',
'OxicEvo04pgiEvo06J02EcoliGlc',
'OxicEvo04tpiAEvo01J01EcoliGlc',
'OxicEvo04tpiAEvo02J01EcoliGlc',
'OxicEvo04tpiAEvo03J01EcoliGlc',
'OxicEvo04tpiAEvo04J01EcoliGlc',
'OxicEvo04pgiEvo07J02EcoliGlc',
'OxicEvo04pgiEvo08J02EcoliGlc',
'OxicEvo04pgiEvo02J03EcoliGlc',
'OxicEvo04pgiEvo03J03EcoliGlc',
'OxicEvo04tpiAEvo01J03EcoliGlc',
'OxicEvo04pgiEvo04J03EcoliGlc',
'OxicEvo04pgiEvo05J03EcoliGlc',
'OxicEvo04pgiEvo06J03EcoliGlc',
'OxicEvo04pgiEvo07J03EcoliGlc',
'OxicEvo04pgiEvo08J03EcoliGlc',
'OxicEvo04ptsHIcrrEvo03J04EcoliGlc',
'OxicEvo04ptsHIcrrEvo04J04EcoliGlc',
'OxicEvo04ptsHIcrrEvo02J03EcoliGlc',
'OxicEvo04ptsHIcrrEvo03J03EcoliGlc',
'OxicEvo04ptsHIcrrEvo04J03EcoliGlc',
'OxicEvo04tpiAEvo02J03EcoliGlc',
'OxicEvo04tpiAEvo03J03EcoliGlc',
'OxicEvo04tpiAEvo04J03EcoliGlc',
'OxicEvo04ptsHIcrrEvo01J03EcoliGlc',
];
##calculate the average growth rates
physrates01.execute_calculateRatesAverages(
    'ALEsKOs02',
    sample_name_abbreviations_I = physiology_sna,
    met_ids_I = []
    );

