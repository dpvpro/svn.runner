### Комментарии:

В `svn_urls.txt` нужно поместить ссылки на `svn` репозитории и запустить скрипт `svn_runner.py`.

Для `rest_api.py` нужно поставить зависимости:

```
pip3 install flask flask_restful sqlalchemy
```

Это было тестовое задание в `OpenWay`.

### HowTo:

Перейти в папку с проектом. Установить uv `yay -S uv`.

```
uv python install cpython-3.12.10-linux-x86_64-gnu
uv venv -p python312 venv
uv pip install flask flask_restful sqlalchemy
rm test.db
```

`python svn_runner.py` - для инициализации базы данных.

`python rest_api.py` - для запуска API.

Пример вызова API, в браузере выполнить:

```
http://127.0.0.1:5002/listbyperiod/2018-07-28/2018-07-29
```
