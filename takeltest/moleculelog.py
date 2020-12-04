from io import StringIO
import logging
from molecule import util
import os


class MoleculeLog(object):

    def __init__(self):
        self._log_stream = StringIO()
        handler = logging.StreamHandler(self._log_stream)
        self._logger = logging.getLogger('takeltest')
        self._logger.handlers = []
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.DEBUG)

    def debug(self, msg):
        self._logger.debug(msg)

    def get_log(self):
        return self._log_stream.getvalue()

    def print_debug(self):
        takeltest_env = \
            {k: v for (k, v) in os.environ.items() if 'TESTVARS_' in k}
        if takeltest_env:
            print('\n')
            print('TESTVARS ENVIRONMENT')
            print(takeltest_env)
        log = self.get_log()
        if log:
            if not takeltest_env:
                print('\n')
            print('TESTVARS LOG')
            print(log)
