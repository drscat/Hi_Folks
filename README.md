# Запуск

** Загрузить и перейти в проект  **

```sh

# Клогируем проект
git clone https://github.com/drscat/Hi_Folks.git

# Переходим в проект
cd Hi_Folks/

# Содержимое проекта смотрим ls -1F
ls -1F # Просмотр файлов

All_added_manually-1553870058244.json # Дашбоард
flask_app/ # Dockerfile
prometheus/ # docker-compose
README.md # Описание
```

# Собираем Dockerfile

** Находясь в корне проекта запускаем**

```sh
docker build -t hifolks_flask_app:v0.1 flask_app/
```

# Переходим в prometheus и запускаем docker-compose

** Выполняем **
```sh
cd prometheus/

```
<!-- docker run -d -p 5000:5000 hifolks_flask_app:v0.1
docker run -itd --network=prometheus_two_monitor-net -d -p 5000:5000 hifolks_flask_app:v0.1 -->
