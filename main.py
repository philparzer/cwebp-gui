from webptools import grant_permission
from webptools import cwebp

grant_permission()
# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file type extension)
print(cwebp(input_image="test.png", output_image="test.webp",
            option="-q 80", logging="-v"))