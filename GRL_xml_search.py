import json
import os
import lxml,bs4
from bs4 import BeautifulSoup as bs
class Xml_Parser:
    def Json_parser(self):
        n = int(input("enter a n value:"))
        d = {'location':input()}
        global json_
        for i in range(n):
            keys = input()
            values = input()
            d[keys] = values
        json_ = json.dumps(d)
        json_ = json.loads(json_)
        Xml_Parser.Get_xml(self)
    def Get_xml(self):
        path = json_['location']
        xml_files = []
        for r, d, f in os.walk(path):
            for file in f:
                if '.xml' in file:
                    xml_files.append(os.path.join(r, file))
        Xml_Parser.Search_xml(self,xml_files)
    def Search_xml(self,xml_files):
        print('1')
        for file_path in xml_files:
            xml_content = []
            with open(file_path, "r") as file:
                xml_content = file.readlines()
                xml_content = "".join(xml_content)
                bs_content = bs(xml_content, "lxml")
                result = bs_content.find('Cable_HW_Vers'.lower())
            continue_=count=0
            for i in json_:
                if continue_ == 0:
                    continue_ += 1
                    continue
                result = bs_content.find(i.lower())
                if str(result) == 'None':
                    break
                else:
                    if json_[i].lower() in str(result):
                        count += 1
            if len(json_)-1 == count:
                concat = ''
                for j in range(len(file_path)-1,0,-1):
                    concat +=file_path[j]
                    if file_path[j-1] == '/':
                        break
                print(concat[::-1])

obj1 = Xml_Parser()
obj1.Json_parser()