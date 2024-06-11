# Fare Amount Prediction

## Project Overview

**Project 2: Fare Amount Prediction**

**Objective**: Predict the fare amount for taxi rides accurately.

This project involves developing a model to predict the fare amount for taxi rides based on various factors such as user details, driver conditions, weather, traffic conditions, pickup/dropoff locations, and trip details. The application is deployed using Django, and an API integration with Google Maps is used to calculate distances between pickup and dropoff locations.

## Technologies Used

- **Django**: A high-level Python web framework used for deploying the application.
- **Google Maps API**: Integrated to calculate the distance between pickup and dropoff locations.
- **Python**: Used for developing the predictive model and implementing backend logic.
- **Machine Learning Libraries**: Including libraries like scikit-learn, pandas, and numpy for data analysis and model building.

## Project Description

This project aims to predict the fare amount for taxi rides by analyzing multiple factors:

- **User Details**: Information about the user requesting the ride.
- **Driver Conditions**: Details about the driver, such as experience and ratings.
- **Weather**: Current weather conditions during the trip.
- **Traffic Conditions**: Real-time traffic data impacting the trip.
- **Pickup and Dropoff Locations**: Geographical coordinates and addresses.
- **Trip Details**: Information like trip duration, distance, and route.

By evaluating these parameters, the model predicts the fare amount accurately. 

### Google Maps API Integration

The project integrates with the Google Maps API to calculate the distance between the pickup and dropoff locations. This integration allows for more precise fare predictions by considering the actual driving distance rather than just the straight-line distance.


