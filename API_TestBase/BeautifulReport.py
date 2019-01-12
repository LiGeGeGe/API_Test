"""
@Version: 1.0
@Project: BeautyReport

"""

import os
import sys
from io import StringIO as StringIO
import time
import json
import unittest
import platform
import base64
from distutils.sysconfig import get_python_lib
import traceback
from functools import wraps

__all__ = ['BeautifulReport']

HTML_IMG_TEMPLATE = """
    <a href="data:image/png;base64, {}">
    <img src="data:image/png;base64, {}" width="800px" height="500px"/>
    </a>
    <br></br>
"""
from BeautifulReport import BeautifulReport

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    
    def __init__(self, fp):
        self.fp = fp
    
    def write(self, s):
        self.fp.write(s)
    
    def writelines(self, lines):
        self.fp.writelines(lines)
    
    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

SYSSTR = platform.system()
SITE_PAKAGE_PATH = get_python_lib()

FIELDS = {
    "testPass": 0,
    "testResult": [
    ],
    "testName": "",
    "testAll": 0,
    "testFail": 0,
    "beginTime": "",
    "totalTime": "",
    "testSkip": 0
}


class PATH:
    """ all file PATH meta """
    config_tmp_path = SITE_PAKAGE_PATH + '../API_TestBase/template'


class MakeResultJson:
    """ make html table tags """
    
    def __init__(self, datas: tuple):
        """
        init self object
        :param datas: �õ����з������ݽṹ
        """
        self.datas = datas
        self.result_schema = {}
    
    def __setitem__(self, key, value):
        """
        
        :param key: self[key]
        :param value: value
        :return:
        """
        self[key] = value
    
    def __repr__(self) -> str:
        """
            ���ض����html�ṹ��
        :rtype: dict
        :return: self��repr����, ����һ��������ɵ�tr��
        """
        keys = (
            'className',
            'methodName',
            'description',
            'spendTime',
            'status',
            'log',
        )
        for key, data in zip(keys, self.datas):
            self.result_schema.setdefault(key, data)
        return json.dumps(self.result_schema)


