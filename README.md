# Physiome-Blackfynn-API
This api is created to link the [webGL heart model](https://github.com/Tehsurfer/MPB) to the [Blackfynn Python API](https://github.com/Blackfynn/blackfynn-python)

## Documentation of Routes

### Base API address: http://18.191.253.82/api

### '/' (GET)
Returns printout. Can be used for https later

### '/get_timeseries_dataset_names' (POST)
Post Data is taken in like so:

```javascript
postData = { 
  tokenId: 'asdfasdfasdf',
  secret: 'dafsafdasdf'
  }
```
 
  
Response will be a json dictionary containg the names for items containing timeseries data

### '/get_channel_data' (GET)
Note: must have already used '/get_timeseries_dataset_names'
Headers needed:

```
headers = {
  'Name': name of the dataset
  'Channel': data channel in dataset requested
  }
```
  
Response is a json dictionary with the data for 1 second of the channel (will add more here soon)

### '/get_channels' (GET)
Note: must have already used '/get_timeseries_dataset_names'
Headers needed:

```
headers = {
  'Name': name of the dataset
  }
```
  
Response is a json dictionary of channel names

### '/get_channel' (GET)
Note: must have already used '/get_timeseries_dataset_names'
Headers needed:

```
headers = {
  'Name': name of the dataset
  }
```
  
Response is a json dictionary of channel names

### '/get_file' (GET)
Note: must have already used '/get_timeseries_dataset_names'
Headers needed:

```
headers = {
  'FileName': name of the file
  }
```
  
Returns the loaded file

### '/create_openCOR_URL' (GET)
Note: must have already used '/get_timeseries_dataset_names'
( no headers needed )
  
This address will export all the selected channels into a .csv file readable by opencor. 

Response is the URL that can be use to access said .csv file
  
## Backend

### Prerequisites
- pip
- virtualenv
- python 2.7

### Running the Flask App
- Create a python 2.7 virtual environment and activate it: `virtualenv --python=C:\Python27\Scripts PBA_venv`
- Either Open `Config.py` and update the environment variables below
  - BLACKFYNN_API_TOKEN = ""
  - BLACKFYNN_API_SECRET = ""
  or enter them later using the supplied 'index.html' front end
- Run `pip install -r requirements.txt`
- Run `python server.py` to start the flask app

## Frontend
-will add soon (its currently at https://github.com/Tehsurfer/MPB)

### Prerequisites
none

### Use the front end tester
- Open index.html
- enter you API keys and check it fetches the repository names


