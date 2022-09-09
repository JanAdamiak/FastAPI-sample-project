# Sample FastAPI project
This repository is a hobby project, that serves as a way to learn FastAPI.
I will additionally try to pick-up a few more technologies in this project.
All of them will be listed below.

## Running the project
To run the project locally you have to [install Docker on your machine](https://docs.docker.com/get-docker/).

Then you can try building the Docker image by using:
`sudo docker build . -t myapp`

And running the Docker image with:
`sudo docker run myapp`

If no issues were present the server should be running on http://0.0.0.0:80

## Running the tests
To run the tests locally you have to ensure you have the environment setup with all the dependencies downloaded.
Then you can call: 
`pytest`

## DB schema
Database schema can be found [here](https://dbdiagram.io/d/631b18440911f91ba570e59c)


## API design

At a high level, we need the following three APIs:

#### POST /v1/sales-webhook
Spawn a purchase task for the paid order to be added to our database.
Since we have many regional offices around the globe we want to be able to do writes ascynchronously.

    regional_office - Office from which the request came (probably could be identified from the authorisation credentials)
    external_order_number - order_number supplied in regional office to keep track of purchase
    car_model - model of the ordered car
    brand - brand of the car (an enum with allowed models)


#### GET /v1/get-all-vehicles-for-manufacturing/{brand}
This is a very simplified endpoint that essentially pools together all purchases that haven't started manufacturing.
In a more advanced version each Purchase would be linked to a product (car) and that product would have parts model attached to it.
This would allow us to regulary run a cronjob at the end of the day (or the rate that the manufacturer wants) to pool together all the vechicle parts we need.

    id - a way for manufacturer to reference this purchase
    car_model - model of the ordered car
    brand - brand of the car (an enum with allowed models)


#### POST /v1/update-state-webhook/{purchase_id}
This endpoint allows a manufacturer to update us on the state of the car.
So we can update the purchase state and allow users to track what's happening.

    purchase_id - a way for manufacturer to reference this purchase
    state - new state of the purchase

Additionally on state update:
Regional offices might have a webhook that listens to the purchase state updates from our end.
This would be triggered on each update of the purchase where state has changed.
We would spawn a task that would later send a request with payload of state to the regional office.


#### POST /login
Endpoint for manufacturers and regional sales offices to authenticate themselves through JWT or OAuth2.
