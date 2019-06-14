from PIL import Image
import sys
def fill_image(image):
    width, height = image.size    
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')    
    if width > height:
        new_image.paste(image, (0,                      int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2),0))    
    return new_image

def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []    
    for i in range(0,3):
        for j in range(0,3):           
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]    
    return image_list

def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.jpg')
        index += 1

if __name__ == '__main__':
    file_path = "1.jpg"
    image = Image.open(file_path)   
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)