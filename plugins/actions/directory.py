class taskProcessor:

  def __init__(self):
    return
  
  def process(self, action_payload):

    try:
      from plugins.helper.cmdprocess import CmdWrap 
    except Exception as ex:
      print(ex)
    
    cm = CmdWrap()
    cm.run_cmd(['install',
                     '-d',
                      '-m' ,
                      action_payload["mode"],
                      '-g', action_payload["group"],
                      '-o', action_payload["owner"],
                      action_payload["Name"]])

    return action_payload
