# Django Rest Project

Simple project featuring basic Rest API and Django 

## Description

Project contains 3 databases: Author, Books, Genres  
Authors and Genres are nested into Books, individual records can be accessed by writing id number at the end of url eg. `http://127.0.0.1:8000/catalog/Books/5`
Please note that project itself is in early stage of development and will server a wider purpose in the future.
Currently has been modified to utilize Rest, some of the models/functionality might not be connected.
## Getting Started

### Dependencies

* Project was designed on Windows 10 Home 64x 
* Python 3.10.0
* Django 3.2.9
* djangorestframework 3.12.4
### Installing

* Download all files into the same directory

### Testing
* Tested with 'Postman' site

### Executing program

* make sure to have all neccessary dependencies installed ( `pip install` )
* open terminal and execute manage.py file `...\> py manage.py runserver`
* open `http://127.0.0.1:8000/catalog/` in browser
* pick one of avaible links to see its content

## Help

Under any issues feel free to contact me directly

## Authors

me

## Version History
* 0.2
    * add comments, change directory to /catalog if no directory provided
* 0.1
    * Initial Release

## License

No idea

## Acknowledgments

* [official documentation](https://www.django-rest-framework.org/)
* [Utilized Video by Kacper Sieradziński](https://www.youtube.com/watch?v=Bo76ny5X38Y&t)
* [stackoverflow](https://stackoverflow.com/)
