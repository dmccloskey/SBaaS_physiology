import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_LIMS')
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_statistics')
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_physiology')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/io_utilities')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/calculate_utilities')

#functions to return sample names
#physiology samples to calculate the growth rates
def sample_names_short_calculateGrowthRates_QPR():
    return [
            'OxicEvo04tpiAEcoliGlc_Broth-1',
            'OxicEvo04tpiAEcoliGlc_Broth-2',
            'OxicEvo04tpiAEcoliGlc_Broth-3',
            'OxicEvo04tpiAEvo01EPEcoliGlc_Broth-1',
            'OxicEvo04tpiAEvo01EPEcoliGlc_Broth-2',
            'OxicEvo04tpiAEvo01EPEcoliGlc_Broth-3',
            'OxicEvo04tpiAEvo02EPEcoliGlc_Broth-1',
            'OxicEvo04tpiAEvo02EPEcoliGlc_Broth-2',
            'OxicEvo04tpiAEvo02EPEcoliGlc_Broth-3',
            'OxicEvo04tpiAEvo03EPEcoliGlc_Broth-1',
            'OxicEvo04tpiAEvo03EPEcoliGlc_Broth-2',
            'OxicEvo04tpiAEvo03EPEcoliGlc_Broth-3',
            'OxicEvo04tpiAEvo04EPEcoliGlc_Broth-1',
            'OxicEvo04tpiAEvo04EPEcoliGlc_Broth-2',
            'OxicEvo04tpiAEvo04EPEcoliGlc_Broth-3'
            ];
def sample_names_abbreviation_calculateRatesAverages_QPR():
    return [
            'OxicEvo04tpiAEcoliGlc',
            'OxicEvo04tpiAEvo01EPEcoliGlc',
            'OxicEvo04tpiAEvo02EPEcoliGlc',
            'OxicEvo04tpiAEvo03EPEcoliGlc',
            'OxicEvo04tpiAEvo04EPEcoliGlc'];
