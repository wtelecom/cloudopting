import xml.etree.ElementTree as ET

# [main_list.append(i) for i in root]

class ToscaUtils(object):

    def __init__(self, xml):
        super(ToscaUtils, self).__init__()
        #'../resources/clearo_example.xml'
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
        self.main_dict = {'title':'', 'children':[]}


    def get_type(s):
        return s.split('}')[1]


    def walk_children(self, l, n_l):
        d = {}
        for el in l:
            d['title'] = self.get_type(el.tag)
            if len(el.getchildren()):
                self.walk_children(el)



tu = ToscaUtils('../resources/clearo_example.xml')


if len(tu.root.getchildren()):
    tu.main_dict['title'] = tu.get_type(tu.root.tag)
    tu.main_dict['children'] = []
    for child in tu.root.getchildren():
        tu.walk_chilren(child, tu.main_dict['type'])






