from human import *

def solve_robotic(gazeData, xsz = 1920, ysz = 1080):
    robot_images_mouth = (0.0, -0.12, 0.29, 0.11)
    robot_images_eye = (0.0, 0.02, 0.34, 0.16)

    normalised_robot_images_mouth = (normalize_coordinate(robot_images_mouth[0]), normalize_coordinate(robot_images_mouth[1]), robot_images_mouth[2], robot_images_mouth[3])
    normalised_robot_images_eye = (normalize_coordinate(robot_images_eye[0]), normalize_coordinate(robot_images_eye[1]), robot_images_eye[2], robot_images_eye[3])

    bounds_robot_image_mouth = get_bounds(normalised_robot_images_mouth[0], normalised_robot_images_mouth[1], normalised_robot_images_mouth[2], normalised_robot_images_mouth[3])
    bounds_robot_image_eye = get_bounds(normalised_robot_images_eye[0], normalised_robot_images_eye[1], normalised_robot_images_eye[2], normalised_robot_images_eye[3])


    robot_8_mouth_count = 0
    robot_8_eyes_count = 0
    robot_8_other_count = 0
    robot_32_mouth_count = 0
    robot_32_eyes_count = 0
    robot_32_other_count = 0
    robot_mouth_count = 0
    robot_eyes_count = 0
    robot_other_count = 0


    scaled_robot_image_mouth = rescale(*bounds_robot_image_mouth, xsz, ysz)
    scaled_robot_image_eyes = rescale(*bounds_robot_image_eye, xsz, ysz)

    gaze = gazeData
    gaze_x = gaze[0]
    gaze_y = gaze[1]
    for i in gaze_x:
        if i == "LSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_robot_image_eyes)):
                    robot_8_eyes_count+=1
                elif (is_inside(x, y, *scaled_robot_image_mouth)):
                    robot_8_mouth_count+=1
                else:
                    robot_8_other_count+=1
        elif i == "HSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_robot_image_eyes)):
                    robot_32_eyes_count+=1
                elif (is_inside(x, y, *scaled_robot_image_mouth)):
                    robot_32_mouth_count+=1
                else:
                    robot_32_other_count+=1
        elif i == "BSF":
            for ii in range(len(gaze_x[i])):
                x, y = normalize_coordinateXY(gaze_x[i][ii], gaze_y[i][ii])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (is_inside(x, y, *scaled_robot_image_eyes)):
                    robot_eyes_count+=1
                elif (is_inside(x, y, *scaled_robot_image_mouth)):
                    robot_mouth_count+=1
                else:
                    robot_other_count+=1


    total = robot_eyes_count + robot_mouth_count + robot_other_count
    if total>0:
        robot_eyes_count/=total
        robot_mouth_count/=total
        robot_other_count/=total

    total = robot_8_eyes_count + robot_8_mouth_count + robot_8_other_count
    if total>0:
        robot_8_eyes_count/=total
        robot_8_mouth_count/=total
        robot_8_other_count/=total

    total = robot_32_eyes_count + robot_32_mouth_count + robot_32_other_count
    if total>0:
        robot_32_eyes_count/=total
        robot_32_mouth_count/=total
        robot_32_other_count/=total

    return ([robot_eyes_count, robot_mouth_count, robot_other_count], [robot_8_eyes_count, robot_8_mouth_count, robot_8_other_count], [robot_32_eyes_count, robot_32_mouth_count, robot_32_other_count])


def plot_robotic(gazeData):
    data = solve_robotic(gazeData)
    Legend = ["8", "32", "c"]
    X_labels = ["Eyes", "Mouth", "Other"]
    X_axis = np.arange(len(X_labels))
    ListLow = data[1]
    ListRafd = data[0]
    ListHigh = data[2]
    plt.bar(X_axis - 0.2, ListLow, 0.2, label = '8')
    plt.bar(X_axis + 0.0, ListHigh, 0.2, label = '32')
    plt.bar(X_axis + 0.2, ListRafd, 0.2, label = 'c')
    plt.title("Robot ROI Summary")
    plt.xticks(X_axis, X_labels)
    plt.legend(Legend)
    plt.show()

if __name__ == "__main__":
    plot_robotic()