#physiology samples used to calculate the uptake and secretion rates
def sample_names_interpolateBiomassFromReplicates_P():
    return [
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3'];
def sample_names_updatePhysiologicalParametersFromOD600_P():
    return [
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-1',
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-2',
        '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-3',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
        '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
        '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
        '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
        '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
        '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3'];
def sample_names_short_calculateUptakeAndSecretionRates_P():
    return [
            "OxicEvo04tpiAEcoliGlc_Broth-1",
            "OxicEvo04tpiAEcoliGlc_Broth-2",
            "OxicEvo04tpiAEcoliGlc_Broth-3",
            "OxicEvo04tpiAEvo01EPEcoliGlc_Broth-1",
            "OxicEvo04tpiAEvo01EPEcoliGlc_Broth-2",
            "OxicEvo04tpiAEvo01EPEcoliGlc_Broth-3",
            "OxicEvo04tpiAEvo02EPEcoliGlc_Broth-1",
            "OxicEvo04tpiAEvo02EPEcoliGlc_Broth-2",
            "OxicEvo04tpiAEvo02EPEcoliGlc_Broth-3",
            "OxicEvo04tpiAEvo03EPEcoliGlc_Broth-1",
            "OxicEvo04tpiAEvo03EPEcoliGlc_Broth-2",
            "OxicEvo04tpiAEvo03EPEcoliGlc_Broth-3",
            "OxicEvo04tpiAEvo04EPEcoliGlc_Broth-1",
            "OxicEvo04tpiAEvo04EPEcoliGlc_Broth-2",
            "OxicEvo04tpiAEvo04EPEcoliGlc_Broth-3"];
def sample_names_abbreviation_exportRatesAverages_P():
    return [
            'OxicEvo04tpiAEcoliGlc',
            'OxicEvo04tpiAEvo01EPEcoliGlc',
            'OxicEvo04tpiAEvo02EPEcoliGlc',
            'OxicEvo04tpiAEvo03EPEcoliGlc',
            'OxicEvo04tpiAEvo04EPEcoliGlc'];
    
    #Physiology starting and endpoint growth rates
    execute01.execute_calculateGrowthRates('ALEsKOs01',sample_names_short_calculateGrowthRates_QPR());
    execute01.execute_interpolateBiomassFromReplicates('ALEsKOs01',sample_names_interpolateBiomassFromReplicates_P());
    execute01.execute_updatePhysiologicalParametersFromOD600('ALEsKOs01',sample_names_updatePhysiologicalParametersFromOD600_P());
    execute01.execute_calculateUptakeAndSecretionRates('ALEsKOs01',sample_names_short_calculateUptakeAndSecretionRates_P());
    execute01.execute_calculateRatesAverages('ALEsKOs01',sample_names_abbreviation_calculateRatesAverages_QPR());
def sample_names_QPR():
    return [
        '140721_41841.3542093171_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.3777238195_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.4001605902_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.4251096065_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.4791666667_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.4930555556_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.3551769097_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.3786927777_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.4011281019_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.4260766087_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.4805555556_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.49375_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.3561445833_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.3796597454_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.4020939814_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.4270440856_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.48125_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.4944444444_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.4923611111_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.5145833333_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.5388888889_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_41841.4923611111_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.5145833333_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.5388888889_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_41841.4923611111_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.5145833333_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_41841.5388888889_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140807_41858.4263888889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.4659722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.4784722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.5270833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.5451388889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.6048611111_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.6291666667_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.6520833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.6652777778_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_41858.4263888889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.4659722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.4784722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.5270833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.5451388889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.6048611111_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.6291666667_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.6520833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.6652777778_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_41858.4263888889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.4659722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.4784722222_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.5270833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.5451388889_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.6048611111_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.6291666667_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.6520833333_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.6652777778_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_41858.4263888889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.4659722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.4784722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.5270833333_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.5451388889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.6048611111_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.6291666667_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.6652777778_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.6805555556_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_41858.4263888889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.4659722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.4784722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.5270833333_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.5451388889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.6048611111_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.6291666667_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.6652777778_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.6805555556_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_41858.4263888889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.4659722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.4784722222_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.5270833333_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.5451388889_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.6048611111_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.6291666667_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.6652777778_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_41858.6805555556_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140811_41862.4180555556_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.46875_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.5291666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.5847222222_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.6138888889_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.6416666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.6527777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.6652777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_41862.4180555556_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.46875_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.5291666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.5847222222_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.6138888889_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.6416666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.6527777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.6652777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_41862.4180555556_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.46875_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.5291666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.5847222222_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.6138888889_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.6416666667_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.6527777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.6652777778_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_41862.4180555556_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.46875_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.5291666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.5847222222_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.6138888889_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.6416666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.6527777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.6652777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_41862.4180555556_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.46875_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.5291666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.5847222222_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.6138888889_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.6416666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.6527777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.6652777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_41862.4180555556_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.46875_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.5291666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.5847222222_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.6138888889_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.6416666667_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.6527777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_41862.6652777778_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-1',
    '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-2',
    '140721_1_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_2_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_3_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_4_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140721_5_OxicEvo04tpiAEcoliGlcM9_Broth-3',
    '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1',
    '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-2',
    '140807_1_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_2_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_3_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_4_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_5_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_6_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-3',
    '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1',
    '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-2',
    '140807_1_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_2_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_3_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_4_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_5_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140807_6_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-3',
    '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1',
    '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-2',
    '140811_1_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_2_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_3_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_4_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_5_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_6_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-3',
    '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1',
    '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-2',
    '140811_1_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_2_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_3_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_4_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_5_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3',
    '140811_6_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-3'];

## initialize the biologicalMaterial_massVolumeConversion
#from SBaaS_LIMS.lims_biologicalMaterial_io import lims_biologicalMaterial_io
#limsbiomat = lims_biologicalMaterial_io(session,engine,pg_settings.datadir_settings);
##limsbiomat.drop_lims_biologicalMaterial();
##limsbiomat.initialize_lims_biologicalMaterial();
##limsbiomat.reset_lims_biologicalMaterial();
#limsbiomat.import_biologicalMaterialMassVolumeConversion_add('data/tests/analysis_physiology/150908_Physiology_ALEsKOs01_biologicalMaterial01.csv');

## initialize the experiment
#from SBaaS_LIMS.lims_experiment_execute import lims_experiment_execute
#limsexperiment = lims_experiment_execute(session,engine,pg_settings.datadir_settings);
#limsexperiment.execute_deleteExperiments(experiment_ids_I = ['ALEsKOs01'],
#                                         sample_names_I = sample_names_QPR());
#limsexperiment.execute_makeExperimentFromSampleFile('data/tests/analysis_physiology/140905_Physiology_ALEsKOs01_sampleFile01.csv',0,[]);
#limsexperiment.execute_makeExperimentFromSampleFile('data/tests/analysis_physiology/140905_Quantification_ALEsKOs01_biomass01.csv',0,[]);

## Make the analysis table
#from SBaaS_physiology.stage01_physiology_analysis_execute import stage01_physiology_analysis_execute
#exanalysis01 = stage01_physiology_analysis_execute(session,engine,pg_settings.datadir_settings);
#exanalysis01.drop_dataStage01_physiology_analysis();
#exanalysis01.initialize_dataStage01_physiology_analysis();
#exanalysis01.reset_dataStage01_physiology_analysis("ALEsKOs01_0_11_evo04tpiA");
#exanalysis01.import_dataStage01PhysiologyAnalysis_add('data/tests/analysis_physiology/150908_Physiology_ALEsKOs01_analysis01.csv');

## make the physiology_data
#from SBaaS_physiology.stage01_physiology_data_execute import stage01_physiology_data_execute
#physdata01 = stage01_physiology_data_execute(session,engine,pg_settings.datadir_settings);
#physdata01.drop_dataStage01_physiology_data();
#physdata01.initialize_dataStage01_physiology_data();
#physdata01.reset_dataStage01_physiology_data('ALEsKOs01');
#physdata01.import_dataStage01PhysiologyData_add('data/tests/analysis_physiology/140905_Physiology_ALEsKOs01_samples01.csv');
#physdata01.import_dataStage01PhysiologyData_update('data/tests/analysis_physiology/140905_Physiology_ALEsKOs01_update01.csv');
#physdata01.import_dataStage01PhysiologyData_add('data/tests/analysis_physiology/140905_Quantification_ALEsKOs01_biomass01.csv');

# make the rates tables
from SBaaS_physiology.stage01_physiology_rates_execute import stage01_physiology_rates_execute
physrates01 = stage01_physiology_rates_execute(session,engine,pg_settings.datadir_settings);
#physrates01.drop_dataStage01_physiology_rates();
#physrates01.initialize_dataStage01_physiology_rates();
## calculate the rates
#physrates01.reset_dataStage01_physiology_rates('ALEsKOs01');
#physrates01.execute_calculateGrowthRates('ALEsKOs01',sample_names_short_calculateGrowthRates_QPR());
#physrates01.execute_interpolateBiomassFromReplicates('ALEsKOs01',sample_names_interpolateBiomassFromReplicates_P());
#physrates01.execute_updatePhysiologicalParametersFromOD600('ALEsKOs01',sample_names_updatePhysiologicalParametersFromOD600_P());
#physrates01.execute_calculateUptakeAndSecretionRates('ALEsKOs01',sample_names_short_calculateUptakeAndSecretionRates_P());
## calculate the yield
#physrates01.execute_calculateYield('ALEsKOs01',
#    sample_name_short_I=sample_names_short_calculateUptakeAndSecretionRates_P()
#    );
# calculate the the average rates
physrates01.reset_dataStage01_physiology_ratesAverages('ALEsKOs01');
physrates01.execute_calculateRatesAverages('ALEsKOs01',sample_names_abbreviation_calculateRatesAverages_QPR());
## calculate the average yield
#physrates01.execute_calculateRatesAverages('ALEsKOs01',
#    sample_name_abbreviations_I=sample_names_abbreviation_calculateRatesAverages_QPR(),
#    met_ids_I=[
#    "yield_ss"
#    ]
#    );
# export the data
physrates01.export_dataStage01PhysiologyRatesAverages_js("ALEsKOs01_0_11_evo04tpiA",data_dir_I="tmp")

