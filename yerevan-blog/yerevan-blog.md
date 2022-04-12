# Info
Task goal is to get access to the server
Frontend is nearly useless
# Steps 
## 1 research
- main page is useless
- using intuition/[[dirsearch]]/[[gobuster]]   find directories
```paths
/dashboard
/users
 ```
## 2 reach panel
- `/dashboard` and `/users` have [[JavaScript|JS]] that rediects to the `/`
- quick reversing give us an understanding that it checks for `admin` cookie
- to bypass the check we need to add it manually or ignore the [[JavaScript|JS]] source
	```
	cookies="admin=true"
	```
## 3 analyse `/users`
- here we can find only two interaction methods
	1. regenerate qr code
	2. request qr code via [[GET reques]]
- now lets focuse on GET request
## 4 vulnerable `/get_qr`
- it took filename as a parameter
- let's request some source, like [[CSS]] from a server to be sure 
	_path is optained from source of a page_
	```
	<domain>/get_qr?uname=../static/css/somecss
	```
- So we have a __[[Directory traversal]]__ vulnerability
## 5 get source code 
- we need to know __which file to steal__
- lets get [[enviroment|ENV]]
	_`../` used to reach root. Probably absolute path work as well_
	```
	../../../../../../../proc/self/enveron
	```
- here we know that there is [[python]] installed
- grab the `requirements.txt` from root directory of an app
- now we sure that it is a __flask application__
- __standart__ name for [[flask]] app is `app.py` or `main.py`
- use `/get_qr` to steal `main.py`
## 6 analyse the source code 
- here we see that not to much to interact with
- but `generate_qr` take a part of a filename as a [[command line]] parameter
- also the filenames are concatinated
- so we need to pass a command splitted into chunks and rise a shell
- [[innoctf-yerevan-blog-exploit.py]]
## 7 grab flag
- using a [[shell]] reach a flag
- submit it
- __you are awesome!__

 
