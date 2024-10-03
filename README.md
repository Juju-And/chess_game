# chess_game

This is a simple chess game simulator with some limited functionalities like outputting possible movements of figures, or verification whether the planned move is allowed.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install -r requirements.txt
```

### Installing


In order to test the application, the server should run, therefore, the command should be typed:

```
$ python app.py
```


### API endpoints

### URL passes id to methods

#### GET /api/v1/<chess_figure>/<current_field>
Returns possible moves for the provided figure in json format.

#### GET /api/v1/<chess_figure>/<current_field>/<dest_field>
Returns validation whether move of figure from provided field is possible to the other provided field in json format.