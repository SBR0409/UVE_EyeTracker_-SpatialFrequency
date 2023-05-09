'''Generalized code for Gaze collection - participant wise'''


import pandas as pd
import os


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

        iterPartic = 0
        for file in sorted(os.listdir(curDir+"\\behaviour_analysis" +dataDir[iii])):
            if not (file.endswith("monocular_data.csv")):
                continue

            id = "P"+str(iterPartic+1)
            iterPartic += 1
            monData = pd.read_csv(curDir + "\\behaviour_analysis" +  dataDir[iii]+ "\\" + file)
            triggers = pd.read_csv(curDir + "\\behaviour_analysis" +  dataDir[iii]+ "\\" + file[:-19:] + ".csv")
            image_vs_time_start = triggers[["file_name", s]].values.tolist()[1:-1:]
            for image, time in image_vs_time_start:
                temp = monData[monData['time'].between(time, time+1, inclusive="left")]
                trig_gaze_x = temp["gaze_x"].values.tolist()
                trig_gaze_y = temp["gaze_y"].values.tolist()
                im = image.split(".")[0]

                if id not in i_wise_gaze_x:
                    i_wise_gaze_x[id] = {}
                    i_wise_gaze_y[id] = {}
                    i_wise_gaze_x[id][im] = trig_gaze_x
                    i_wise_gaze_y[id][im] = trig_gaze_y
                else:
                    if im not in i_wise_gaze_x[id]:
                        i_wise_gaze_x[id][im] = []
                        i_wise_gaze_y[id][im] = []
                    i_wise_gaze_x[id][im].extend(trig_gaze_x)
                    i_wise_gaze_y[id][im].extend(trig_gaze_y)
    return [i_wise_gaze_x, i_wise_gaze_y]
    


if __name__ == "__main__":
    i_wise_gaze_x, i_wise_gaze_y = gaze_collection()
    gazeData = {imgg:[i_wise_gaze_x[imgg], i_wise_gaze_y[imgg]] for imgg in i_wise_gaze_x.keys()}
    finDf = pd.DataFrame(gazeData).T
    finDf.columns = ["Gaze_X", "Gaze_Y"]
    print(finDf)
    finDf.to_csv(os.getcwd()+"\\"+"NewGazeCollection.csv")