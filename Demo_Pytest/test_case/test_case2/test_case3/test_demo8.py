import pytest
import json

# class TestUserPasswrod(object):
#     @pytest.fixture
#     def users(self):
#         return json.loads(open("./users.dev.json","r").read())
#
#     def test_user_password(self,users):
#         for user in users:
#             passwd = user['password']
#             assert len(passwd) >= 6
#             msg = "user %s has a weak password" % (user['name'])
#             assert passwd != 'password', msg
#             assert passwd != 'password123', msg

#  参数化参数化的Fixture
import pytest
import json
users = json.loads(open('./users.dev.json', 'r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" %(user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg

if __name__ == '__main__':
    pytest.main(["-q","test_demo8.py"])