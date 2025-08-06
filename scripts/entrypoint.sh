#!/bin/sh
set -e

echo "Начало инициализации базы данных..."

# Подождем некоторое время, чтобы убедиться, что сеть готова
echo "Подождем 5 секунд, чтобы убедиться, что сеть готова..."
sleep 5

echo "Создаём миграции..."
python manage.py makemigrations --noinput

echo "Применяем миграции..."
python manage.py migrate --noinput

echo "Собираем статические файлы..."
python manage.py collectstatic --noinput

# Выполнение команды, переданной в docker-compose
exec "$@"