class ReportTestResult(unittest.TestResult):
    """ override"""
    
    def __init__(self, suite, stream=sys.stdout):
        """ pass """
        super(ReportTestResult, self).__init__()
        self.begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.start_time = 0
        self.stream = stream
        self.end_time = 0
        self.failure_count = 0
        self.error_count = 0
        self.success_count = 0
        self.skipped = 0
        self.verbosity = 1
        self.success_case_info = []
        self.skipped_case_info = []
        self.failures_case_info = []
        self.errors_case_info = []
        self.all_case_counter = 0
        self.suite = suite
        self.status = ''
        self.result_list = []
        self.case_log = ''
        self.default_report_name = '�Զ������Ա���'
        self.FIELDS = None
        self.sys_stdout = None
        self.sys_stderr = None
        self.outputBuffer = None
    
    @property
    def success_counter(self) -> int:
        """ set success counter """
        return self.success_count
    
    @success_counter.setter
    def success_counter(self, value) -> None:
        """
            success_counter������setter����, ���ڸı�ɹ���case����
        :param value: ��ǰ���ݽ����ĳɹ�������int��ֵ
        :return:
        """
        self.success_count = value
    
    def startTest(self, test) -> None:
        """
            �������������Լ�������ʱ����
        :return:
        """
        unittest.TestResult.startTest(self, test)
        self.outputBuffer = StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.sys_stdout = sys.stdout
        self.sys_stdout = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        self.start_time = time.time()
    
    def stopTest(self, test) -> None:
        """
            ����������ִ����ɺ���е���
        :return:
        """
        self.end_time = '{0:.3} s'.format((time.time() - self.start_time))
        self.result_list.append(self.get_all_result_info_tuple(test))
        self.complete_output()
    
    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.sys_stdout:
            sys.stdout = self.sys_stdout
            sys.stderr = self.sys_stdout
            self.sys_stdout = None
            self.sys_stdout = None
        return self.outputBuffer.getvalue()
    
    def stopTestRun(self, title=None) -> dict:
        """
            ���в���ִ����ɺ�, ִ�и÷���
        :param title:
        :return:
        """
        FIELDS['testPass'] = self.success_counter
        for item in self.result_list:
            item = json.loads(str(MakeResultJson(item)))
            FIELDS.get('testResult').append(item)
        FIELDS['testAll'] = len(self.result_list)
        FIELDS['testName'] = title if title else self.default_report_name
        FIELDS['testFail'] = self.failure_count
        FIELDS['beginTime'] = self.begin_time
        end_time = int(time.time())
        start_time = int(time.mktime(time.strptime(self.begin_time, '%Y-%m-%d %H:%M:%S')))
        FIELDS['totalTime'] = str(end_time - start_time) + 's'
        FIELDS['testError'] = self.error_count
        FIELDS['testSkip'] = self.skipped
        self.FIELDS = FIELDS
        return FIELDS
    
    def get_all_result_info_tuple(self, test) -> tuple:
        """
            ����test �����Ϣ, ��ƴ�ӳ�һ����ɵ�tuple�ṹ����
        :param test:
        :return:
        """
        return tuple([*self.get_testcase_property(test), self.end_time, self.status, self.case_log])
    
    @staticmethod
    def error_or_failure_text(err) -> str:
        """
            ��ȡsys.exc_info()�Ĳ����������ַ������͵�����, ȥ��t6 error
        :param err:
        :return:
        """
        return traceback.format_exception(*err)
    
    def addSuccess(self, test) -> None:
        """
            pass
        :param test:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')
        self.success_counter += 1
        self.status = '�ɹ�'
        self.case_log = output.split('\n')
        self._mirrorOutput = True  # print(class_name, method_name, method_doc)
    
    def addError(self, test, err):
        """
            add Some Error Result and infos
        :param test:
        :param err:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        logs.extend(self.error_or_failure_text(err))
        self.failure_count += 1
        self.add_test_type('ʧ��', logs)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')
        
        self._mirrorOutput = True
    
    def addFailure(self, test, err):
        """
            add Some Failures Result and infos
        :param test:
        :param err:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        logs.extend(self.error_or_failure_text(err))
        self.failure_count += 1
        self.add_test_type('ʧ��', logs)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')
        
        self._mirrorOutput = True
    
    def addSkip(self, test, reason) -> None:
        """
            ��ȡȫ����������case��Ϣ
        :param test:
        :param reason:
        :return: None
        """
        logs = [reason]
        self.complete_output()
        self.skipped += 1
        self.add_test_type('����', logs)
        
        if self.verbosity > 1:
            sys.stderr.write('S  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('S')
        self._mirrorOutput = True
    
    def add_test_type(self, status: str, case_log: list) -> None:
        """
            abstruct add test type and return tuple
        :param status:
        :param case_log:
        :return:
        """
        self.status = status
        self.case_log = case_log
    
    @staticmethod
    def get_testcase_property(test) -> tuple:
        """
            ����һ��test, ������һ��test��class_name, method_name, method_doc����
        :param test:
        :return: (class_name, method_name, method_doc) -> tuple
        """
        class_name = test.__class__.__qualname__
        method_name = test.__dict__['_testMethodName']
        method_doc = test.__dict__['_testMethodDoc']
        return class_name, method_name, method_doc


class BeautifulReport(ReportTestResult, PATH):
    img_path = 'img/' if platform.system() != 'Windows' else 'img\\'
    
    def __init__(self, suites):
        super(BeautifulReport, self).__init__(suites)
        self.suites = suites
        self.log_path = None
        self.title = '�Զ������Ա���'
        self.filename = 'report.html'

    def report(self, description, filename: str = None, log_path='.'):
        """
            ���ɲ��Ա���,�����ڵ�ǰ����·����
        :param log_path: ����report���ļ��洢·��
        :param filename: �����ļ���filename
        :param description: �����ļ���ע��
        :return:
        """
        if filename:
            self.filename = filename if filename.endswith('.html') else filename + '.html'
        
        if description:
            self.title = description
        
        self.log_path = os.path.abspath(log_path)
        self.suites.run(result=self)
        self.stopTestRun(self.title)
        self.output_report()
        text = '\n������ȫ�����, ��ǰ��{}��ѯ���Ա���'.format(self.log_path)
        print(text)
    
    def output_report(self):
        """
            ���ɲ��Ա��浽ָ��·����
        :return:
        """
        template_path = self.config_tmp_path
        override_path = os.path.abspath(self.log_path) if \
            os.path.abspath(self.log_path).endswith('/') else \
            os.path.abspath(self.log_path) + '/'
        
        with open(template_path, 'rb') as file:
            body = file.readlines()
        with open(override_path + self.filename, 'wb') as write_file:
            for item in body:
                if item.strip().startswith(b'var resultData'):
                    head = '    var resultData = '
                    item = item.decode().split(head)
                    item[1] = head + json.dumps(self.FIELDS, ensure_ascii=False, indent=4)
                    item = ''.join(item).encode()
                    item = bytes(item) + b';\n'
                write_file.write(item)
    
    @staticmethod
    def img2base(img_path: str, file_name: str) -> str:
        """
            ���ܴ��ݽ�������filename ���ҵ��ļ�ת��Ϊbase64��ʽ
        :param img_path: ͨ���ļ�����Ĭ��·���ҵ���img����·��
        :param file_name: �û���װ�����д��ݽ������ʼ�����
        :return:
        """
        pattern = '/' if platform != 'Windows' else '\\'

        with open(img_path + pattern + file_name, 'rb') as file:
            data = file.read()
        return base64.b64encode(data).decode()

    def add_test_img(*pargs):
        """
            �������ɸ�ͼƬԪ��, ��չʾ�ڲ��Ա�����
        :param pargs:
        :return:
        """

        def _wrap(func):
            @wraps(func)
            def __wrap(*args, **kwargs):
                img_path = os.path.abspath('{}'.format(BeautifulReport.img_path))
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    if 'save_img' in dir(args[0]):
                        save_img = getattr(args[0], 'save_img')
                        save_img(func.__name__)
                        data = BeautifulReport.img2base(img_path, pargs[0] + '.png')
                        print(HTML_IMG_TEMPLATE.format(data, data))
                    sys.exit(0)
                print('<br></br>')

                if len(pargs) > 1:
                    for parg in pargs:
                        print(parg + ':')
                        data = BeautifulReport.img2base(img_path, parg + '.png')
                        print(HTML_IMG_TEMPLATE.format(data, data))
                    return result
                if not os.path.exists(img_path + pargs[0] + '.png'):
                    return result
                data = BeautifulReport.img2base(img_path, pargs[0] + '.png')
                print(HTML_IMG_TEMPLATE.format(data, data))
                return result
            return __wrap
        return _wrap
