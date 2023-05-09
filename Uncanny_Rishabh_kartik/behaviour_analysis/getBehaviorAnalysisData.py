import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import allDataCollector as adc
import pickle
import generalisedHuman as gh
import generalisedHumanoid as ghid
import generalisedRobotic as gr


def zer(roi_list_partic_wise):
    c = [0, 0, 0]
    for participant in roi_list_partic_wise:
        i = 0
        for roi in participant:
            isZero = True
            for ii in range(len(roi)):
                isZero = isZero and roi[ii] < 0.00001 
            if isZero:
                c[i] += 1
            i += 1
    # sf wise mean
    for participant in roi_list_partic_wise:
        i = 0
        for SF in participant:
            for roii in range(len(SF)):
                if len(roi_list_partic_wise)-c[i] != 0:
                    SF[roii] /= (len(roi_list_partic_wise)-c[i])
            i+=1
    #sum all participants using numpy
    roi_list_partic_wise = np.sum(roi_list_partic_wise, axis=0)
    return roi_list_partic_wise


# read behavior analysis data from csv BehavioralAnalysisData
def getBehaviorAnalysisData():
    # read data from csv
    df = pd.read_csv('BehavioralAnalysisData.csv', sep=',', header=0, index_col=0)
    return df

# get the data from csv
df = getBehaviorAnalysisData()

finalData = {}

allGazeX, allGazeY = adc.gaze_collection()

# iterate over each row
for index, row in df.iterrows():
    # get the value for each column at the current row
    file_name = row['File_Name']
    type_ = row['Type']
    Spatial_Freq = row['Spatial_Freq']
    Likability = row['Likability']
    
    Mechano_Humanness = row['Mechano_Humanness']

    # convert string to list
    Likability = list(map(float, Likability[1:-1].split(',')))
    Mechano_Humanness = list(map(float, Mechano_Humanness[1:-1].split(',')))

    for i in range(len(Likability)):
        id = "P" + str(1+i)
        lk = 0
        mh = 0
        if Likability[i] >= 0:
            lk = 1
        if Mechano_Humanness[i] >= 50:
            mh = 1

        gaze_x = allGazeX[id][file_name.split(".")[0]]
        gaze_y = allGazeY[id][file_name.split(".")[0]]
        
        if id not in finalData:
            finalData[id] = {}
            
            finalData[id][file_name] = [type_, Spatial_Freq, Likability[i], Mechano_Humanness[i], lk, mh, gaze_x, gaze_y]
        else:
            finalData[id][file_name] = [type_, Spatial_Freq, Likability[i], Mechano_Humanness[i], lk, mh, gaze_x, gaze_y]

# human->ml::hl ll
# human->hml::hl ll
# robot->ml::hl ll
# robot->hml::hl ll

HHLHM_x = {}
HHLLM_x = {}
HLLHM_x = {}
HLLLM_x = {}
MHLHM_x = {}
MHLLM_x = {}
MLLHM_x = {}
MLLLM_x = {}

HHLHM_y = {}
HHLLM_y = {}
HLLHM_y = {}
HLLLM_y = {}
MHLHM_y = {}
MHLLM_y = {}
MLLHM_y = {}
MLLLM_y = {}


