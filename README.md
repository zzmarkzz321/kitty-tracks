# kittyTracks
RESTful service to access cattracks data 

## API Endpoints
HTTP | URI | Action
--- | --- | ---
**GET** | http://[hostname]/kittyTracks/api/v1.0/lines | Retrieves lines w/ associated stops and times
**GET** | http://[hostname]/kittyTracks/api/v1.0/lines?line=[line name] | Retrieves a specific line
**GET** | http://[hostname]/kittyTracks/api/v1.0/stops | Retrieves all stops w/ associated lines and times
**GET** | http://[hostname]/kittyTracks/api/v1.0/stops?stop=[stop name] | Retrieves a specific stops w/ associated lines and times
