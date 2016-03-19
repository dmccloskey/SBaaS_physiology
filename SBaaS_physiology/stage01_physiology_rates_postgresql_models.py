from SBaaS_base.postgresql_orm_base import *

class data_stage01_physiology_rates(Base):
    __tablename__ = 'data_stage01_physiology_rates'
    id = Column(Integer, Sequence('data_stage01_physiology_rates_id_seq'), primary_key=True)
    #experiment_id = Column(String(50), primary_key=True)
    experiment_id = Column(String(50))
    #sample_name_short = Column(String(100), primary_key=True)
    sample_name_short = Column(String(100))
    #met_id = Column(String(100), primary_key=True)
    met_id = Column(String(100))
    slope = Column(Float)
    intercept = Column(Float)
    r2 = Column(Float)
    rate = Column(Float)
    rate_units = Column(String(20))
    p_value = Column(Float)
    std_err = Column(Float)
    used_ = Column(Boolean)
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name_short','met_id'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.std_err=row_dict_I['std_err'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_short=row_dict_I['sample_name_short'];
        self.met_id=row_dict_I['met_id'];
        self.slope=row_dict_I['slope'];
        self.intercept=row_dict_I['intercept'];
        self.r2=row_dict_I['r2'];
        self.rate=row_dict_I['rate'];
        self.rate_units=row_dict_I['rate_units'];
        self.p_value=row_dict_I['p_value'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self, experiment_id_I, sample_name_short_I,
                 met_id_I, slope_I, intercept_I,
                 r2_I, rate_I, rate_units_I,
                 p_value_I, std_err_I,
                 used__I, comment__I):
        self.experiment_id = experiment_id_I;
        self.sample_name_short = sample_name_short_I;
        self.slope = slope_I;
        self.intercept = intercept_I;
        self.met_id=met_id_I
        self.r2 = r2_I;
        self.rate = rate_I;
        self.rate_units = rate_units_I;
        self.p_value = p_value_I;
        self.std_err = std_err_I;
        self.used_ = used__I;
        self.comment_ = comment__I;

    def __repr__dict__(self):
        return {'id':self.id,
        'experiment_id':self.experiment_id,
        'sample_name_short':self.sample_name_short,
        'met_id':self.met_id,
        'slope':self.slope,
        'intercept':self.intercept,
        'r2':self.r2,
        'rate':self.rate,
        'rate_units':self.rate_units,
        'p_value':self.p_value,
        'std_err':self.std_err,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_physiology_ratesAverages(Base):
    __tablename__ = 'data_stage01_physiology_ratesAverages'
    id = Column(Integer, Sequence('data_stage01_physiology_ratesAverages_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    met_id = Column(String(100))
    n = Column(Integer)
    slope_average = Column(Float)
    intercept_average = Column(Float)
    rate_average = Column(Float)
    rate_var = Column(Float)
    rate_lb = Column(Float)
    rate_ub = Column(Float)
    rate_units = Column(String(50))
    used_ = Column(Boolean)
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name_abbreviation','met_id'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.rate_var=row_dict_I['rate_var'];
        self.rate_average=row_dict_I['rate_average'];
        self.intercept_average=row_dict_I['intercept_average'];
        self.slope_average=row_dict_I['slope_average'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.met_id=row_dict_I['met_id'];
        self.n=row_dict_I['n'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.rate_units=row_dict_I['rate_units'];
        self.rate_ub=row_dict_I['rate_ub'];
        self.rate_lb=row_dict_I['rate_lb'];

    def __set__row__(self, experiment_id_I, sample_name_abbreviation_I,
                 met_id_I, n_I, slope_average_I, intercept_average_I, rate_average_I, rate_var_I,
                 rate_lb_I, rate_ub_I, rate_units_I, used__I, comment__I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.met_id=met_id_I;
        self.n = n_I;
        self.slope_average = slope_average_I;
        self.intercept_average = intercept_average_I;
        self.rate_average = rate_average_I;
        self.rate_var = rate_var_I;
        self.rate_lb = rate_lb_I;
        self.rate_ub = rate_ub_I;
        self.rate_units = rate_units_I;
        self.used_ = used__I;
        self.comment_ = comment__I;

    def __repr__dict__(self):
        return {'id':self.id,
            'experiment_id':self.experiment_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'met_id':self.met_id,
            'n':self.n,
            'slope_average':self.slope_average,
            'intercept_average':self.intercept_average,
            'rate_average':self.rate_average,
            'rate_var':self.rate_var,
            'rate_lb':self.rate_lb,
            'rate_ub':self.rate_ub,
            'rate_units':self.rate_units,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
