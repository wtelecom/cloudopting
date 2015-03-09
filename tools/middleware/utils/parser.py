import xml.etree.ElementTree as ET

class ToscaUtils(object):

    def __init__(self, xml):
        super(ToscaUtils, self).__init__()
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
        self.main_dict = {'type':'', 'children':[]}


    def get_type(self, s):
        return s.split('}')[1]


    def walk_children(self, m_l, n_l):
        p_d = {}
        p_d['type'] = self.get_type(m_l.tag)
        p_d['children'] = []
        n_l.append(p_d)
        for el in m_l:
            d = {}
            d['type'] = self.get_type(el.tag)
            d['children'] = []
            if len(el.getchildren()):
                for child in el.getchildren():
                    self.walk_children(child, d['children'])
            p_d['children'].append(d)

def execute_walk(tu_instance):
    if len(tu_instance.root.getchildren()):
        tu_instance.main_dict['type'] = tu_instance.get_type(tu_instance.root.tag)
        tu_instance.main_dict['children'] = []
        for child in tu_instance.root.getchildren():
            tu_instance.walk_children(child, tu_instance.main_dict['children'])
    else:
        tu_instance.main_dict['type'] = tu_instance.get_type(tu_instance.root.tag)
        tu_instance.main_dict['children'] = []

    return True







