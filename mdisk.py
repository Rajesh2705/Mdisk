import requests

class GetInfo():
  def __init__(self,param):
    self.param = param
    self.ad_action = None
    self.display_name = None
    self.download = None
    self.duration = None
    self.filename = None
    self.height = None
    self.mainad_action = None
    self.poster = None
    self.rid = None
    self.size = None
    self.source = None
    self.source_type = None
    self.ts = None
    self.width = None
    self.All_Info = None
    self.set_info()

  def set_info(self):
    url=f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={self.param}'
    resp = requests.get(url).json()
    self.ad_action = resp['ad_action']
    self.display_name = resp['display_name']
    self.download = resp['download']
    self.duration = resp['duration']
    self.filename = resp['filename']
    self.height = resp['height']
    self.mainad_action = resp['mainad_action']
    self.poster = resp['poster']
    self.rid = resp['rid']
    self.size = resp['size']
    self.source = resp['source']
    self.source_type = resp['source_type']
    self.ts = resp['ts']
    self.width = resp['width']
    self.All_Info = resp
  
GetInfo("aae5e7").All_Info