for id in finalData:
    HHLHM_x[id] = {}
    HHLLM_x[id] = {}
    HLLHM_x[id] = {}
    HLLLM_x[id] = {}
    MHLHM_x[id] = {}
    MHLLM_x[id] = {}
    MLLHM_x[id] = {}
    MLLLM_x[id] = {}

    HHLHM_y[id] = {}
    HHLLM_y[id] = {}
    HLLHM_y[id] = {}
    HLLLM_y[id] = {}
    MHLHM_y[id] = {}
    MHLLM_y[id] = {}
    MLLHM_y[id] = {}
    MLLLM_y[id] = {}

    
    
    HLLHM_x[id]["HSF"] = []
    HLLHM_x[id]["BSF"] = []
    HLLHM_x[id]["LSF"] = []

    HLLLM_x[id]["HSF"] = []
    HLLLM_x[id]["BSF"] = []
    HLLLM_x[id]["LSF"] = []

    HHLLM_x[id]["HSF"] = []
    HHLLM_x[id]["BSF"] = []
    HHLLM_x[id]["LSF"] = []

    HHLHM_x[id]["HSF"] = []
    HHLHM_x[id]["BSF"] = []
    HHLHM_x[id]["LSF"] = []

    MLLHM_x[id]["HSF"] = []
    MLLHM_x[id]["BSF"] = []
    MLLHM_x[id]["LSF"] = []

    MLLLM_x[id]["HSF"] = []
    MLLLM_x[id]["BSF"] = []
    MLLLM_x[id]["LSF"] = []

    MHLHM_x[id]["HSF"] = []
    MHLHM_x[id]["BSF"] = []
    MHLHM_x[id]["LSF"] = []
    
    MHLLM_x[id]["HSF"] = []
    MHLLM_x[id]["BSF"] = []
    MHLLM_x[id]["LSF"] = []

    HLLHM_y[id]["HSF"] = []
    HLLHM_y[id]["BSF"] = []
    HLLHM_y[id]["LSF"] = []

    HLLLM_y[id]["HSF"] = []
    HLLLM_y[id]["BSF"] = []
    HLLLM_y[id]["LSF"] = []

    HHLLM_y[id]["HSF"] = []
    HHLLM_y[id]["BSF"] = []
    HHLLM_y[id]["LSF"] = []

    HHLHM_y[id]["HSF"] = []
    HHLHM_y[id]["BSF"] = []
    HHLHM_y[id]["LSF"] = []

    MLLHM_y[id]["HSF"] = []
    MLLHM_y[id]["BSF"] = []
    MLLHM_y[id]["LSF"] = []

    MLLLM_y[id]["HSF"] = []
    MLLLM_y[id]["BSF"] = []
    MLLLM_y[id]["LSF"] = []

    MHLHM_y[id]["HSF"] = []
    MHLHM_y[id]["BSF"] = []
    MHLHM_y[id]["LSF"] = []

    MHLLM_y[id]["HSF"] = []
    MHLLM_y[id]["BSF"] = []
    MHLLM_y[id]["LSF"] = []



    for img in finalData[id]:
        type_ = finalData[id][img][0]
        Spatial_Freq = finalData[id][img][1]
        lk = finalData[id][img][4]
        mh = finalData[id][img][5]
        gaze_x = finalData[id][img][6]
        gaze_y = finalData[id][img][7]
        

        if type_ == "Human" and lk == 1 and mh == 1:
            HHLHM_x[id][Spatial_Freq].extend(gaze_x)
            HHLHM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ == "Human" and lk == 1 and mh == 0:
            HHLLM_x[id][Spatial_Freq].extend(gaze_x)
            HHLLM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ == "Human" and lk == 0 and mh == 1:
            HLLHM_x[id][Spatial_Freq].extend(gaze_x)
            HLLHM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ == "Human" and lk == 0 and mh == 0:
            HLLLM_x[id][Spatial_Freq].extend(gaze_x)
            HLLLM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ != "Human" and lk == 1 and mh == 1:
            MHLHM_x[id][Spatial_Freq].extend(gaze_x)
            MHLHM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ != "Human" and lk == 1 and mh == 0:
            MHLLM_x[id][Spatial_Freq].extend(gaze_x)
            MHLLM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ != "Human" and lk == 0 and mh == 1:
            MLLHM_x[id][Spatial_Freq].extend(gaze_x)
            MLLHM_y[id][Spatial_Freq].extend(gaze_y)
        elif type_ != "Human" and lk == 0 and mh == 0:
            MLLLM_x[id][Spatial_Freq].extend(gaze_x)
            MLLLM_y[id][Spatial_Freq].extend(gaze_y)


AllData = [HHLHM_x, HHLLM_x, HLLHM_x, HLLLM_x, 
           MHLHM_x, MHLLM_x, MLLHM_x, MLLLM_x, 
           HHLHM_y, HHLLM_y, HLLHM_y, HLLLM_y, 
           MHLHM_y, MHLLM_y, MLLHM_y, MLLLM_y]



# pickle the data
with open('AllData.pickle', 'wb') as handle:
    pickle.dump(AllData, handle, protocol=pickle.HIGHEST_PROTOCOL)


