# Housing Price Prediction
This Project implements a Real Estate Prediction Website.
Bangalore Home Prices Dataset from Kaggle is preprocessed and feature engineered. Then a Regression model is built on the dataset using Linear Regression. Finally, the model is deployed through a website that uses a Flask server on the backend to ouptut the predicted price.

Technologies/ Frameworks Used
* Python
* Numpy and Pandas
* Scikit-Learn
* Flask Framework
* HTML, CSS and Javascript
* Matplotlib

This website has been deployed using

*   Amazon EC2 Instance
*   Apache2

The Deployed website can be accessed [here](ec2-13-233-118-214.ap-south-1.compute.amazonaws.com)

## Running Locally

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:dpsingh287/Housing-Price-Prediction.git
    $ cd Housing-Price-Prediction
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
You can now run the development server:

    $ python server.py
## Screenshots
![image](https://user-images.githubusercontent.com/83512136/208238539-7c156c81-dfb6-4e56-abeb-ef9a4267736e.png)
![image](https://user-images.githubusercontent.com/83512136/208238615-2c51b992-e897-4a6c-b14c-29cb7bae334e.png)
