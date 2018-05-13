import requests
import json
import sys
import xml.etree.ElementTree as ET

def get_element_list(xml_file):
    '''Get the list of devices from the xml file.'''
    tree = ET.parse(xml_file)
    return tree.findall('devices/device')

def list_element_names(xml_file):
    '''Create a list of device names. '''
    device_name_list=[]
    element_list = get_element_list(xml_file)
    for item in element_list:
        device_name_list.append(item.find('name').text)
    return device_name_list

#list_element_names('mini-schema.xml')

def list_element_notes(xml_file):
    '''Create a list of device notes. '''
    device_note_list=[]
    element_list = get_element_list(xml_file)
    for item in element_list:
        device_note_list.append(item.find('notes').text)
    return device_note_list

#list_element_notes('mini-schema.xml')

names_and_notes = dict(zip(list_element_names('mini-schema.xml'), list_element_notes('mini-schema.xml')))

print names_and_notes


response1 = requests.get('http://127.0.0.1:5000/Geo_Notes/ct')
response2 = requests.get('http://127.0.0.1:5000/Geo_Notes/hub_ethernet_sniffer')
print response1.text, response1.status_code
print response2.text

#-------------------------------
ct_dict_test = response1.json()
print "dictionary_test = " , ct_dict_test

if ct_dict_test['ct'] == names_and_notes['ct']:
    print "PASS"
else:
    print "FAIL" 


#-------------------------------
ct_dict1 = response1.json()
print "dictionary1 = " , ct_dict1

if ct_dict1['ct'] == "Legacy Legato CT transmitter":
    print "PASS"
else:
    print "FAIL" 

#----------------------------------
ct_dict2 = response2.json()
print "dictionary2 = " , ct_dict2
#print  ct_dict2.values()[0]
#print ct_dict2['hub_ethernet_sniffer']

if ct_dict2['hub_ethernet_sniffer'] == "Sniffer":
    print "PASS"
else:
    print "FAIL" 
#----------------------------------

ct_dict3 = json.loads(response1.text)
ct_dict3_new = json.loads(response1.text.decode(sys.getdefaultencoding()))
print "yes", ct_dict3_new

print "dictionary3 = ", ct_dict3

print ct_dict3.keys(), ct_dict3.values()

if ct_dict3.values()[0] == 'Legacy Legato CT transmitter' :
    print "PASS"
else:
    print "FAIL" 
#-------------------------------------

print type(ct_dict3.values()[0])

#-------------------------------------

a = requests.get('http://127.0.0.1:5000/Geo_Notes/ctdddd')

error_dict = a.json()
print "dictionary4 = ", error_dict
print "dictionary4 = ", a
print a.text
print a.status_code

print str(error_dict)
print type(a)



