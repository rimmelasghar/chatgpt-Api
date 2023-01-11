<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

<img src="https://staticg.sportskeeda.com/editor/2022/12/12ba3-16703270774402-1920.jpg" alt="Girl in a jacket" width="1000" height="250">

# 🤖 ChatGpt API (Un-Official)
This is an Unofficial Chat-GPT Api built with Flask & playwright.
This Flask Project act as a Wrapper around ChatGpt.
# ⚙️ Prerequisites

- You need to have python installed. You can install it from microsoft store or follow this [guide](https://www.geeksforgeeks.org/how-to-install-python-on-windows/).

# Setting up a Virtual Enviroment

It’s a common practice to have your Python apps and their instances running in virtual environments. Virtual environments allow different package sets and configurations to run simultaneously, and avoid conflicts due to incompatible package versions. 

Create a Virtual Enviroment in python by executing following command.
```bash
$ python3 -m venv env
```
activate the virtual environment.
```bash
# On Unix or MacOS (bash shell): 
/path/to/venv/bin/activate

# On Unix or MacOS (csh shell):
/path/to/venv/bin/activate.csh

# On Unix or MacOS (fish shell):
/path/to/venv/bin/activate.fish

# On Windows (command prompt):
\path\to\venv\Scripts\activate.bat

# On Windows (PowerShell):
\path\to\venv\Scripts\Activate.ps1
```

# Installation:
now install all the dependencies.
```bash
 $ pip install -r requirements.txt
```

# Working:
Thats it! You are ready to go. </br>
run the Project by executing this.
```bash
$ python3 chat.py
```

Project will be available on
``http://127.0.0.1:8000``

# API Reference

#### Get Response

```http
  GET /chat
```

#### Post Response

```http
  POST /chat/${q}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `q`      | `string` | **Required**. message that you want to pass  |


regenerate the Session
```http
  POST /regenerate/
```

reset the Session
```http
  POST /reset/
```


restart the Session
```http
  POST /restart/
```

# Demo
These are the Demo of the Api.
 - <a href="https://github.com/rimmelasghar/chatgpt-Api/blob/master/img/chatgpt-1.PNG">demo-1</a>
 - <a href="https://github.com/rimmelasghar/chatgpt-Api/blob/master/img/chatgpt-2.PNG">demo-2</a>
 - <a href="https://github.com/rimmelasghar/chatgpt-Api/blob/master/img/chatgpt-3.PNG">demo-3</a>
 - <a href="https://github.com/rimmelasghar/chatgpt-Api/blob/master/img/chatgpt-4.PNG">demo-4</a>
 - <a href="https://github.com/rimmelasghar/chatgpt-Api/blob/master/img/chatgpt-5.PNG">demo-5</a>
# Feedback
If you have any feedback, please reach out to me at  `rimmelasghar4@gmail.com` 


[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

```
print('Code by Rimmel with ❤')
```

