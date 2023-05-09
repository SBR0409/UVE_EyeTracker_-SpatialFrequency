from human import *

def solve_robotic():
    gaze_x, gaze_y, bxs, bys, bxe, bye = 100, 100, 50, 50, 150, 150

    robot_images_mouth = (0.0, -0.12, 0.29, 0.11)
    robot_images_eye = (0.0, 0.02, 0.34, 0.16)

    normalised_robot_images_mouth = (normalize_coordinate(robot_images_mouth[0]), normalize_coordinate(robot_images_mouth[1]), robot_images_mouth[2], robot_images_mouth[3])
    normalised_robot_images_eye = (normalize_coordinate(robot_images_eye[0]), normalize_coordinate(robot_images_eye[1]), robot_images_eye[2], robot_images_eye[3])

    bounds_robot_image_mouth = get_bounds(normalised_robot_images_mouth[0], normalised_robot_images_mouth[1], normalised_robot_images_mouth[2], normalised_robot_images_mouth[3])
    bounds_robot_image_eye = get_bounds(normalised_robot_images_eye[0], normalised_robot_images_eye[1], normalised_robot_images_eye[2], normalised_robot_images_eye[3])


    gazeData = pd.read_csv(os.getcwd()+"\\"+"GazeCollection.csv")
    gazeData.rename(columns = {"Unnamed: 0": "Image"}, inplace = True)

    robot_name = ["10","11","12","14","16","17","43","27","33","35","36","37","38", "41", "42"]

    robot_8_mouth_count = 0
    robot_8_eyes_count = 0
    robot_8_other_count = 0
    robot_32_mouth_count = 0
    robot_32_eyes_count = 0
    robot_32_other_count = 0
    robot_mouth_count = 0
    robot_eyes_count = 0
    robot_other_count = 0


    robot_pre=["matched-8","matched-32","matched-c"]
    for image in gazeData["Image"]:
        path_ = ""
        isRobot = image[-2::] in robot_name
        if isRobot:
            path_ = "behaviour_analysis\\roi_images\\screenshots_ROBOTS"
            imager = mpimg.imread(path_+"\\"+image+".jpg")
            ysz = imager.shape[0]
            xsz = imager.shape[1]
            scaled_robot_image_mouth = rescale(*bounds_robot_image_mouth, xsz, ysz)
            scaled_robot_image_eyes = rescale(*bounds_robot_image_eye, xsz, ysz)
            gaze = gazeData.loc[gazeData['Image'] == image]
            gaze_x = gaze["Gaze_X"].values
            gaze_x = list(map(float, gaze_x[0][1:-1:].split(", ")))
            gaze_y = gaze["Gaze_Y"].values
            gaze_y = list(map(float, gaze_y[0][1:-1:].split(", ")))
            for i in range(0, len(gaze_x)):
                x, y = normalize_coordinateXY(gaze_x[i], gaze_y[i])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (image[0:len(robot_pre[0]):] == robot_pre[0]):
                    if (is_inside(x, y, *scaled_robot_image_eyes)):
                        robot_8_eyes_count+=1
                    elif (is_inside(x, y, *scaled_robot_image_mouth)):
                        robot_8_mouth_count+=1
                    else:
                        robot_8_other_count+=1
                elif (image[0:len(robot_pre[1]):] == robot_pre[1]):
                    if (is_inside(x, y, *scaled_robot_image_eyes)):
                        robot_32_eyes_count+=1
                    elif (is_inside(x, y, *scaled_robot_image_mouth)):
                        robot_32_mouth_count+=1
                    else:
                        robot_32_other_count+=1
                elif (image[0:len(robot_pre[2]):] == robot_pre[2]):
                    if (is_inside(x, y, *scaled_robot_image_eyes)):
                        robot_eyes_count+=1
                    elif (is_inside(x, y, *scaled_robot_image_mouth)):
                        robot_mouth_count+=1
                    else:
                        robot_other_count+=1


    total = robot_eyes_count + robot_mouth_count + robot_other_count

    robot_eyes_count/=total
    robot_mouth_count/=total
    robot_other_count/=total

    total = robot_8_eyes_count + robot_8_mouth_count + robot_8_other_count

    robot_8_eyes_count/=total
    robot_8_mouth_count/=total
    robot_8_other_count/=total

    total = robot_32_eyes_count + robot_32_mouth_count + robot_32_other_count

    robot_32_eyes_count/=total
    robot_32_mouth_count/=total
    robot_32_other_count/=total

    return ([robot_eyes_count, robot_mouth_count, robot_other_count], [robot_8_eyes_count, robot_8_mouth_count, robot_8_other_count], [robot_32_eyes_count, robot_32_mouth_count, robot_32_other_count])


def plot_robotic():
    data = solve_robotic()
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