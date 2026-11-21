# Участники и распределение задач

Лабораторная работа № 2 «Ветвление и проверка изменений».

Группа: ФТ(м)-61.

## Состав команды

| Участник                       | Основная задача         | Направление работы       |
| ------------------------------ | ----------------------- | ------------------------ |
| Оболонский Дмитрий Сергеевич   | Маршрут /about и тест   | Маршруты и тесты         |
| Кулешов Виталий Константинович | Маршрут /health и тест  | Проверка PR и интеграция |
| Назаренко Данила Вадимович     | Маршрут /version и тест | CI и выпуск              |

## Проверка изменений

- Дмитрий проверяет Pull Request Виталия.
- Виталий проверяет Pull Request Данилы.
- Данила проверяет Pull Request Дмитрия.

Каждый участник создаёт собственную feature-ветку,
пишет код и тест, обновляет README.md и отправляет
изменения через Pull Request.

После первой итерации участники меняют направления
работы и выполняют дополнительную проверку или
исправление.

## Доказательства выполнения

**Оболонский Дмитрий Сергеевич**

- Разработка маршрута `/about` и соответствующего теста: [Pull Request #4](https://github.com/animeybe/flask-review-lab2/pull/4).
- Проверка изменений Виталия: [Pull Request #6](https://github.com/animeybe/flask-review-lab2/pull/6).

**Кулешов Виталий Константинович**

- Разработка маршрута `/health` и соответствующего теста: [Pull Request #6](https://github.com/animeybe/flask-review-lab2/pull/6).
- Проверка изменений Данилы: [Pull Request #9](https://github.com/animeybe/flask-review-lab2/pull/9).

**Назаренко Данила Вадимович**

- Разработка маршрута `/version` и соответствующего теста: [Pull Request #9](https://github.com/animeybe/flask-review-lab2/pull/9).
- Проверка изменений Дмитрия: [Pull Request #4](https://github.com/animeybe/flask-review-lab2/pull/4).

**Общие результаты команды**

- Демонстрация конфликта изменений в `README.md`: [Pull Request #7](https://github.com/animeybe/flask-review-lab2/pull/7) и [Pull Request #8](https://github.com/animeybe/flask-review-lab2/pull/8).
- Демонстрация неуспешной проверки тестов и последующего исправления: [Pull Request #10](https://github.com/animeybe/flask-review-lab2/pull/10).
- Автоматическая проверка проекта: [GitHub Actions](https://github.com/animeybe/flask-review-lab2/actions).
- Подготовка стабильной версии: [Pull Request #11](https://github.com/animeybe/flask-review-lab2/pull/11).
- Выпуск версии: [тег v0.1.0](https://github.com/animeybe/flask-review-lab2/releases/tag/v0.1.0).
- Исправление документации: Pull Request из ветки `feature/readme-cleanup` в `development`.

Итоговый отчёт будет содержать таблицу личного вклада и результаты работы каждого участника.
