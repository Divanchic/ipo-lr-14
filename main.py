# Кудлаш Иван
from ImageProcessor import ImageProcessor

# Запрос пути к изображению
img_path = input("Введите путь к изображению: ")

# Инициализация процессора изображений
proc = ImageProcessor(img_path)

# Пишем текст по-центру
proc.text()
