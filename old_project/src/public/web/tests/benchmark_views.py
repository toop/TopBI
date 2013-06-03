
""" ``benchmark_views`` module.
"""

from wheezy.core.benchmark import Benchmark

from public.web.tests.test_views import PublicTestCase
from public.web.tests.test_views import ErrorTestCase


class PublicBenchmarkTestCase(PublicTestCase, ErrorTestCase):

    def runTest(self):
        """ Perform bachmark and print results.
        """
        b = Benchmark((
            self.test_root,
            self.test_home,
            self.test_error_400,
            self.test_error_403,
            self.test_error_404,
        ), 1000)
        b.report('public', baselines={
            'test_root': 1.0,
            'test_home': 1.0,
            'test_error_400': 1.0,
            'test_error_403': 1.0,
            'test_error_404': 1.0,
        })


class StaticFilesBenchmarkTestCase(PublicTestCase, ErrorTestCase):

    def runTest(self):
        """ Perform bachmark and print results.
        """
        b = Benchmark((
            self.test_static_files,
            self.test_static_file_not_found,
            self.test_static_file_forbidden
        ), 1000)
        b.report('static', baselines={
            'test_static_files': 1.00,
            'test_static_file_not_found': 1.0,
            'test_static_file_forbidden': 1.0,
        })

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: