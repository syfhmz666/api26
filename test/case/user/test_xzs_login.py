import unittest
from lib import xzs_login


class MyTestCase(unittest.TestCase):
    x= xzs_login.xzs_login()
    def test_login_1_ok(self):
        t = self.x.login('666','123456')
        print(t)
        self.assertIn("成功",t)
    # def test_lohin_err(self):
    #     data ={"userName":"","password":"123456","remember":False}
    #     r = requests.post(url=self.url,headers=self.header,json=data)
    #     self.assertIn('用户名或密码错误',r.text)
    def test_login_err_01(self):
        t = self.x.login('','123456')
        self.assertIn('用户名或密码错误',t)
    def test_login_err_02(self):
        t = self.x.login('666','')
        self.assertIn('用户名或密码错误',t)

if __name__ == '__main__':
    unittest.main()
