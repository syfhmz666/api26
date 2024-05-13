import unittest

# 当前模块执行前只执行一次
def setUpModuel():
    print('=== setUpModuel ===')
# 当前模块执行前只执行一次
def tearDownModule():
    print('=== tearDownModule ===')
class MyTestCase(unittest.TestCase):
    # 在所有的用例之前 只运行一次
    @classmethod
    def setUpClass(cls):
        print("setupclass")
    # 在所有的用例之后 只运行一次
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
    # 在每个用例执行之前 都会运行一次
    def setUp(self) -> None:
        print("setup")
    # 在每个用例执行之后 都会运行一次
    def tearDown(self) -> None:
        print("teardown")
    # 所有都测试用例必须以test开头
    def test_01(self):
        print("test01")
        # 比较值相等
        self.assertEqual(True, True)

    def test_02(self):
        print("test_02")
    #     包含 a 包含 b 中
        self.assertIn('h',"hello")
    def test_03(self):
        print("test_03")
        # 比较内存中的位置
        self.assertIsNot(2,4/2)
    def test_04(self):
        print("test04")
        # 比大小 less< greater> lessequal<= greaterequal>=
        self.assertGreater(7,4)
    def test_05(self):
        print("test05")
        self.assertIsInstance({'user':'hmz','ps':'123456'},dict)

if __name__ == '__main__':
    unittest.main()
