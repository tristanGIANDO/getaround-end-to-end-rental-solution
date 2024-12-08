# getaround-end-to-end-rental-solution

## INTRODUCTION

[GetAround](https://www.getaround.com/?wpsrc=Google+Organic+Search) is the Airbnb for cars. You can rent cars from any person for a few hours to a few days! Founded in 2009, this company has known rapid growth. In 2019, they count over 5 million users and about 20K available cars worldwide.

### Project 🚧

When using Getaround, drivers book cars for a specific time period, from an hour to a few days long. They are supposed to bring back the car on time, but it happens from time to time that drivers are late for the checkout.

Late returns at checkout can generate high friction for the next driver if the car was supposed to be rented again on the same day : Customer service often reports users unsatisfied because they had to wait for the car to come back from the previous rental or users that even had to cancel their rental because the car wasn’t returned on time.

### Goals 🎯

In order to mitigate those issues we’ve decided to implement a minimum delay between two rentals. A car won’t be displayed in the search results if the requested checkin or checkout times are too close from an already booked rental.

It solves the late checkout issue but also potentially hurts Getaround/owners revenues: we need to find the right trade off.

* **threshold:** how long should the minimum delay be?
* **scope:** should we enable the feature for all cars?, only Connect cars?

## DELIVERIES

### Web dashboard

Click on [this](https://getaround-end-to-end-rental-solution-fxcfy9ndwnqd3facsw3nd5.streamlit.app/) link to access the web dashboard.

Copy/paste this link if you can't access the URL:

```url
https://getaround-end-to-end-rental-solution-fxcfy9ndwnqd3facsw3nd5.streamlit.app/
```

![dashboard_image](https://raw.githubusercontent.com/tristanGIANDO/getaround-end-to-end-rental-solution/main/resources/dashboard.png)

### API

The API documentation is available [here](https://gt-api-getaround-93493ccc17ad.herokuapp.com/docs#/).

Copy/paste this link if you can't access the URL:

```url
https://gt-api-getaround-93493ccc17ad.herokuapp.com/docs#/
```

![api_image](https://raw.githubusercontent.com/tristanGIANDO/getaround-end-to-end-rental-solution/main/resources/api.png)

## Train the model

To train the model, run this command:

```py
python -m train
```

The model is saved in `data/model.pkl`.

## Deploy in local

```bash
streamlit run deployment/dashboard.py
```

```bash
python api.py
```

Or if you can use `make`:

```bash
make local-app
```
