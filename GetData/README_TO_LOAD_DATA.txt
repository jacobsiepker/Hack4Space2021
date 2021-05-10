Source:	Mars Climate Sounder
	https://atmos.nmsu.edu/data_and_services/atmospheres_data/MARS/aerosols.html
	https://atmos.nmsu.edu/PDS/data/MROM_2104/
	From: 2018-05-18

The data contains only one same file from the data set
Use these two programs to get and parse the full data set


NASAdataLoader.py
	Use this file to download the data files from the source into one folder
	The data file provided only contains the .TAB files, the only ones relevent in our case

NASAParser.py
	Use this file to turn the raw NASA .TAB files into a more useable .CSV file
	CSV lines contain [Date,TimeUTC,M_Latitude,M_Longitude,Dust,Dust_Err,H20Ice,H20_iceErr]
	Lines that contain NULL vals for anything other than H20_ice and H20ice_Err were not considered
	The file that contains the .py file MUST be in the folder with the folder that contains the .TAB files
	The file with the .TAB files must be named data

	