## Crear un entorno virtual:

1. Abre Visual Studio Code.
2. Abre tu carpeta de proyecto o crea una nueva carpeta para tu proyecto.
3. Abre una nueva terminal en Visual Studio Code haciendo clic en "Terminal" en la barra de menú y luego en "Nueva Terminal".
4. En la terminal, ejecuta el siguiente comando para crear un entorno 

<blockquote>
<h4>Crear</h4>
<p>
python -m venv nombre_del_entorno

</p>
</blockquote>

Cuando creas en entorno en Visual Studio Code y accedes a un proyecto Python, a menudo se te preguntará si deseas activar el entorno virtual para ese proyecto. Generalmente, es recomendable aceptar esta opción, ya que activar el entorno virtual asegura que las bibliotecas y dependencias específicas del proyecto se utilicen correctamente

## Activar el entorno virtual:

En la misma terminal, ejecuta el comando adecuado según tu sistema operativo:


<blockquote>
<h4>En Windows:</h4>
<p>
nombre_del_entorno\Scripts\activate

**.\venv\Scripts\activate**

</p>
</blockquote>


<blockquote>
<h4>En macOS y Linux:</h4>
<p>
source nombre_del_entorno/bin/activate
</p>
</blockquote

## Instalar paquetes en el entorno virtual:

Una vez que el entorno virtual esté activado, puedes instalar paquetes utilizando pip, el gestor de paquetes de Python.Por ejemplo, para instalar un paquete llamado "nombre_paquete", ejecuta el siguiente comando en la terminal:

>
>pip install nombre_paquete
>

## Exportar los requisitos del proyecto:

Para exportar los requisitos de tu proyecto (es decir, los paquetes instalados junto con sus versiones), puedes utilizar el siguiente comando en la terminal:

> pip list

> pip freeze > requirements.txt

## Instalar los paquetes del archivo requirements.txt:

Una vez que hayas revisado los paquetes en el archivo requirements.txt, puedes instalarlos en un nuevo entorno virtual.

1. Primero, crea un nuevo entorno virtual siguiendo los pasos anteriores.

2. Activa el entorno virtual.

3. Ejecuta el siguiente comando en la terminal para instalar los paquetes especificados en el archivo requirements.txt:

> pip install -r requirements.txt

## Desactivar el entorno virtual:

Para desactivar el entorno virtual cuando hayas terminado de trabajar en tu proyecto, simplemente ejecuta el siguiente comando en la terminal:

> deactivate

Esto cerrará el entorno virtual y restaurará el entorno de Python global.
