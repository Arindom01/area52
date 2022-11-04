from pathlib import Path
import sys
# sys.path.append(str(Path(__file__).parent.parent.parent)) 
import click
from plugins.cli import pass_context
import json
import hcl
# sys.path.append("..")
sys.path.append("...")
# sys.path.append("../helper")
try:
    from ..helper.cmdprocess import CmdWrap 
    from ..helper.queuesteps import QueueSteps
except Exception as ex:
  print(ex)


@click.command('parsesteps', short_help='Shows file changes.')
@click.option('--template_path', '-a', help='The path to directory which holds the configuration steps in hcl')
@pass_context
def cli(ctx, template_path):
    cmd = CmdWrap()
    q = QueueSteps()

    #  load task queue
    q.taskqueue()
    
    # print(obj)
    # print(cmd.run_cmd("ls", "-ltr"))
