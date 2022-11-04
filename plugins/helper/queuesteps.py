import sys
import glob, os
import re
import json
sys.path.append("..")
sys.path.append("...")
import subprocess
import hcl
# import importlib
import importlib.util
from importlib.machinery import SourceFileLoader
import inspect
from pydoc import locate


task_order = [
              "file", 
              "directory",
              "template", 
              "package", 
              "service"]
class QueueSteps:

    def __init__(self):
      return

    def taskqueue(self, *args, **kwds):
        worker_queue = []
        task_file_list = []
        run_list_file = None
        runlist = None
        module = None

        # all files with specific extension
        task_file_list = glob.glob(os.path.join(os.getcwd(), '*.hc'))

        if len(task_file_list) < 1:
          return "No configuration instructions found"

        # Load run list order file
        run_list_file = glob.glob(os.path.join(os.getcwd(), 'runlist.hc'))

        if run_list_file is None:
          return "No run list file is provided"
        
        # always take the first file. Onle one file is expected.
        with open(f'{run_list_file[0]}', 'r') as fp:
          runlist = json.load(fp)

        while len(runlist['run_list']) > 0:
          file_name =  re.match(r'^.*\[(?P<name>.*)\]', runlist['run_list'].pop(0)).group('name') + ".hc"
          print(file_name)
          with open(file_name, 'r') as fp:
            action_data_obj = hcl.load(fp)
            for item in task_order:
              if action_data_obj.get(item):
                for task in action_data_obj[item]:
                  action_data_obj[item][task]["do"]["Name"] = task
                  worker_queue.append( {"type": item, "value": action_data_obj[item][task]["do"]})

          while len(worker_queue) > 0:
            # TO - DO
            # file name which matches the actions plugins defined
            task = worker_queue.pop(0)
            
            # file_name = file_name.split(".")[0]
            file_name = task["type"]
            action_payload = task["value"]
            ROOT_DIR = os.path.abspath(os.curdir)
            path = os.path.join(os.path.abspath(os.path.join(__file__, "../..")), f'actions/{file_name}.py')
            # print(path)
            spec = importlib.util.spec_from_file_location(f'{file_name}', path)

            # try:
            #     from ..actions.cmdprocess import CmdWrap 
            #     from ..helper.queuesteps import QueueSteps
            # except Exception as ex:
            #   print(ex)

            try:
              # load the class from module using path
              foo = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(foo)
              # call processor method on task action class for each plugin
              print(foo.taskProcessor().process(action_payload))
            except Exception as ex:
              print(ex)
            # TO - DO

        
            
            
