import unittest
from api.api_gd import *


class TestGD(unittest.TestCase):
    """"""

    def test_gd(self):
        """高德开放接口测试脚本"""
        print("test1")
        self.r = api_gd('北京市海淀区上地街道金隅嘉华大厦', city='010')
        self.assertEqual(self.r['status'], "1")
        self.assertEqual(self.r['info'], "OK")


if __name__ == '__main__':
    unittest.main()
