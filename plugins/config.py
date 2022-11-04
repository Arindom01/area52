import yaml
import anyconfig
import os
import sys
sys.path.append("..")
sys.path.append("...")
from dateutil.tz import tzoffset
# from ingest_app.utils.errorHandler import ValidationException
# import settings

from datetime import datetime, timedelta


#GLOBAL_TO = eval(App_Conf._conf['timewindow']['to'])
#GLOBAL_FROM = eval(App_Conf._conf['timewindow']['from'])

class App_Conf:


    dt = {}

    #GLOBAL_TO = ''
    #GLOBAL_FROM = ''

    # Get current working directory
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    # proj_dir_path = settings.PROJECT_ROOT
    proj_dir_path = os.path.dirname(os.path.realpath(__file__))
    # Config type (format) is automatically detected by filename (file
    # extension) in some cases.
    _conf = anyconfig.load("./config.yml", "yaml")
    #l = []
    #print tuple((str(x.keys()[0]), str(x.values()[0])) for x in _conf['param'])

    @staticmethod
    def config_list_to_tuple(name):
        return tuple((str(x.keys()[0]), str(x.values()[0])) for x in App_Conf._conf[name])

    @staticmethod
    def config_to_dict(env, name):
        # print(App_Conf._conf[env][name])
        print(App_Conf.config()[name])
        for x in App_Conf.config()[name]:
            print(App_Conf.config()[name][x]) 
        # return dict((str(x),str(App_Conf._conf[env][name][x]) for x in App_Conf._conf[env][name])
        return dict((str(x),str(App_Conf.config()[name][x])) for x in App_Conf.config()[name])

    @staticmethod
    def config():
        try:
            if os.environ['DEPLOY_ENV'] == 'LOCAL':
                ret = App_Conf._conf['non-prod']
            elif os.environ['DEPLOY_ENV'] == 'PROD':
                ret = App_Conf._conf['prod']
            else:
                ret = App_Conf._conf['non-prod']
        except Exception as ex:
            #  raise ValidationException(20001, ex, "Envoronment Variable DEPLOY_ENV not set")
            ret = App_Conf._conf['non-prod']
            print("Envoronment Variable DEPLOY_ENV not set")
        # finally:
        #     ret = App_Conf._conf['non-prod']
        # Set deploy region defaulting to us-east-1
        return ret

    @staticmethod
    def add_to_config_transform_tuple(name):

        now = eval(App_Conf._conf['timewindow']['to'])
        from_date = eval(App_Conf._conf['timewindow']['from']) #datetime.utcnow() - timedelta(seconds=App_Conf._conf['timewindow']['box'])
        now.strftime("%Y-%m-%dT:%H:%M:%S")
        from_date.strftime("%Y-%m-%dT:%H:%M:%S")
        GLOBAL_TO =  now.isoformat()
        print("Global2 %s" %GLOBAL_TO)
        GLOBAL_FROM = from_date.isoformat()
        App_Conf._conf[name].append({'from' : from_date.isoformat()}) #['from'] = now.isoformat()
        App_Conf._conf[name].append({'to': now.isoformat()})
        return tuple((str(x.keys()[0]), str(x.values()[0])) for x in App_Conf._conf[name]), GLOBAL_TO, GLOBAL_FROM