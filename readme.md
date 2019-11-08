## jwt ... ?

### how to start
```
git clone https://github.com/h4ppyy/zero-jwt
cd zero-jwt
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```
### let's start
http://127.0.0.1:8000

### curl test (regist)
```bash
curl -XPOST http://127.0.0.1:8000/api/v1/regist -H 'Content-Type: application/json' -d '{"user_id":"your_id", "user_pw":"your_password"}'
```
