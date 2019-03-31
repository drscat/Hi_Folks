# Запуск

**Загрузить и перейти в проект**

```sh

# Клонируем проект
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

**Находясь в корне проекта запускаем**

```sh
docker build -t hifolks_flask_app:v0.1 flask_app/
```

# Переходим в директорию prometheus и запускаем docker-compose

**Выполняем**
```sh
cd prometheus/

# И запускаем

docker-compose up # добавляем -d если без отладки

```

# Grafana

**В браузере набираем "IP хоста:3000"**

**В "Data Sources" добавляем prometheus и в настройках указываем URL http://prometheus:9090**

**Имортируем дашборды, файл "All_added_manually-1553870058244.json"**


<!-- docker run -d -p 5000:5000 hifolks_flask_app:v0.1
docker run -itd --network=prometheus_two_monitor-net -d -p 5000:5000 hifolks_flask_app:v0.1 -->

# Minikube

**Добавляем переменные окружения Docker для Minikube с помощью команды minikube docker-env:**

```sh

# Переходим в корень проекта
cd ../../Hi_Folks/

# Содержимое проекта смотрим ls -1F
ls -1F # Просмотр файлов

All_added_manually-1553870058244.json # Дашбоард
flask_app/ # Dockerfile
prometheus/ # docker-compose
README.md # Описание

# Выполняем перед отправкой в Kubernetes
eval $(minikube docker-env)

# Собираем образ
docker build -t hifolks_flask_app:v0.1 flask_app/

kubectl run hifolks-flask-app --image=hifolks_flask_app:v0.1 --port=5000

kubectl expose deployment hifolks-flask-app --type=NodePort

curl $(minikube service hifolks-flask-app --url)
```

# Должны увидеть сообщение "Hi Folks"



# Продолжение следует...


<!-- docker image tag hifolks_flask_app:v0.1 $(minikube ip):30500/hifolks_flas
k_app:v0.1 -->

<!-- docker run -d -p 5000:5000 hifolks_flask_app:v0.1
docker run -itd --network=prometheus_two_monitor-net -d -p 5000:5000 hifolks_flask_app:v0.1 -->
