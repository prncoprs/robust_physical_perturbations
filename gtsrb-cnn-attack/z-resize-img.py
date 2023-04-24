import cv2

def resize_image(input_img, output_img, new_width, new_height):
    # Read the input image
    image = cv2.imread(input_img)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Save the resized image
    cv2.imwrite(output_img, resized_image)

input_img = "./printed_images/Sign_Stop-usstop-l1rectangles-less-256-epoch-999-noresize.png"
output_img = "./printed_images/Sign_Stop-usstop-l1rectangles-less-256-epoch-999-original-size.png"
new_width, new_height = 512, 512

resize_image(input_img, output_img, new_width, new_height)
