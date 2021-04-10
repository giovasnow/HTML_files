# ComeColegial

Tabla de contenidos

[1. Requisitos](#requisitos)

&nbsp; &nbsp;[1.2 Configuracion de variables de ambiente en Windows](#configuracion-de-variables-de-ambiente-para-windows)

[2. Django](#django)

&nbsp; &nbsp; [2.1 Instalacion](#instalacion)

&nbsp; &nbsp; [2.2 Dependencias](#dependencias)

&nbsp; &nbsp; [2.3 Estructura de archivos](#estructura-de-archivos)

&nbsp; &nbsp; [2.4 Como correr el proyecto localmente](#como-correr-el-proyecto-localmente)


## Requisitos
[Descargar Git](https://git-scm.com/)

[Descargar Github Desktop (app para simplificar el acceso a git con Github)](https://desktop.github.com/)

[Descargar Python 3.9.x](https://www.python.org/downloads/)

[Descargar SQL Server Developer Edition (servidor local)](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

[Descargar SQL Server Manage Studio (app para accesar servidor)](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)




Para verificar en el terminal si ya tienes instalado python, ejecutar la instruccion:

```
py
```

Si esta instalado correctamente, te abrira el terminal de Python. Si te dice la version `3.9.x` donde x puede ser cualquier numero, pues tienes la version correcta instalada. Para cerrar el terminal de Python ejecutar la instruccion: 

```
exit()
```

### Configuracion de variables de ambiente para Windows
Para configurar las variables de ambiente en la Windows:

1. Abrir Control panel y navegar a System and Security > System. 
2. Presionar Advanced system settings. 
3. En system properties, ir al tab de advanced.
4. Click environment variables. 
5. Bajo system variables, click Path. Abrira pantalla para editar variables de ambiente. En una nueva linea entrar la ruta en donde instalaste Python. Por ejemplo:
```
C:\Users\{tu-usario}\AppData\Local\Programs\Python\Python39
```
6. click Ok para salvar. Igual en las pantallas de Environment Variables y System Properties.
7. Si tienes algun terminal abierto, proceder a cerrarlo para que tome esta actualizacion.


Python 3.9.x ya viene con un package manager instalado llamado pip. Para verificar la version lo puedes hacer utilizando en el terminal la instruccion

```
pip --version
```

## Django
[Documentacion oficial (V3.2)](https://docs.djangoproject.com/en/3.2/)

### Instalacion

TODO

### Dependencias

[django-mssql-backend](https://pypi.org/project/django-mssql-backend/)

### Estructura de archivos

TODO

#### Proyecto vs Aplicacion

TODO

### Como correr el proyecto localmente

TODO


