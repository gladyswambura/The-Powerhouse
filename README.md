**The-Powerhouse**

## AUTHOR 
*Gladys Wambura*

## DESCRIPTION 
This is a personal gallery application that you displays a variety of  photos from different categories.

## Features
As a user of the application you will be able to:


1. View different photos that interest you.
2. Click on a single photo to expand it and also view the details of the photo. The photo details will appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Travel, Food)
4. Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share with your friends.
5. View photos based on the location they were taken or category.


### Installation and setup instructions

1. Clone this repo: git clone https://github.com/gladyswambura/The-Powerhouse
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database gallery using the command below.


       CREATE DATABASE gallery;
5. Migrate the database using the command below


       python3.6 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests

Use the command given below to run automated tests.

        python manage.py test gallery

## TECHNOLOGIES USED 

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## CONTACTS
gladyswahito7@gmail.com

## LIVE LINK
https://gladysgallery.herokuapp.com/


## LICENSE 

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
