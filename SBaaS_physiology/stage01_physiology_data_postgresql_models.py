from SBaaS_base.postgresql_orm_base import *

class data_stage01_physiology_data(Base):
    __tablename__ = 'data_stage01_physiology_data'
    id = Column(Integer, Sequence('data_stage01_physiology_data_id_seq'), primary_key=True)
    #experiment_id = Column(String(50), primary_key=True)
    experiment_id = Column(String(50))
    #sample_id=Column(String(500), nullable=False, primary_key=True);
    sample_id=Column(String(500), nullable=False);
    #sample_name_short = Column(String(100), primary_key=True)
    #time_point = Column(String(10))
    #sample_date = Column(DateTime, primary_key=True)
    #met_id = Column(String(100), primary_key=True)
    met_id = Column(String(100))
    data_raw = Column(Float)
    data_corrected = Column(Float)
    data_units = Column(String(100))
    #data_reference = Column(String(500), primary_key=True)
    data_reference = Column(String(500))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_id','met_id','data_reference','data_units'),
            )

    def __init__(self, experiment_id_I,sample_id_I,
                 #sample_name_short_I,time_point_I,sample_date_I,
                 met_id_I,data_raw_I,data_corrected_I,
                 data_units_I,data_reference_I,used__I,comment__I,):
        self.experiment_id=experiment_id_I
        self.sample_id=sample_id_I
        #self.time_point=time_point_I
        #self.sample_date=sample_date_I
        self.met_id=met_id_I
        self.data_raw=data_raw_I
        self.data_corrected=data_corrected_I
        self.data_units=data_units_I
        self.data_reference=data_reference_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
        'experiment_id':self.experiment_id,
        'sample_id':self.sample_id,
        'met_id':self.met_id,
        'data_raw':self.data_raw,
        'data_corrected':self.data_corrected,
        'data_units':self.data_units,
        'data_reference':self.data_reference,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
