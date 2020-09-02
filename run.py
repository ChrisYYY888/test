# 基础路径
import os
import platform
import sys
import time
import unittest
from BeautifulReport import BeautifulReport
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner_Echarts import HTMLTestRunner_Echarts

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
print(base_path)


def run_test():
    case_dir = base_path + 'test_cases/'
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test_gd.py')
    filename = base_path + 'report/report_test_gd.html'
    fp = open(filename, 'wb')
    title = '接口自动化测试报告'
    #
    runner = HTMLTestRunner(stream=fp,
                            title=title,
                            description='执行环境：系统：' + platform.platform() + '，Python版本：' + sys.version,
                            verbosity=2,
                            tester='yinqiang')
    runner.run(discover)
    # # 饼状图报告
    # runner_echarts = HTMLTestRunner_Echarts(stream=fp,
    #                                         title=title,
    #                                         description='Interface AutoTest,执行环境：系统：' + platform.platform() +
    #                                                     '，Python版本：' + sys.version,
    #                                         verbosity=2)
    # runner_echarts.run(discover)
    # # BeautifulReport
    # result = BeautifulReport(discover)
    # result.report(filename=time.strftime("%Y-%m-%d %H:%M:%S") + '测试报告',
    #               description='*****报告' + '\n执行环境：系统：' + platform.platform() + '，Python版本：' + sys.version,,
    #               report_dir=base_path + '/report')
    fp.close()


if __name__ == '__main__':
    run_test()
