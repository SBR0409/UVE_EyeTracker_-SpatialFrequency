"""Collects gaze_x and gaze_y of all participants for each image"""

# iterate through each participant file and collect gaze coordinates ->> pass this into image dictionary:: using image name as uid, triggers are in generated file


# extract human image start time from name_type_uncanny/../../.csv and thjen from this timestamp till another 1 sec, pick all the  instances from monocular data csv...

# column from name_type_uncanny/../../.csv ["image.started"], corresponding column in monocular data csv file -> ["time"]



# Schedule -> iterate through each, compare andf store in a list in turn stored in a dictionary...     store this dictionary in pickled/json file format...


# Usage -> Extract data from the stored data file and plot gaze_x, gaze_y for each image...

# Usage +1 -> Use bounds(i.e., ROI ranges) and get the freq of gaze points in each ROI for each image separately... then pickle/json the same...
#         * then, extract this data file and plot a bar plot for the average case for human & robotic categories...

import os
import pandas as pd


def gaze_collection():
    dataDir = ['\\LH', '\\LR', '\\MH', '\\MR']

    curDir = os.getcwd()

    i_wise_gaze_x = {}
    i_wise_gaze_y = {}
    j = 0
    for iii in range(len(dataDir)):
        j+=1
        s = "Human_image.started"
        if (j%2 == 0):
            s = "Robotic__Stimuli.started"
        
        for file in sorted(os.listdir(curDir+"\\behaviour_analysis" +dataDir[iii])):
            if not (file.endswith("monocular_data.csv")):
                continue
            monData = pd.read_csv(curDir + "\\behaviour_analysis" +  dataDir[iii]+ "\\" + file)
            triggers = pd.read_csv(curDir + "\\behaviour_analysis" +  dataDir[iii]+ "\\" + file[:-19:] + ".csv")
            image_vs_time_start = triggers[["file_name", s]].values.tolist()[1:-1:]
            for image, time in image_vs_time_start:
                temp = monData[monData['time'].between(time, time+1, inclusive="left")]
                trig_gaze_x = temp["gaze_x"].values.tolist()
                trig_gaze_y = temp["gaze_y"].values.tolist()
                im = image.split(".")[0]

                if im not in i_wise_gaze_x.keys():
                    i_wise_gaze_x[im] = trig_gaze_x
                    i_wise_gaze_y[im] = trig_gaze_y
                else:
                    i_wise_gaze_x[im].extend(trig_gaze_x)
                    i_wise_gaze_y[im].extend(trig_gaze_y)

    return [i_wise_gaze_x, i_wise_gaze_y]
    


if __name__ == "__main__":
    i_wise_gaze_x, i_wise_gaze_y = gaze_collection()
    gazeData = {imgg:[i_wise_gaze_x[imgg], i_wise_gaze_y[imgg]] for imgg in i_wise_gaze_x.keys()}
    finDf = pd.DataFrame(gazeData).T
    finDf.columns = ["Gaze_X", "Gaze_Y"]
    finDf.to_csv(os.getcwd()+"\\"+"GazeCollection.csv")
    print("Successfully created GazeCollection.csv")
