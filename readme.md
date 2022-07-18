# DJANGO REST API + MONGO-DB

## INSTALL 
    git clone https://github.com/ismael-rodrigo/django-mongo-db.git

    cd django-mongo-db

    pip install -r requirements.txt

# RUN APP

    python managa.py runserver


---
&nbsp;
# ENDPOINTS
| endpoint | method | Descript |
| :--- | :--- | :--- |
| `api/product`   |   `GET , POST`   | Products |

&nbsp;
---
&nbsp;
# Products
## list Products

### Request

`GET api/product`

### Response

```javascript
[
	{
		"_id": {
			"$oid": id
		},
		"name": str,
		"tamanho": int,
		"valor": float
	},
]
```
&nbsp;
&nbsp;
## Create new Product

### Request

`POST api/product`



| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `name` | `string` | **Required**. Name of product |
| `tamanho` | `int` | **Required**. Lenth of product |
| `valor` | `float` | **Required**. Price of product |

### Response

```javascript
{
	"_id": id
}
```