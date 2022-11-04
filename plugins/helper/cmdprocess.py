import sys
import os
sys.path.append("..")
sys.path.append("...")
import subprocess

class CmdWrap:

    def __init__(self):
      return

    def run_cmd(self, *args, **kwds):
            cmd, = args
            print(cmd)
            process = subprocess.Popen(cmd,
                                        shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        cwd=None)
            out = process.communicate()

            if process.returncode != 0:
                raise Exception(cmd, process.returncode, out)
            else:
                return out

