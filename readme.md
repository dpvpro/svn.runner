### Комментарии:

В `svn_urls.txt` нужно поместить ссылки на `svn` репозитории и запустить скрипт `svn_runner.py`.

Разработка велась на debian-подобной системе. Для `rest_api.py` нужно поставить зависимости:

```
sudo -H pip3 install flask flask_restful sqlalchemy
```

Пример вызова API - `http://127.0.0.1:5002/listbyperiod/2018-07-28/2018-07-29`.

Это было тестовое задание в `OpenWay`.
