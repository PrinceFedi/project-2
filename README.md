# UOCIS322 - Project 2 #

This project will get you started with Docker and Flask. You need to have Docker set up on your machine to complete this
project. You can alternatively use the machine we talked about in class.

## Getting started

* Go to `web/`. Read every line of the docker file and the simple flask app.

* Build the simple flask app image using

  ```
  docker build -t some-image-name .
  ```
  **Make sure to use a unique name if you're running on testium.**
* Run the container using

  ```
  docker run -d -p 5001:5000 some-image-name
  ```

* Launch `http://hostname:5001` using your web browser and check the output "UOCIS docker demo!".<br>
  **Q:** What's `5001` and what's `5000`?<br>
  **A:** the `-p` argument opens a container port to another on your local machine. Think of the container as its own
  separate machine, and assume you start a web server on port `5000` there. To access the web server from your machine,
  you forward container's `5000` to YOUR `5001`.<br>
  To understand this better, try chaning the `5001` when starting your container, or `5000`. But remember, `5000` should
  be the port Flask uses (see `web/app.py`).

## Tasks

The goal of this project is to implement a "file checking" logic, while also adding configuration reading to your Python
script.

* If a file exists in `web/pages/` (i.e. `trivia.html`, any name, any extention or format) exists, transmit `200/OK`
  header followed by that file. If the file doesn't exist, transmit an error code in the header along with the
  appropriate page html in the body. You'll do this by creating error handlers. You'll also create the following two
  html files with the error messages:
    * `web/pages/404.html` will display "File not found!"
    * `web/pages/403.html` will display "File is forbidden!"

  ⚠️ NOTE: if a request contains illegal characters (`..` or `~`), the response should be 403.

* Add a configuration parsing logic (like project 0) to `app.py` so that it looks for `credentials.ini`, and if not
  found `default.ini`, and reads the port number and debug mode from the file found.

* Update your name and email in `Dockerfile`. Update `README` with your name, info, and a brief description of the
  project.

* You will submit your credentials.ini in Canvas. It should include your name and repo URL.


* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Details

### Background:

The logic implemented in this project was built upon refactoring code from the previous projects to incorporate the web
application
framework flask.

### app.py:

#### hello:

The flask web frameworks allows us to significantly reduces our code from our previous project without worrying about
low-level details such as protocol, thread management and other dependencies.
In this module, a single method called hello.py. This method takes the given input of a request taken from the
Flask decorator `app.route` which ties the root URL to the `hello` function. Therefore, when the user goes to the root
URL at the specified port, the `hello` function is automatically invoked. After this the `hello` method test the
validity of the request as follows:

1. Does the request contain illegal characters?
    1. If this is the case then, our method will raise an exception using the `abort` method. This exception is
       specified as a 403 error in which will trigger our `forbidden` method. Our forbidden method will then transmit a
       html file designed to represent a 403 error.
2. Is the File invalid or not found?
   1. If the file does not exist similar to the logic above, `hello` will raise a 404 error using `abort`. From there it will be sent to our `not_found` method which transmits a html files designed to show a 404 error

If both cases are false we have a valid request, and the specified file will be transmitted the port ran from the docker container.


#### Configuration parsing logic:

Similar to project 0, we needed to implement logic that will look for credentials.ini, and if not found default.ini, and reads the port number and debug mode from the file found. In order to build this, I used the `parse_config` method. This function checks if any of the files we specify exist, and use the first one that does.
From there at the module level I created a list variable of the needed files (`credentials.ini`, `default.ini`) and set them to the `config_paths` parameter in the `parse_config` method so that it would check for those two files. After the valid file was parsed and configured, I would access its `Server` key to get the specified `Port` number
as well as the `debug` mode. The app module is also the main program being run by our interpreter, so we use the code:
`if __name__ == "__main__":` to designate it as such. Under this condition, we run our application, type casting the string values received from accessing are .ini file keys, and filling them in as the correct parameters for flask's `run` method.


### Notes:

* Html and css source code was inspired through a tutorial. Modifications were carefully made to fit the project's description. Credit is given in the html files and the link can be found here: https://www.youtube.com/watch?v=m7ZZNsa0pOA


## Authors

Fedi Aniefuna
