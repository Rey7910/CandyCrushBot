from PIL import Image
import imagehash

# Cargar las imágenes
image1 = Image.open('game194.png')
image2 = Image.open('game195.png')

# Calcular los hashes de las imágenes
hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

# Comparar los hashes
if hash1 == hash2:
    print("Las imágenes son iguales o muy similares.")
else:
    print("Las imágenes son diferentes.")