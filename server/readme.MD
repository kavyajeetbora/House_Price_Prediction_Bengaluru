## Developing the server-side application

[Flask](https://flask.palletsprojects.com/en/1.1.x/) web application framework is used to write the server side code.

- On runing the server, the artifacts (trained model and data columns) will be loaded.
- The [server side code](server.py) is responsible for listening to calls from client side and output the prediction based on the inputs
- [util.py](util.py) contains the code for all the essential functions like prediction of house prices, loading artifacts etc
