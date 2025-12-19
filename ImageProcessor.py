from PIL import Image , ImageDraw, ImageFont, ImageFilter
from ImageHadler import ImageHandler
class ImageProcessor:
    def __init__(self, path):
        # Загрузка изображения
        self.proc_img = ImageHandler(path)
        self.proc_img.load()
        # Конвертируем в rgb для удобной работы
        self.image = self.proc_img.proc().convert("RGB")

    def text(self):
        # Загружаем шрифт и объявляем ,,Карандаш,, для нанесения текста
        pencil = ImageDraw.Draw(self.image)
        font = ImageFont.load_default()
        #Пишем "3 вариант " в центре изображение
        pencil.text((self.image.size[0]/2,self.image.size[1]/2), "Вариант 3", font=font, fill="white")
        #Обновление и сохранение изображения
        self.proc_img.img = self.image
        self.proc_img.save()

    def cont(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.proc_img.img = self.image
        self.proc_img.save()