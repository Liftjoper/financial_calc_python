# Financial Calculator

Простой финансовый калькулятор на Python с функциями расчёта простых процентов, сложных процентов и налогов.

## Функции

- **calc_simple_interest(principal, annual_rate, years)** — расчёт простых процентов
- **calc_compound_growth(initial_amount, annual_rate, years, periods_per_year=1)** — расчёт сложных процентов с капитализацией
- **calc_tax_deduction(income, tax_percent)** — расчёт суммы налога

## Требования

- Python 3.10+
- uv (менеджер пакетов)

## Установка и запуск

### 1. Клонирование репозитория

git clone git@github.com:Liftjoper/financial_calc_python.git
cd financial_calc_python

2. Установка uv
Если у вас ещё нет uv, установите его:

bash
pip install uv
Или следуйте официальной инструкции: https://github.com/astral-sh/uv

3. Инициализация проекта
bash
uv init

4. Установка зависимостей
bash
uv add --dev pytest

5. Запуск тестов
bash
uv run pytest
Для подробного вывода:

bash
uv run pytest -v
