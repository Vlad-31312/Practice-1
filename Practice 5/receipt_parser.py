import re
import json

# -------------------------
# 1. Читаем файл
# -------------------------
with open("raw.txt.txt", "r", encoding="utf-8") as file:
    text = file.read()


# -------------------------
# 2. Ищем дату и время
# -------------------------
date_match = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)

if date_match:
    date_time = date_match.group()
else:
    date_time = None


# -------------------------
# 3. Ищем способ оплаты
# -------------------------
payment_match = re.search(r"Банковская карта|Наличные", text)

if payment_match:
    payment_method = payment_match.group()
else:
    payment_method = None


# -------------------------
# 4. Ищем итоговую сумму
# -------------------------
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)

if total_match:
    total_str = total_match.group(1)
    
    # убираем пробелы
    total_str = total_str.replace(" ", "")
    
    # меняем запятую на точку
    total_str = total_str.replace(",", ".")
    
    # превращаем в число
    total = float(total_str)
else:
    total = None


# -------------------------
# 5. Ищем товары
# -------------------------
products = re.findall(r"\d+\.\n(.+)", text)


# -------------------------
# 6. Ищем суммы по позициям
# -------------------------
item_totals_raw = re.findall(r"\n([\d\s]+,\d{2})\nСтоимость", text)

clean_item_totals = []

for price in item_totals_raw:
    
    # убираем пробелы
    price_no_spaces = price.replace(" ", "")
    
    # меняем запятую на точку
    price_with_dot = price_no_spaces.replace(",", ".")
    
    # переводим в число
    number = float(price_with_dot)
    
    # добавляем в новый список
    clean_item_totals.append(number)

item_totals = clean_item_totals


# -------------------------
# 7. Считаем сумму сами
# -------------------------
calculated_sum = 0

for number in item_totals:
    calculated_sum += number


# -------------------------
# 8. Собираем результат
# -------------------------
data = {
    "date_time": date_time,
    "payment_method": payment_method,
    "receipt_total": total,
    "calculated_sum": calculated_sum,
    "products": products
}


# -------------------------
# 9. Красивый вывод JSON
# -------------------------
print(json.dumps(data, indent=4, ensure_ascii=False))