import os
# Style Models Data
style_models_file = ['candy.t7', 'Fire_Style_22000_Iterations.t7', 'flame_style_iter_500.t7', 'gold_black_2000.t7', 'landscape_style_5700.t7', 'pink_style_2000.t7', 'starry_night_2500.t7']
style_models_name = ['Candy', 'Fire_style', 'flame_style', 'Gold Black', 'Landscape', 'pink_style', 'starry_night']
model_path = 'models'

style_models_dict = {name: os.path.join(model_path, filee) for name, filee in zip(style_models_name, style_models_file)}

# Style Images Data

content_images_file = ['hug-kiss-images.jpg', 'jagannath.jpg', 'odisha_temple.jpg', 'odisha_tribe.jpg', 'pooja_lv.jpg', 'radha_krishna.jpg', 'rathyatra.jpg', 'v.jpg']

content_images_name = ['Hug', 'Jai Jagannath', 'Odisha Temple', 'Odisha Tribe', 'Pooja Mylv', 'Radhakrishna', 'Rathayatra Puri', 'Nani']

images_path = 'images'

content_images_dict = {name: os.path.join(images_path, filee) for name, filee in zip(content_images_name, content_images_file)}