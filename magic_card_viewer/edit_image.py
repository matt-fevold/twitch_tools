from PIL import Image, ImageFont, ImageDraw
import random
import string


class MagicImage:
    def __init__(self, image_path, name):
        self.image_path = image_path
        try:
            self.open_image = Image.open(self.image_path)
        except FileNotFoundError as e:
            print("File not found! {}".format(e))
            exit(-1)
        except IOError as e:
            print("Some IOError occurred! {}".format(e))
            exit(-1)

        self.name = name

    def crop_image(self):
        """
        crop the image to just the top part of the card.
        :return:
        """
        self.image_width = self.open_image.size[0]
        self.image_height = self.open_image.size[1]
        crop_tuple = (0, 0, self.image_width, self.image_height/5)
        self.open_image = self.open_image.crop(crop_tuple)

    def add_card_name(self):
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font-file should be present in provided path.
        font = ImageFont.truetype("./calibri.ttf", 64)

        draw = ImageDraw.Draw(self.open_image)
        # draw.text((x, y),"Sample Text",(r,g,b))
        print(self.image_width)
        white = (255, 255, 255)  # gotta do some stuff to find width and such
        draw.text((0, 20), self.name, white, font=font)

    def save_image(self, save_name):
        """
        save the open image
        :param save_name:
        :return:
        """
        try:
            self.open_image.save(save_name)
        except (KeyError, IOError) as e:
            print("Something went wrong saving the file! {}".format(e))

    def process_image(self):
        self.crop_image()
        self.add_card_name()
        self.save_image('./assets/' + self.name + "-cropped-" + self.id_generator() + '.jpg')

    def id_generator(self, size=6):
        """
        generate "random" string for unique id, used to avoid having to worry about duplicate name
        but probably not necessary
        :param size:
        :return:
        """
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    test = MagicImage("./assets/m19-71-scholar-of-stars.jpg", "Scholar Of Stars")
    test.process_image()