# convert to csv
df = pd.DataFrame.from_dict(finalData, orient='index')
df.to_csv('finalData.csv')

roi_list_partic_wise_HHLHM = []
for i in HHLHM_x:
    roi = gh.solve_human((HHLHM_x[i], HHLHM_y[i]))
    roi_list_partic_wise_HHLHM.append(roi)
    
roi_list_partic_wise_HHLLM = []
for i in HHLLM_x:
    roi = gh.solve_human((HHLLM_x[i], HHLLM_y[i]))
    roi_list_partic_wise_HHLLM.append(roi)

roi_list_partic_wise_HLLHM = []
for i in HLLHM_x:
    roi = gh.solve_human((HLLHM_x[i], HLLHM_y[i]))
    roi_list_partic_wise_HLLHM.append(roi)
    
roi_list_partic_wise_HLLLM = []
for i in HLLLM_x:
    roi = gh.solve_human((HLLLM_x[i], HLLLM_y[i]))
    roi_list_partic_wise_HLLLM.append(roi)

"----------------------------------------------------------------------------------------------"

roi_list_partic_wise_MHLHM = []
for i in MHLHM_x:
    roi = ghid.solve_humanoid((MHLHM_x[i], MHLHM_y[i]))
    roi_list_partic_wise_MHLHM.append(roi)
    
roi_list_partic_wise_MHLLM = []
for i in MHLLM_x:
    roi = gr.solve_robotic((MHLLM_x[i], MHLLM_y[i]))
    roi_list_partic_wise_MHLLM.append(roi)


roi_list_partic_wise_MLLHM = []
for i in MLLHM_x:
    roi = ghid.solve_humanoid((MLLHM_x[i], MLLHM_y[i]))
    roi_list_partic_wise_MLLHM.append(roi)
    
roi_list_partic_wise_MLLLM = []
for i in MLLLM_x:
    roi = gr.solve_robotic((MLLLM_x[i], MLLLM_y[i]))
    roi_list_partic_wise_MLLLM.append(roi)


roi_list_partic_wise_HHLHM = zer(roi_list_partic_wise_HHLHM)
roi_list_partic_wise_HHLLM = zer(roi_list_partic_wise_HHLLM)
roi_list_partic_wise_HLLHM = zer(roi_list_partic_wise_HLLHM)
roi_list_partic_wise_HLLLM = zer(roi_list_partic_wise_HLLLM)
roi_list_partic_wise_MHLHM = zer(roi_list_partic_wise_MHLHM)
roi_list_partic_wise_MHLLM = zer(roi_list_partic_wise_MHLLM)
roi_list_partic_wise_MLLHM = zer(roi_list_partic_wise_MLLHM)
roi_list_partic_wise_MLLLM = zer(roi_list_partic_wise_MLLLM)


# plot in subplots bar plots the x shouold be the roi regions like eye mouth and y should be the average ROI
roi_labels = ["Eye", "Forehead", "Mouth", "Nose", "Other"]
roi = np.arange(len(roi_labels))

fig, axs = plt.subplots(2, 2)
# padding
fig.tight_layout(pad=3.0)
# fig size
fig.set_size_inches(18.5, 10.5)
fig.suptitle('Average ROI of all participants: Human Images')
axs[0, 0].bar(roi - 0.2, roi_list_partic_wise_HHLHM[0], 0.2, label = 'BSF')
axs[0, 0].bar(roi, roi_list_partic_wise_HHLHM[1], 0.2, label = 'LSF')
axs[0, 0].bar(roi + 0.2, roi_list_partic_wise_HHLHM[2], 0.2, label = 'HSF')
axs[0, 0].set_title('HighLik HighMechHum')
axs[0, 0].set_xticks(roi, roi_labels)
axs[0, 1].bar(roi - 0.2, roi_list_partic_wise_HHLLM[0], 0.2, label = 'BSF')
axs[0, 1].bar(roi, roi_list_partic_wise_HHLLM[1], 0.2, label = 'LSF')
axs[0, 1].bar(roi + 0.2, roi_list_partic_wise_HHLLM[2], 0.2, label = 'HSF')
axs[0, 1].set_title('HighLik LowMechHum')
axs[0, 1].set_xticks(roi, roi_labels)
axs[1, 0].bar(roi - 0.2, roi_list_partic_wise_HLLHM[0], 0.2, label = 'BSF')
axs[1, 0].bar(roi, roi_list_partic_wise_HLLHM[1], 0.2, label = 'LSF')
axs[1, 0].bar(roi + 0.2, roi_list_partic_wise_HLLHM[2], 0.2, label = 'HSF')
axs[1, 0].set_title('LowLik HighMechHum')
axs[1, 0].set_xticks(roi, roi_labels)
axs[1, 1].bar(roi - 0.2, roi_list_partic_wise_HLLLM[0], 0.2, label = 'BSF')
axs[1, 1].bar(roi, roi_list_partic_wise_HLLLM[1], 0.2, label = 'LSF')
axs[1, 1].bar(roi + 0.2, roi_list_partic_wise_HLLLM[2], 0.2, label = 'HSF')
axs[1, 1].set_title('LowLik LowMechHum')
axs[1, 1].set_xticks(roi, roi_labels)

