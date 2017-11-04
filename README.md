# kittyTracks
RESTful service to access cattracks data 

## Getting started

You can use the heroku instance I deployed or deploy your own local version

### Heroku server 
kittytracks.herokuapp.com

### Getting started locally

1. Clone the respository
2. Set up your virtualenv (recommended)
3. install dependencies:
```bash
    pip install -r requirements.txt
```
4. run the app.py file with the python command

See API Endpoints below to start using the endoints

## API Endpoints
HTTP | URI | Action
--- | --- | ---
**GET** | http://[hostname]/kittyTracks/api/v1.0/lines | Retrieves lines w/ associated stops and times

## Example Request & Response

**/kittyTracks/api/v1.0/lines?line=fastcat** 

```json
{
    "_id" : "SOMERANDOMIDFROMMONGO",
    "line" : "fastcat",
    "availability" : "Mon-Fri",
    "stops" : {
        "Emigrant Pass at Scholars Lane | " : [ 
            "6:28", 
            "7:26", 
            "8:44", 
            "9:42", 
            "10:40", 
            "11:58", 
            "12:56", 
            "2:14", 
            "3:12", 
            "4:10", 
            "5:08", 
            "6:26", 
            "7:24\n"
        ],
        "Muir Pass | " : [ 
            "6:26", 
            "7:24", 
            "8:42", 
            "9:40", 
            "10:38", 
            "11:56", 
            "12:54", 
            "2:12", 
            "3:10", 
            "4:08", 
            "5:06", 
            "6:24", 
            "7:22", 
            "8:20", 
            ""
        ],
        "Mammoth Lakes Rd | " : [ 
            "6:21", 
            "7:19", 
            "8:17", 
            "9:35", 
            "10:33", 
            "11:31", 
            "12:49", 
            "1:47", 
            "3:05", 
            "4:03", 
            "5:01", 
            "5:59", 
            "7:17", 
            "8:15\n"
        ],
        "Merced College The Bus Terminal | " : [ 
            "6:11", 
            "7:09", 
            "8:07", 
            "9:25", 
            "10:23", 
            "11:21", 
            "12:39", 
            "1:37", 
            "2:55", 
            "3:53", 
            "4:51", 
            "5:49", 
            "7:07", 
            "8:05\n"
        ],
        "Castle Air Park | " : [ 
            "5:53", 
            "6:51", 
            "7:49", 
            "9:07", 
            "10:05", 
            "11:03", 
            "12:21", 
            "1:19", 
            "2:37", 
            "3:35", 
            "4:33", 
            "5:31", 
            "6:49", 
            "7:47\n"
        ]
    }
}
```
