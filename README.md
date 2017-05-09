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

To deploy in pythonanywhere follow the instructions.



## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
