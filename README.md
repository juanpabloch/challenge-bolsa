# challenge-bolsa
## Desafío Entrevista Técnica

```se utilizo sqlite que viene por defecto en django```
<br><br>
Creamos una carpeta para colocar el proyecto <br><br>
Creamos un ambiente virtual y lo activamos con el comando: `python -m venv VENV && .\VENV\Scripts\activate` <br><br>
Clonamos el repositorio <br><br>
Ingresamos a la carpeta challenge-bolsa <br><br>
Ejecutamos: `pip install -r requirements.txt` <br><br>
Una vez terminado vamos a ingresar a la carpeta api <br><br>
Debemos  crear un archivo .env:
- en la consola ejecutamos: `nano .env`
- pegamos: `SECRET_KEY='escribir-una-clave'`
- apretamos: ```ctrl + o``` para escribir el archivo | y luego ```enter``` para guardar
- para salir precionamos: ```ctrl + x``` <br><br>

Y ejecutamos: `python manage.py makemigrations && python manage.py migrate` <br><br>
Luego: `python manage.py runserver` <br><br>

## Esta es una api con un crud la cual retorna:
- `'/products'` GET: retorna una lista de productos
- `'/products'` POST: podemos agregar un producto nuevo, campos:
	- code : codigo del producto (texto menor a 10 caracteres)
	- buy : precio de compra (numero)
	- sell : precio de venta (numero)
	- description : descripcion (texto)

- `'/product/<product_code>` GET: retorna un producto por su codigo
- `'/product/<product_code>` POST: podemos modificar los campos buy y sell por el codigo del producto
- `'/product/<product_code>` DELETE: elimina el producto por el codigo

<br>

Los precios de los productos se van a actualizar cada 10 segundos, utilizamos la libreria `apscheduler`
se encuentra en `services/updater.py`


## Ahora vamos a ejecutar el servidor

En una nueva consola entramos a la carpeta `servidor` <br><br>
Debemos  crear un archivo .env:
- en la consola ejecutamos: `nano .env`
- pegamos: `SECRET_KEY='escribir-una-clave'`
- apretamos: ```ctrl + o``` para escribir el archivo | y luego ```enter``` para guardar
- para salir precionamos: ```ctrl + x``` <br><br>
y ejecutamos: `python manage.py makemigrations && python manage.py migrate`<br><br>
Luego: `python manage.py runserver`<br><br>
Ingresamos en el navegador a la direccion: `http://127.0.0.1:8000/`<br><br>
Nos va a mostrar una lista de productos, 
podemos ingresar y ver un producto en particular el mismo se va a actualizar cada 10 segundos mediente un websocket
