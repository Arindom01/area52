class taskProcessor:

  def __init__(self):
    return

  def process(self, action_payload):

    try:
      from plugins.helper.cmdprocess import CmdWrap 
    except Exception as ex:
      print(ex)
    
    cm = CmdWrap()
    print(cm.run_cmd(['cp', action_payload['cmd']]))

    return action_payload
