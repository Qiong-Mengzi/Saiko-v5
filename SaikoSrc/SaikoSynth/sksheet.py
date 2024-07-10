import json

Number = int | float
JSON_Object = Number | str | bool | None

class Note(object):
    '''音符'''
    def __init__(self, **kwargs: JSON_Object):
        '''
        (由于我不大可能会更新代码的注释, 参数请移步至说明文档 [/Sad/sksheet.md](../../Sad/sksheet.md))
        '''
        self.kwargs = kwargs
        self.pitch = kwargs.get('pitch', None)
        self.freq = kwargs.get('pitch', None)
        self.beat = kwargs.get('beat', 0)
        self.delay = kwargs.get('delay', 0)
        self.length = kwargs.get('length', 0)
        self.volume = kwargs.get('volume', kwargs.get('vol', 1))




