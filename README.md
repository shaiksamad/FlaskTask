
# FlaskTask - CRUD APP and REST API

## Homepage (https://127.0.0.1:5000)
In homepage you can do basic CURD operation without API



### Screenshot

![Home Screenshot](https://github.com/shaiksamad/FlaskTask/blob/main/screenshots/Screenshot%202022-03-31%20213212.png?raw=true)


## API Reference

#### Create movie

```
  POST /api/movies/add
```
| Body   |  Type | Description                  |
| :----- | :---- | :--------------------------- |
| `data` | `JSON`| **Required**. data to insert.|

##### screenshot:

![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20210615.png)

when you add data it returns `id` of document.



### Read movie

```
GET /api/movies/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of movie to fetch |

here I used the `ID` of above inserted document.

##### screenshot:

![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20210715.png)


### Update movie

```
PUT /api/movies/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of movie to update |


here, I used the same above `ID` to change director name from 'SSR' to 'S.S.Rajamouli'

##### screenshot:

![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20210845.png)

##### screenshot: after updating

![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20210917.png)

### Delete movie

```
DELETE /api/movies/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of movie to delete |

##### screenshot:
![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20211037.png)

after deleting, if we search it shows 404 error
![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20211057.png)




### Get all movies list

```
GET /api/movies
```
##### screenshot:

![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20205906.png)

same screenshot in browser:
![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20211213.png)
#
MongoDB-cluster collections Screenshot:
![screenshot](https://raw.githubusercontent.com/shaiksamad/FlaskTask/main/screenshots/Screenshot%202022-03-31%20211627.png)
