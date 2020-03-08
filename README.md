# python-safer-tests
this is the test set we use to verify changes in our downstream of the python-safer repo

get our latest downstream, and setup a python venv, then install requirments.txt
```bash
bash get-latest.sh
```
set any variables and uncomment which test you'd like to run against in app.py
```bash
python3 app.py
```
when done, cleanup dir
```bash
bash clean-up.sh
```
