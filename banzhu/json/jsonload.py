# -*- coding: utf-8 -*-
import json
import Queue



class jsonLoad(object):

    def load(self, path):
        q = Queue.Queue()
        with open(path,'r') as load_f:
            load_dict = json.load(load_f)
            for item in load_dict:
                q.put(item)
        return q
                