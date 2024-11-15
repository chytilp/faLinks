Spouští se:
```
$ poetry run poe app
```
Curl na post usera:
```
curl -d '{"name":"René", "email":"renda87@seznam.cz", "password": "op159tr"}' -H "Content-Type: application/json" -X POST http://localhost:8000/users/
```
Spuštění testů:
```
$ poetry run poe tests
```