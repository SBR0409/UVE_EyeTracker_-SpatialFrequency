from human import *

def solve_humanoid(gazeData, xsz = 1920, ysz = 1080):
    gaze_x, gaze_y, bxs, bys, bxe, bye = 100, 100, 50, 50, 150, 150

    humanoid_images_mouth = (0.0, -0.13, 0.21, 0.07)
    humanoid_images_eye = (0.0, 0.018, 0.29, 0.075)
    humanoid_images_nose = (0.0, -0.055, 0.2, 0.055)
    humanoid_images_forehead = (0.0, 0.1, 0.25, 0.066)

    normalised_humanoid_images_mouth = (normalize_coordinate(humanoid_images_mouth[0]), normalize_coordinate(humanoid_images_mouth[1]), humanoid_images_mouth[2], humanoid_images_mouth[3])
    normalised_humanoid_images_eye = (normalize_coordinate(humanoid_images_eye[0]), normalize_coordinate(humanoid_images_eye[1]), humanoid_images_eye[2], humanoid_images_eye[3])
    normalised_humanoid_images_nose = (normalize_coordinate(humanoid_images_nose[0]), normalize_coordinate(humanoid_images_nose[1]), humanoid_images_nose[2], humanoid_images_nose[3])
    normalised_humanoid_images_forehead = (normalize_coordinate(humanoid_images_forehead[0]), normalize_coordinate(humanoid_images_forehead[1]), humanoid_images_forehead[2], humanoid_images_forehead[3])

    bounds_humanoid_image_mouth = get_bounds(normalised_humanoid_images_mouth[0], normalised_humanoid_images_mouth[1], normalised_humanoid_images_mouth[2], normalised_humanoid_images_mouth[3])
    bounds_humanoid_image_eye = get_bounds(normalised_humanoid_images_eye[0], normalised_humanoid_images_eye[1], normalised_humanoid_images_eye[2], normalised_humanoid_images_eye[3])
    bounds_humanoid_image_nose = get_bounds(normalised_humanoid_images_nose[0], normalised_humanoid_images_nose[1], normalised_humanoid_images_nose[2], normalised_humanoid_images_nose[3])
    bounds_humanoid_image_forehead = get_bounds(normalised_humanoid_images_forehead[0], normalised_humanoid_images_forehead[1], normalised_humanoid_images_forehead[2], normalised_humanoid_images_forehead[3])

    humanoid_8_eyes_count = 0
    humanoid_8_nose_count = 0
    humanoid_8_forehead_count = 0
    humanoid_8_mouth_count = 0
    humanoid_8_other_count = 0
    humanoid_32_mouth_count = 0
    humanoid_32_eyes_count = 0
    humanoid_32_nose_count = 0
    humanoid_32_forehead_count = 0
    humanoid_32_other_count = 0
    humanoid_mouth_count = 0
    humanoid_eyes_count = 0
    humanoid_nose_count = 0
    humanoid_forehead_count = 0
    humanoid_other_count = 0


    scaled_humanoid_image_mouth = rescale(*bounds_humanoid_image_mouth, xsz, ysz)
    scaled_humanoid_image_eyes = rescale(*bounds_humanoid_image_eye, xsz, ysz)
    scaled_humanoid_image_nose = rescale(*bounds_humanoid_image_nose, xsz, ysz)
    scaled_humanoid_image_forehead = rescale(*bounds_humanoid_image_forehead, xsz, ysz)
            
            
    gaze = gazeData
    gaze_x = gaze[0]
    gaze_y = gaze[1]


    for i in gaze_x:
        if i == "LSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                    humanoid_8_eyes_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                    humanoid_8_nose_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                    humanoid_8_mouth_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                    humanoid_8_forehead_count+=1
                else:
                    humanoid_8_other_count+=1
        elif i == "HSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                    humanoid_32_eyes_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                    humanoid_32_nose_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                    humanoid_32_mouth_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                    humanoid_32_forehead_count+=1
                else:
                    humanoid_32_other_count+=1
        elif i == "BSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                    humanoid_eyes_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                    humanoid_nose_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                    humanoid_mouth_count+=1
                elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                    humanoid_forehead_count+=1
                else:
                    humanoid_other_count+=1
    
    total = humanoid_eyes_count + humanoid_nose_count + humanoid_mouth_count + humanoid_forehead_count + humanoid_other_count
    if total > 0:
        humanoid_eyes_count/=total
        humanoid_nose_count/=total
        humanoid_mouth_count/=total
        humanoid_forehead_count/=total
        humanoid_other_count/=total

    total = humanoid_8_eyes_count + humanoid_8_nose_count + humanoid_8_mouth_count + humanoid_8_forehead_count + humanoid_8_other_count
    if total > 0:
        humanoid_8_eyes_count/=total
        humanoid_8_nose_count/=total
        humanoid_8_mouth_count/=total
        humanoid_8_forehead_count/=total
        humanoid_8_other_count/=total

    total = humanoid_32_eyes_count + humanoid_32_nose_count + humanoid_32_mouth_count + humanoid_32_forehead_count + humanoid_32_other_count
    if total > 0:
        humanoid_32_eyes_count/=total
        humanoid_32_nose_count/=total
        humanoid_32_mouth_count/=total
        humanoid_32_forehead_count/=total
        humanoid_32_other_count/=total

    return ([humanoid_eyes_count, humanoid_nose_count, humanoid_mouth_count, humanoid_forehead_count, humanoid_other_count], [humanoid_8_eyes_count, humanoid_8_nose_count, humanoid_8_mouth_count, humanoid_8_forehead_count, humanoid_8_other_count], [humanoid_32_eyes_count, humanoid_32_nose_count, humanoid_32_mouth_count, humanoid_32_forehead_count, humanoid_32_other_count])

def plot_humanoid(gazeData):
    allData = solve_humanoid(gazeData)
    
    Legend = ["8", "32", "c"]
    X_labels = ["Eyes", "Nose", "Mouth", "Forehead", "Other"]
    X_axis = np.arange(len(X_labels))
    
    ListLow = allData[1]
    ListRafd = allData[0]
    ListHigh = allData[2]

    plt.bar(X_axis - 0.2, ListLow, 0.2, label = '8')
    plt.bar(X_axis + 0.0, ListHigh, 0.2, label = '32')
    plt.bar(X_axis + 0.2, ListRafd, 0.2, label = 'c')
    plt.title("Humanoid ROI Summary")
    plt.xticks(X_axis, X_labels)
    plt.legend(Legend)
    plt.show()

if __name__ == "__main__":
    plot_humanoid()