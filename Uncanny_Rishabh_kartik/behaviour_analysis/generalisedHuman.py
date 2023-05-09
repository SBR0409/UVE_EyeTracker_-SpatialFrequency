import pandas as pd
import os
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

# given a rectangle, check if a point is inside it
def is_inside(gaze_x, gaze_y, bxs, bys, bxe, bye):
    if gaze_x > bxs and gaze_x < bxe and gaze_y > bys and gaze_y < bye:
        return True
    else:
        return False

# function to convert size from center anchor and position to x and y bounds
def get_bounds(center_x, center_y, width, height):
    bxs = center_x - width/2
    bys = center_y - height/2
    bxe = center_x + width/2
    bye = center_y + height/2
    return (bxs, bys, bxe, bye)

def normalize_coordinate(val):
    return (val+1)/2

# normalize the coordinate
def normalize_coordinateXY(x, y):
    return (x+1)/2, (y+1)/2

def rescale(bxs, bys, bxe, bye, image_width, image_height):
    return bxs*image_width, bys*image_height, bxe*image_width, bye*image_height

def rescaleXY(x, y, image_width, image_height):
    return x*image_width, y*image_height


def solve_human(gazeData, xsz = 1920, ysz = 1080):
    gaze_x, gaze_y, bxs, bys, bxe, bye = 100, 100, 50, 50, 150, 150

    human_images_mouth = (0.0, -0.028, 0.12, 0.04)
    human_images_eye = (0.008, 0.053, 0.18, 0.035)
    human_images_nose = (0.0, 0.013, 0.1, 0.036)
    human_images_forehead = (0.008, 0.1, 0.17, 0.045)

    normalised_human_images_mouth = (normalize_coordinate(human_images_mouth[0]), normalize_coordinate(human_images_mouth[1]), human_images_mouth[2], human_images_mouth[3])
    normalised_human_images_eye = (normalize_coordinate(human_images_eye[0]), normalize_coordinate(human_images_eye[1]), human_images_eye[2], human_images_eye[3])
    normalised_human_images_nose = (normalize_coordinate(human_images_nose[0]), normalize_coordinate(human_images_nose[1]), human_images_nose[2], human_images_nose[3])
    normalised_human_images_forehead = (normalize_coordinate(human_images_forehead[0]), normalize_coordinate(human_images_forehead[1]), human_images_forehead[2], human_images_forehead[3])

    bounds_human_image_mouth = get_bounds(normalised_human_images_mouth[0], normalised_human_images_mouth[1], normalised_human_images_mouth[2], normalised_human_images_mouth[3])
    bounds_human_image_eye = get_bounds(normalised_human_images_eye[0], normalised_human_images_eye[1], normalised_human_images_eye[2], normalised_human_images_eye[3])
    bounds_human_image_nose = get_bounds(normalised_human_images_nose[0], normalised_human_images_nose[1], normalised_human_images_nose[2], normalised_human_images_nose[3])
    bounds_human_image_forehead = get_bounds(normalised_human_images_forehead[0], normalised_human_images_forehead[1], normalised_human_images_forehead[2], normalised_human_images_forehead[3])

    human_8_mouth_count = 0
    human_8_eyes_count = 0
    human_8_nose_count = 0
    human_8_forehead_count = 0
    human_8_other_count = 0
    human_32_mouth_count = 0
    human_32_eyes_count = 0
    human_32_nose_count = 0
    human_32_forehead_count = 0
    human_32_other_count = 0
    human_mouth_count = 0
    human_eyes_count = 0
    human_nose_count = 0
    human_forehead_count = 0
    human_other_count = 0

    gaze = gazeData
    gaze_x = gaze[0]
    gaze_y = gaze[1]

    scaled_human_image_mouth = rescale(*bounds_human_image_mouth, xsz, ysz)
    scaled_human_image_eyes = rescale(*bounds_human_image_eye, xsz, ysz)
    scaled_human_image_nose = rescale(*bounds_human_image_nose, xsz, ysz)
    scaled_human_image_forehead = rescale(*bounds_human_image_forehead, xsz, ysz)

    for i in gaze_x:
        if i == "LSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                # print(x, y)
                if (is_inside(x, y, *scaled_human_image_eyes)):
                    human_8_eyes_count+=1
                elif (is_inside(x, y, *scaled_human_image_nose)):
                    human_8_nose_count+=1
                elif (is_inside(x, y, *scaled_human_image_mouth)):
                    human_8_mouth_count+=1
                elif (is_inside(x, y, *scaled_human_image_forehead)):
                    human_8_forehead_count+=1
                else:
                    human_8_other_count+=1
        elif i == "HSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_human_image_eyes)):
                    human_32_eyes_count+=1
                elif (is_inside(x, y, *scaled_human_image_nose)):
                    human_32_nose_count+=1
                elif (is_inside(x, y, *scaled_human_image_mouth)):
                    human_32_mouth_count+=1
                elif (is_inside(x, y, *scaled_human_image_forehead)):
                    human_32_forehead_count+=1
                else:
                    human_32_other_count+=1
        elif i == "BSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_human_image_eyes)):
                    human_eyes_count+=1
                elif (is_inside(x, y, *scaled_human_image_nose)):
                    human_nose_count+=1
                elif (is_inside(x, y, *scaled_human_image_mouth)):
                    human_mouth_count+=1
                elif (is_inside(x, y, *scaled_human_image_forehead)):
                    human_forehead_count+=1
                else:
                    human_other_count+=1

    total = human_eyes_count + human_nose_count + human_mouth_count + human_forehead_count + human_other_count
    if (total > 0):
        human_eyes_count/=total
        human_nose_count/=total
        human_mouth_count/=total
        human_forehead_count/=total
        human_other_count/=total

    total = human_8_eyes_count + human_8_nose_count + human_8_mouth_count + human_8_forehead_count + human_8_other_count
    if (total > 0):
        human_8_eyes_count/=total
        human_8_nose_count/=total
        human_8_mouth_count/=total
        human_8_forehead_count/=total
        human_8_other_count/=total

    total = human_32_eyes_count + human_32_nose_count + human_32_mouth_count + human_32_forehead_count + human_32_other_count
    if (total > 0): 
        human_32_eyes_count/=total
        human_32_nose_count/=total
        human_32_mouth_count/=total
        human_32_forehead_count/=total
        human_32_other_count/=total

    return ([human_eyes_count, human_forehead_count, human_mouth_count, human_nose_count, human_other_count], [human_8_eyes_count, human_8_forehead_count, human_8_mouth_count, human_8_nose_count, human_8_other_count], [human_32_eyes_count, human_32_forehead_count, human_32_mouth_count, human_32_nose_count, human_32_other_count])

def plot_human(gazeData, flag = True):
    if flag:
        allData = solve_human(gazeData)
    else:
        allData = gazeData
    Legend = ["8", "32", "Rafd"]
    X_labels = ["Eyes", "Nose", "Mouth", "Forehead", "Other"]
    X_axis = np.arange(len(X_labels))
    ListLow = allData[1]
    ListRafd = allData[0]
    ListHigh = allData[2]
    plt.bar(X_axis - 0.2, ListLow, 0.2, label = '8')
    plt.bar(X_axis + 0.0, ListHigh, 0.2, label = '32')
    plt.bar(X_axis + 0.2, ListRafd, 0.2, label = 'Rafd')
    plt.title("Human ROI Summary")
    plt.xticks(X_axis, X_labels)
    plt.legend(Legend)
    plt.show()


if __name__ == '__main__':
    plot_human()