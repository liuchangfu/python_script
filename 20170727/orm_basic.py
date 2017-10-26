import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
#定义实例,连接mysql服务，mysql+pymysql://用户名:密码@服务器名称/数据库名
engine = create_engine("mysql+pymysql://root:@127.0.0.1/test",encoding = 'utf-8',echo=True)
#生成orm基类
Base = declarative_base()
#定义表结构
class User(Base):
    __tablename__ ='user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
#生成表结构
Base.metadata.create_all(engine)
#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
#生成session实例
Session = Session_class()
#生成你要创建的数据对象
user_obj = User(name='alex',password='123456')
user_obj1 = User(name='alex123',password='123456')
#把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj)
Session.add(user_obj1)
#提交，创建数据
Session.commit()