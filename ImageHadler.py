from PIL import Image , ImageDraw, ImageFont
class ImageHandler:
    def __init__(self, path=None):
        self.path = path
        self.img = None

    #сохраняем изображение
    def save(self):
        self.img.save(self.path)

    #загружаем изображение
    def load(self):
        self.img=Image.open(self.path)
        self.img.load()

    # меняем размер изображения
    def changer(self):
        if self.img==None:# если изображение не объявлено то пишем об этом
            print("Изображение отсутсвует")
        else:
            print(f"В данный момент размер изображения {self.img.size}")
            x = int(input("Введите новый размер по x"))
            y = int(input("Введите новый размер по y"))
            if x >= 200 and y >= 200:
                self.img = self.img.resize((x,y))
                self.img.save(self.path, "changed")
            else:
                print("Слишком маленький размер")

    def proc(self):

        return self.img

