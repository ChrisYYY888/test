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


def run_test(type):
    case_dir = base_path + 'test_cases/'
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')
    filename = base_path + 'report/report_test_gd.html'
    fp = open(filename, 'wb')
    title = '接口自动化测试报告'
    # HTMLTestRunner
    if type == 1:
        runner = HTMLTestRunner(stream=fp,
                                title=title,
                                description='执行环境：系统：' + platform.platform() + '，Python版本：' + sys.version,
                                verbosity=2,
                                tester='yinqiang')
        result = runner.run(discover)
    # 饼状图报告
    elif type == 2:
        runner_echarts = HTMLTestRunner_Echarts(stream=fp,
                                                title=title,
                                                description='Interface AutoTest,执行环境：系统：' + platform.platform() +
                                                            '，Python版本：' + sys.version,
                                                verbosity=2)
        result = runner_echarts.run(discover)
    # BeautifulReport
    elif type == 3:
        result = BeautifulReport(discover)
        result.report(filename=time.strftime("%Y-%m-%d %H:%M:%S") + '测试报告',
                      description='*****报告' + ' 执行环境：系统：' + platform.platform() + '，Python版本：' + sys.version,
                      report_dir=base_path + '/report')
    else:
        # 文本报告
        file = base_path + 'report/report_test.txt'
        f = open(file, 'w')
        runner = unittest.TextTestRunner(stream=f)
        result = runner.run(discover)
    print("all cases number: {}".format(result.testsRun))
    print("failed cases number: {}".format(result.failure_count))
    print("failed cases reason: {}".format(result.failures))
    print("error cases number: {}".format(result.error_count))
    print("error cases reason: {}".format(result.errors))
    print("success cases number: {}".format(result.success_count))
    fp.close()


if __name__ == '__main__':
    run_test()
