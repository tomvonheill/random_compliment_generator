# random_compliment_generator

Simple API that will generate a random compliment for you and your loved ones.

## Setup 
### Install environment
execute the following to set up environment

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt

### Run flask app
execute the following to run app

    $ export FLASK_APP=flaskr
    $ flask run
## Endpoints

```GET``` '/compliment/{int:length}'
   
   This endpoint will generate a random compliment with a number of positive attributes equal to  {length} and will have a random positive noun at the end. Length should be between 1 and 960.
   
   example:
```curl http://127.0.0.1:5000/compliment/4```

returns:
```{"compliment":"You are a peerless, graceful, flexible, sincere beauty","success":true}```
