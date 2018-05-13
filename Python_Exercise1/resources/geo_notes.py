import os
from flask import request
from flask_restful import Resource, fields, marshal_with
import Python_Exercise1.common.geo_xml_parser as geo

class Geo_Notes(Resource):

    def get(self, device_name):
        '''Get the notes for a device - Return the appropriate notes given a device name as a parameter of the REST call '''
        
        xml_file = os.path.join(os.getcwd(), 'common/mini-schema.xml')
        
        return_status, device_note = geo.get_element_note(xml_file, device_name)
        
        if return_status == True:
            return {device_name: device_note}, 200
        else:
            return {"Error": "Device not found"}, 404
