import xml.etree.ElementTree as ET
import os
import shutil

# configuring the paths
xml_path = r"E:\windows docs\IT\human-tracking\dataset\annotations.xml"
images_path = r"E:\windows docs\IT\human-tracking\dataset\images"
output_path = r"E:\windows docs\IT\human-tracking\dataset\yolo-dataset"

# setting image dimensions
image_width = 1280
image_height = 720

# train-test data split
split_frame = 35

# create folder structure
for folder in ['images/train', 'images/val', 'labels/train', 'labels/val']:
    os.makedirs(os.path.join(output_path, folder), exist_ok=True)

# parsing xml
tree = ET.parse(xml_path)
root = tree.getroot()

# looping through every track in the annotation
for track in root.findall('track'):
    label = track.get('label')
    class_id = 0 if label.lower() == 'person' else 1
    
    # looping through every box in every track to extract yolo information
    for box in track.findall('box'):
        frame = int(box.get('frame'))
        xtl = float(box.get('xtl'))
        xbr = float(box.get('xbr'))
        ytl = float(box.get('ytl'))
        ybr = float(box.get('ybr'))
        
        # converting to yolo format
        center_x = ((xtl + xbr) / 2) / image_width
        center_y = ((ytl + ybr) / 2) / image_height
        width = (xbr - xtl) / image_width
        height = (ybr - ytl) / image_height
        
        yolo_format = f'{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n'
        
        # separate training data from validation data
        train_data = 'train' if frame <= split_frame else 'val'
        
        # saving the label file
        label_file = os.path.join(output_path, f'labels/{train_data}/frame_{frame:06}.txt')
        with open(label_file, 'a') as f:
            f.write(yolo_format)
            
        # copying the images to matching folders
        img_name = f'frame_{frame:06}.png'
        src_img_path = os.path.join(images_path, img_name)
        dst_img_path = os.path.join(output_path, f'images/{train_data}', img_name)
        
        if os.path.exists(src_img_path):
            shutil.copy(src_img_path, dst_img_path)
        else:
            print('can\'t find image files')
            break
            
print('XML Conversion complete, YOLO Dataset Ready!')