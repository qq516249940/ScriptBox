from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 将PDF文件转换为图片
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        # 保存每一页为PNG图片
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')

    print(f"PDF文件已转换为图片，并保存在文件夹: {output_folder}")

# 使用示例
pdf_path = 'example.pdf'  # 你的PDF文件路径
output_folder = 'output_images'  # 输出图片文件夹
pdf_to_images(pdf_path, output_folder)
