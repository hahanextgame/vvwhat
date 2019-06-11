# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, Float, Integer, SmallInteger, String, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FdContentBehaviorMediaHKBBTVSSK(Base):
    __tablename__ = 'fd_content_behavior_media_HKBBTVSSK'
    __table_args__ = (
        UniqueConstraint('followed_media_id', 'media_id'),
    )

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('seq_content_behavior_media_id_hkbbtvssk'::regclass)"))
    ver = Column(String(32), nullable=False)
    server_time = Column(BigInteger, nullable=False)
    ip = Column(String(256))
    city = Column(String(100))
    province = Column(String(100))
    plt = Column(String(100))
    guid = Column(String(100), nullable=False)
    type = Column(SmallInteger, nullable=False)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    ext = Column(JSONB(astext_type=text))
    dt = Column(BigInteger)
    utm_source = Column(String(100))
    followed_media_id = Column(BigInteger)
    media_id = Column(BigInteger)
    uid = Column(String(64), nullable=False)


class FdContentMedia(Base):
    __tablename__ = 'fd_content_media'

    media_id = Column(BigInteger, primary_key=True, server_default=text("nextval('seq_content_media_id'::regclass)"))
    os_key = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    source_type = Column(SmallInteger, nullable=False, server_default=text("1"))
    icon = Column(String(255))
    cover = Column(String(255))
    source_ids = Column(JSONB(astext_type=text))
    third_id = Column(String(255))
    create_time = Column(BigInteger)
    status = Column(SmallInteger, server_default=text("0"))
    describe = Column(String(255))
    ext = Column(JSONB(astext_type=text))
    province = Column(BigInteger)
    city = Column(BigInteger)
    area = Column(BigInteger)
    sex = Column(CHAR(1))
    age = Column(Integer)
    email = Column(String(80))
    country = Column(BigInteger)
    address = Column(String(255))
    birth = Column(BigInteger)
    position_lng = Column(BigInteger)
    position_lat = Column(BigInteger)
    media_num = Column(String(64))
    latitude = Column(Float(53))
    longitude = Column(Float(53))
    update_time = Column(BigInteger)
    sign_time = Column(BigInteger)
    able_status = Column(SmallInteger, server_default=text("1"))
    speech_status = Column(SmallInteger, server_default=text("1"))
    media_mark = Column(SmallInteger)


class FdUserLogin(Base):
    __tablename__ = 'fd_user_login'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('seq_fd_user_login_id'::regclass)"))
    uid = Column(String, nullable=False)
    nickname = Column(String(255), nullable=False, unique=True)
    icon = Column(String(255))
    gender = Column(String(255))
    mobile = Column(String(64))
    source = Column(String(255))
    encrypt = Column(SmallInteger)
    password = Column(String(255))
    code = Column(String(255))
    secret_key = Column(String(255))
    register_time = Column(BigInteger)
    last_login_time = Column(BigInteger)
    status = Column(SmallInteger)
    ext = Column(JSONB(astext_type=text))
    guid = Column(String)
    wechat_union_id = Column(String)
    wechat_open_id = Column(String)
    qq_open_id = Column(String)
    plt = Column(String(255))
    token_time = Column(BigInteger)
    weibo_open_id = Column(String)
    country_code = Column(String(255), server_default=text("86"))
    register_source = Column(Integer)
    te = Column(String)
    media_id = Column(BigInteger)
