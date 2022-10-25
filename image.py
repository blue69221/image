from PIL import Image
import os

for file in os.listdir('original'): # 讀取 original 裡的所有檔案
    if file.endswith('.png'): # 如果檔案名結尾為.png
        image_file = Image.open(os.path.join('original', file))
        image_file = image_file.convert('L') # 轉換成黑白
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))

# image_file = Image.open('image.png')
# print(type(image_file))
# image_file = image_file.convert('L') # 轉換成黑白
# image_file.save("result.png")

# 批次處理圖片轉成黑白
# for file in os.listdir('.'): # 把現在位置所有檔案列出
#     if file.endswith('.png'): # 如果檔案名結尾為.png
#         image_file = Image.open(file)
#         image_file = image_file.convert('L') # 轉換成黑白
#         image_file.save(file[:-4] + '_grey.png')

