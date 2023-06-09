# API for Key-Value storage powered by FastAPI

## Запуск

```
docker-compose up
```

## Экслуатация
![image.png](/example/1.png)


## Add key-value pairs to storage
```
curl -X 'POST' \
  'http://localhost:8080/api/v1/storage/json/write/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "hash":"9669919dc82685cbf2d5b003f85298e994f1725ace428e9c591c9e9c95719292",
    "number":"1",
    "bool":"False",
    "project":"telegram-devops-bot-dev",
    "version":"1.29.2"
}
'
```

## Get all key-value pairs from storage
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/storage/json/read/all/' \
  -H 'accept: application/json'
```

## Get specific value by key
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/storage/json/read/?key=hash' \
  -H 'accept: application/json'
```
