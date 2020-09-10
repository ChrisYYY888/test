import unittest
# from api.api_gd import *


class TestGD(unittest.TestCase):
    """"""

    def test_1(self):
        """高德开放接口测试脚本"""
        print("test1")
        # self.r = api_gd('北京市海淀区上地街道金隅嘉华大厦', city='010')
        # self.assertEqual(self.r['status'], "1")
        # self.assertEqual(self.r['info'], "OK")
        self.a = 1
        self.b = 2
        self.c = self.a + self.b
        self.assertEqual(self.c, 3)

    def test_2(self):
        """接口测试脚本2"""
        print("test2")
        self.a = 1
        self.assertEqual(self.a, 1)

    def test_3(self):
        """接口测试脚本3"""
        print("test3")
        self.a = 1
        self.b = "2"
        self.c = self.a + self.b
        self.assertEqual(self.c, 3)


if __name__ == '__main__':
    unittest.main()
