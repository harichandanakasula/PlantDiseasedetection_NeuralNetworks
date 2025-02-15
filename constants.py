background_path = r'C:\Users\mdhim\Videos\PDD\bg2.jpg'
model_path = 'vision_transformer_image_classifier.pth'

# Load your model and class names
class_names = ['Apple__Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple_healthy', 'Blueberry_healthy', 'Cherry(including_sour)Powdery_mildew', 'Cherry(including_sour)healthy', 'Corn(maize)Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)Common_rust', 'Corn_(maize)Northern_Leaf_Blight', 'Corn(maize)healthy', 'Grape_Black_rot', 'Grape_Esca(Black_Measles)', 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)', 'Grape__healthy', 'Orange_Haunglongbing(Citrus_greening)', 'Peach__Bacterial_spot', 'Peach_healthy', 'Pepper,_bell_Bacterial_spot', 'Pepper,_bell_healthy', 'Potato_Early_blight', 'Potato_Late_blight', 'Potato_healthy', 'Raspberry_healthy', 'Soybean_healthy', 'Squash_Powdery_mildew', 'Strawberry_Leaf_scorch', 'Strawberry_healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites Two-spotted_spider_mite', 'Tomato_Target_Spot', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_Tomato_mosaic_virus', 'Tomato__healthy']
num_classes = len(class_names)


disease_remedies = {
    'Apple__Apple_scab': 'Apply fungicide containing chlorothalonil or mancozeb and prune infected areas.',
    'Apple_Black_rot': 'Prune and destroy infected parts; apply fungicide containing boscalid or pyraclostrobin.',
    'Apple_Cedar_apple_rust': 'Remove galls; apply fungicide containing myclobutanil or propiconazole.',
    'Apple_healthy': 'No remedy needed, plant is healthy.',
    'Blueberry_healthy': 'No remedy needed, plant is healthy.',
    'Cherry(including_sour)Powdery_mildew': 'Apply fungicide containing sulfur or potassium bicarbonate, improve air circulation.',
    'Cherry(including_sour)healthy': 'No remedy needed, plant is healthy.',
    'Corn(maize)Cercospora_leaf_spot Gray_leaf_spot': 'Use disease-resistant varieties, apply fungicides containing chlorothalonil or azoxystrobin.',
    'Corn(maize)Common_rust': 'Plant resistant varieties, apply fungicides containing azoxystrobin or pyraclostrobin early.',
    'Corn_(maize)Northern_Leaf_Blight': 'Rotate crops, use resistant varieties, apply fungicides containing chlorothalonil or fludioxonil.',
    'Corn(maize)healthy': 'No remedy needed, plant is healthy.',
    'Grape_Black_rot': 'Prune affected areas, apply fungicide containing boscalid or fenhexamid.',
    'Grape_Esca(Black_Measles)': 'Prune and destroy infected parts and ensure proper vineyard management, apply fungicide.',
    'Grape__Leaf_blight(Isariopsis_Leaf_Spot)': 'Prune affected leaves, apply fungicide containing myclobutanil or trifloxystrobin.',
    'Grape__healthy': 'No remedy needed, plant is healthy.',
    'Orange_Haunglongbing(Citrus_greening)': 'Remove infected trees, control psyllid vectors.',
    'Peach__Bacterial_spot': 'Prune affected parts, apply copper-based fungicide or streptomycin for bacterial spot control.',
    'Peach_healthy': 'No remedy needed, plant is healthy.',
    'Pepper,_bell_Bacterial_spot': 'Remove infected plants, apply copper-based fungicides or streptomycin for bacterial spot control.',
    'Pepper,_bell_healthy': 'No remedy needed, plant is healthy.',
    'Potato_Early_blight': 'Remove affected leaves, apply fungicides containing chlorothalonil or mancozeb.',
    'Potato_Late_blight': 'Remove and destroy affected plants, apply fungicides containing chlorothalonil or fluazinam.',
    'Potato_healthy': 'No remedy needed, plant is healthy.',
    'Raspberry_healthy': 'No remedy needed, plant is healthy.',
    'Soybean_healthy': 'No remedy needed, plant is healthy.',
    'Squash_Powdery_mildew': 'Apply fungicides containing sulfur or potassium bicarbonate, improve air circulation.',
    'Strawberry_Leaf_scorch': 'Remove infected leaves, apply fungicides containing myclobutanil or trifloxystrobin.',
    'Strawberry_healthy': 'No remedy needed, plant is healthy.',
    'Tomato_Bacterial_spot': 'Remove and destroy infected plants, apply copper-based fungicides or streptomycin for bacterial spot control.',
    'Tomato_Early_blight': 'Remove affected leaves, apply fungicides containing chlorothalonil or mancozeb.',
    'Tomato_Late_blight': 'Remove and destroy infected plants, apply fungicides containing chlorothalonil or fluazinam.',
    'Tomato_Leaf_Mold': 'Improve air circulation, apply fungicides containing chlorothalonil or mancozeb.',
    'Tomato_Septoria_leaf_spot': 'Remove infected leaves, apply fungicides containing chlorothalonil or azoxystrobin.',
    'Tomato_Spider_mites Two-spotted_spider_mite': 'Use insecticidal soap, miticide to control spider mitesneem oil; improve humidity levels.',
    'Tomato_Target_Spot': 'Remove infected leaves, apply fungicides containing chlorothalonil or boscalid.',
    'Tomato_Tomato_Yellow_Leaf_Curl_Virus': 'Control whiteflies, remove infected plants.',
    'Tomato_Tomato_mosaic_virus': 'Remove infected plants, control aphids.',
    'Tomato__healthy': 'No remedy needed, plant is healthy.'
}