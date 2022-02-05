from json2xml import json2xml
from json2xml.utils import readfromjson
import time

start_time = time.time()
r = open("XML1.xml", "w")
data = readfromjson("Json.json")
r.write(json2xml.Json2xml(data, wrapper="root", attr_type=False, item_wrap=True).to_xml())
print(f'time:  {1000 * (time.time() - start_time)}')
