"""
节点信息

获得指定节点的名字，简介，URL 及头像图片的地址。

https://www.v2ex.com/api/nodes/show.json

Method: GET
Authentication: None
接受参数：

name: 节点名（V2EX 的节点名全是半角英文或者数字）
例如：

https://www.v2ex.com/api/nodes/show.json?name=python
"""
import requests
import pytest

class TestV2exApiWithParams(object):
    domain = 'https://www.v2ex.com/'

    @pytest.mark.parametrize('name,node_id', [('python', 90), ('java', 63), ('go', 375), ('nodejs', 436)])

    def test_node(self, name,node_id):
        path = 'api/nodes/show.json?name=%s' %(name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == name
        assert res['id'] == node_id
        assert 0


if __name__ == '__main__':
    pytest.main(["test_demo9.py"])