import xml.etree.ElementTree as ET

def get_element_list(xml_file):
    '''Get the list of devices from the xml file. '''
    tree = ET.parse(xml_file)
    return tree.findall('devices/device')


#print 'Number of elements : ', len(get_element_list('mini-schema.xml'))

def list_element_names(xml_file):
    '''List name of all devices in the device list'''
    element_list = get_element_list(xml_file)
    for item in element_list:
          print(item.find('name').text)


def get_element_note(xml_file, element_name):
    '''Get the notes for a particular device given its name from the xml file. '''
    element_list = get_element_list(xml_file)
    for item in element_list:
        if item.find('name').text == element_name:
            return (True, item.find('notes').text)
    else:
        return (False, 'ERROR')


#list_element_names('mini-schema.xml') 
#print get_element_note('mini-schema.xml', 'ctdina')
#print get_element_note('mini-schema.xml', 'ct')
