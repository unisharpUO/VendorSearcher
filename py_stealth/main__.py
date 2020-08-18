
import os
import sys
import traceback

try:
    from py_stealth import methods, winapi, _protocol
except ImportError:
    sys.path.insert(0, os.path.split(os.path.dirname(__file__))[0])
    from py_stealth import methods, winapi, _protocol
finally:
    from py_stealth.config import DEBUG, ERROR_FILTER


__author__ = 'ZeroDX'
__version__ = 1.2


class SysJournalOut:
    def __init__(self, stream=None):
        self._buffer = str()
        self.stream = stream

    def write(self, line):
        if self.stream is not None:
            self.stream.write(line)
        self._buffer += line
        if '\n' in line:
            self.flush()

    def flush(self):
        methods._add_to_system_journal(self._buffer)
        self._buffer = str()


def main():
    # check cmd
    try:
        self, script = sys.argv[:2]
    except ValueError:
        error = 'CMD params must be: path_to_script [port]'
        title = 'Error'
        if b'' == '':  # py2
            error = error.decode()
            title = title.decode()
        winapi.MessageBox(0, error, title, 0)
        exit(4)
    # change output to the stealth system journal
    if not DEBUG:
        sys.stdout = sys.stderr = SysJournalOut()
    # modify the python import system
    if sys.version_info < (3, 4):  # 2.6 - 3.3
        import py_stealth.py26 as importer
    else:  # 3.4 and above
        import py_stealth.py34 as importer
    sys.meta_path.insert(0, importer.Finder())
    # run script
    directory, filename = os.path.split(script)
    sys.path.insert(0, directory)
    exc = False
    methods.Wait(1)  # connect and save a port number into the Connection class
    try:
        __import__(os.path.splitext(filename)[0])
    except:
        if DEBUG or not ERROR_FILTER:
            raise
        # clean package files and code from trace
        trace = traceback.format_exc().splitlines()
        skip = False
        for line in trace:
            if skip:
                skip = False
            elif "\\py_stealth\\" in line or '/py_stealth/' in line:
                skip = True
            elif "_bootstrap" not in line:
                sys.stderr.write(line + '\n')
    if exc:
        exit(1)


if __name__ == '__main__':
    main()
