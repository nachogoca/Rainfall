# Rainfall

Rainfall monitoring web application. Users can upload their own rain gauge observations and download others. 

This project was made at ITESO, in the context of the Professional Application Project (PAP) "4D08 Desarrollo tecnológico para la sustentabilidad ambiental, energética y alimentaria" guided by Prof. Hugo de Alba Martínez. To see live page go to http://hami1981.pythonanywhere.com/ 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Python 3
Pip
virtualenv

```
pip install virtualenv
```
Mysql


### Installing


* Clone this repository. 
```
git clone https://github.com/nachogoca/Rainfall.git
```

* Create a python virtual environment.
 ```
 virtualenv -p python3 rainfall_venv
 ```
* Install pip requirements.
```
pip install -r requirements.txt
```
* Install mysql and create user.
Consult: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04

* Change name of settings.py.template to settings.py and fill secret key and database information.

* Run python project.
```
python manage.py runserver
```

Go to http://localhost:8000/ to see running site.


## Deployment

To update in pythonanywhere server:
* Go to source folder
* Pull new changes from git
* Go to Web tab and click reload

## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - The web framework used
* [Djanog-leaflet](https://django-leaflet.readthedocs.io/en/latest/) - Used to show maps

## Contributing

Please send an email to hdealba@iteso.mx to make a contribution.


## Authors

* **José Ignacio González Cárdenas** - *Initial work* - [nachogoca](https://github.com/nachogoca)


## License

This project is licensed under the Creative Commons License.