for ax in axs.flat:
    ax.set(xlabel='ROI', ylabel='Average Gaze')
# legends
axs[0, 0].legend()
axs[0, 1].legend()
axs[1, 0].legend()
axs[1, 1].legend()
# save the plot
plt.savefig('behaviour_analysis\\HumanROI.png')


# plot in subplots bar plots the x shouold be the roi regions like eye mouth and y should be the average ROI
roi_rob_labels = ["Eye", "Mouth","Other"]
roi_rob = np.arange(len(roi_rob_labels))
fig, axs = plt.subplots(2, 2)
# padding
fig.tight_layout(pad=3.0)
# fig size
fig.set_size_inches(18.5, 10.5)
fig.suptitle('Average ROI of all participants: Machine Images')
axs[0, 0].bar(roi - 0.2, roi_list_partic_wise_MHLHM[0], 0.2, label = 'BSF')
axs[0, 0].bar(roi, roi_list_partic_wise_MHLHM[1], 0.2, label = 'LSF')
axs[0, 0].bar(roi + 0.2, roi_list_partic_wise_MHLHM[2], 0.2, label = 'HSF')
axs[0, 0].set_title('HighLik HighMechHum')
#xticks
axs[0, 0].set_xticks(roi, roi_labels)
axs[0, 1].bar(roi_rob - 0.2, roi_list_partic_wise_MHLLM[0], 0.2, label = 'BSF')
axs[0, 1].bar(roi_rob, roi_list_partic_wise_MHLLM[1], 0.2, label = 'LSF')
axs[0, 1].bar(roi_rob + 0.2, roi_list_partic_wise_MHLLM[2], 0.2, label = 'HSF')
axs[0, 1].set_title('HighLik LowMechHum')
axs[0, 1].set_xticks(roi_rob, roi_rob_labels)
axs[1, 0].bar(roi - 0.2, roi_list_partic_wise_MLLHM[0], 0.2, label = 'BSF')
axs[1, 0].bar(roi, roi_list_partic_wise_MLLHM[1], 0.2, label = 'LSF')
axs[1, 0].bar(roi + 0.2, roi_list_partic_wise_MLLHM[2], 0.2, label = 'HSF')
axs[1, 0].set_title('LowLik HighMechHum')
axs[1, 0].set_xticks(roi, roi_labels)
axs[1, 1].bar(roi_rob - 0.2, roi_list_partic_wise_MLLLM[0], 0.2, label = 'BSF')
axs[1, 1].bar(roi_rob, roi_list_partic_wise_MLLLM[1], 0.2, label = 'LSF')
axs[1, 1].bar(roi_rob + 0.2, roi_list_partic_wise_MLLLM[2], 0.2, label = 'HSF')
axs[1, 1].set_title('LowLik LowMechHum')
axs[1, 1].set_xticks(roi_rob, roi_rob_labels)

for ax in axs.flat:
    ax.set(xlabel='ROI', ylabel='Average Gaze')
# legends
axs[0, 0].legend()
axs[0, 1].legend()
axs[1, 0].legend()
axs[1, 1].legend()

# save the plot
plt.savefig('behaviour_analysis\\MachineROI.png')

print("Successfuly created HumanROI.png and MachineROI.png")



