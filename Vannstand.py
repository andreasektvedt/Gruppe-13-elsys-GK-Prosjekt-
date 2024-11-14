import requests
import xml.etree.ElementTree as ET
import datetime
import time

#setter sammen request stringen til kartverkets API med datoen i dag og i morgen
today= datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
req_str = "https://vannstand.kartverket.no/tideapi.php?lat=63.86798521547748&lon=8.654635752331998&fromtime="+str(today)+"T00%3A00&totime="+str(tomorrow)+"T00%3A00&datatype=all&refcode=cd&place=&file=&lang=nn&interval=60&dst=0&tzone=1&tide_request=locationdata"

#Sender en API fåresspørsel til kartverkets vannstands API
response = requests.get(req_str)
#print(req_str)

#Parser XML responsen fra kartverket.no
root = ET.fromstring(response.content)

#Funkjon for å gjøre om XML responsen til et python directory
def parse_xml_to_dict(element):
    data_dict = {element.tag: {} if element.attrib else None}
    children = list(element)
    dd = dict()
    for dc in map(parse_xml_to_dict, children):
        for k, v in dc.items():
            if k in dd:
                if isinstance(dd[k], list):
                    dd[k].append(v)
                else:
                    dd[k] = [dd[k], v]
            else:
                dd[k] = v
        data_dict = {element.tag: dd}
    if element.attrib:
        data_dict[element.tag].update(a for a in element.attrib.items())
    return data_dict

#Kaller opp funksjonen for å gjøre om fra xml til dict
jl = parse_xml_to_dict(root)

"""
#Henter den nyeste målingen fra målestasjonen på maursund
vannstand_målt = jl["tide"]["locationdata"]["data"][0]["waterlevel"][len(jl["tide"]["locationdata"]["data"][0]["waterlevel"])-1]["value"]
"""

#Henter datan med varslet vannstand og skriver dete til en liste
forcast= []
for x in range(0,len(jl["tide"]["locationdata"]["data"][1]["waterlevel"])-1):
    forcast.append(jl["tide"]["locationdata"]["data"][1]["waterlevel"][x]["value"])

#Henter nåverende time som en integer
hour_index = int(((time.time()//3600)+2)%24)

"""
#Sammenligner den nyeste målingen med varselet for denne timen og ut i fra det avgjør om vannstanden synker eller øker.
if float(forcast[hour_index]) > float(vannstand_målt):
    print("vannstanden øker")
else:
    print("vannstanden synker")
"""

#Sammenlikner vanstandsvarselet for denne timen vs den kommende timen for å avgjøre om vannstanden øker eller synker.
if float(forcast[hour_index+1]) > float(forcast[hour_index]):
    print("vannstanden øker")
else:
    print("vannstanden synker")