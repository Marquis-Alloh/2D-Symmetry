import cv2 as cv
  
def Img_Conv(img_source):
    '''
    This procedure will respond
    '''
    # read the image file
    img = cv.imread(img_source, 2)

    ret, bw_img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) #cv.THRESH_BINARY or  to make it binary



    cv.imshow("Binary", bw_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    name = str(input("provide a name for the image"))
    cv.imwrite('{}.jpg', img) # Save the image

def save_img(x):
    print("x")

    



