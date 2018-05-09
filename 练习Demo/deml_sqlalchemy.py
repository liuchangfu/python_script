from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root@localhost:3306/testdb',echo=False)

# 定义Channel对象:
class Channel(Base):
    # 表名
    __tablename__ = 'playback'
    # 表结构
    id = Column(String(20), primary_key=True)
    channel_name = Column(String(45))
    address = Column(String(80))
    service_name = Column(String(45))

# 创建所有表结构
Base.metadata.create_all(engine)

# 创建DBSession类型:
Dbsession = sessionmaker(bind=engine)
session = Dbsession()

# 增操作
# item1 = Channel(id='1', channel_name='catv1', address='http://10.10.10.188/catv1', service_name='news')
# session.add(item1)
#
# item2 = Channel(id='2', channel_name='catv2', address='http://10.10.10.188/catv2', service_name='news')
# session.add(item2)
#
# item3 = Channel(id='3',channel_name='catv3',address='http://10.10.10.188/catv3',service_name='economics')
# session.add(item3)

# item5 = Channel(id='5',channel_name='catv3',address='http://10.10.10.188/catv5',service_name='economics')
# session.add(item5)
#
# session.commit()
# session.close()

# 查操作

# session1 = Dbsession()
# channel = session1.query(Channel).filter(Channel.id < '4').all()
#
# for i in range(len(channel)):
#     print(channel[i].id)
#     print(channel[i].channel_name)
#     print(channel[i].address)
#     print(channel[i].service_name)
#
# session1.close()

# 改操作
# session2 = Dbsession()
# session2.query(Channel).filter(Channel.id == '2').update({Channel.service_name: 'movie'}, synchronize_session=False)
# session2.commit()
# session2.close()

## 查看修改结果
# session3 = Dbsession()
# print('\n')
# print(session3.query(Channel).filter(Channel.id == '2').one().service_name)
# session3.close()

# 删操作
session4 = Dbsession()
session4.query(Channel).filter(Channel.id == '3').delete()
session4.commit()
session4.close()