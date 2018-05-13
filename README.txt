DESCRIPTION
	Web Server with REST API using flask and flask_restful.

HOW TO RUN IT
	mkvirtualenv Python_Exercise
	pip install requirements
	---------------------------
	workon Python_Exercise
	---------------------------

	export FLASK_APP=$HOME/Python_Exercise1
	flask run
	---------------------------
	
	Show devices : shows list of devices : 
		http://127.0.0.1/5000/devices
	Api: REST API: Returns notes for a device : Some examples :
		http://127.0.0.1:5000/geo_Notes/ct
		http://127.0.0.1:5000/geo_Notes/hub_ethernet_sniffer
		http://127.0.0.1:5000/geo_Notes/CELLO
		http://127.0.0.1:5000/geo_Notes/CEL
	  	
KEY DEPENDENCIES:
	create a virtualenv
	pip install the following:
	-flask
	-flask-restful
	-requests

HOW TO RUN THE UNIT TESTS
	tbd

FUTURE ENHANCEMENTS
	tbd

SAMPLE OUTPUT:
	------------------------------------------------------------------------
	http://127.0.0.1:5000/geo_Notes/hub_ethernet_sniffer
	-Returns note for the device with name 'hub_ethernet_sniffer'
	
	{
		"hub_ethernet_sniffer": "Sniffer"
	}

	------------------------------------------------------------------------
	http://127.0.0.1:5000/geo_Notes/CEL
	-Returns Error message - For any device not in the list (mini-schema.xml)
	
	{
		"Error": "Device not found"
	}         
        
	------------------------------------------------------------------------
        
