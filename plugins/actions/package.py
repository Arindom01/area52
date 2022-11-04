class taskProcessor:

  def __init__(self):
    return

  def process(self, action_payload):

    try:
      from plugins.helper.cmdprocess import CmdWrap 
    except Exception as ex:
      print(ex)
    
    cm = CmdWrap()
    print(cm.run_cmd(['apt-get', 'update']))
    print(cm.run_cmd(['apt-get', 'install', '-y', action_payload['package']]))

    return action_payload
