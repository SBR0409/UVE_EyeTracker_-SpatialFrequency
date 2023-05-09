import os
import pandas as pd

def buildII():
    dataDir = ['\\LH', '\\LR', '\\MH', '\\MR']
    j=0

    listOfFilenames = []
    listOfFileTypes = []
    listOfSpatialFreq = []
    listOfLikability = []
    listOfMechano_Humanness = []
    curDir = os.getcwd()

    img_vs_lik = {}
    img_vs_hum = {} 
    img_vs_spat = {}
    img_vs_type = {}
    
    for iii in range(len(dataDir)):
        j+=1
        for file in sorted(os.listdir(curDir+"\\behaviour_analysis"  + dataDir[iii])):
            if (len(file) > 10):
                continue

            csv_ = pd.read_csv(curDir +"\\behaviour_analysis"  +dataDir[iii]+ "\\" + file)

            if (j<3):
                listOfLikability = list(csv_['Likebility_slider_3.response'][1:-1:])
                listOfFilenames = list(csv_['file_name'][1:-1:])
                listOfSpatialFreq = list(csv_['Spatial_Frequency'][1:-1:])
                listOfFileTypes = list(csv_['Type'][1:-1:])

                for i in range(len(listOfLikability)):
                    if listOfFilenames[i] not in list(img_vs_lik.keys()):
                        img_vs_lik[listOfFilenames[i]] = [listOfLikability[i]]
                    else:
                        img_vs_lik[listOfFilenames[i]].append(listOfLikability[i])
                    img_vs_type[listOfFilenames[i]]= listOfFileTypes[i]
                    img_vs_spat[listOfFilenames[i]]= listOfSpatialFreq[i]
            
            else:
                listOfMechano_Humanness = list(csv_['M_H_likeness_slider.response'][1:-1:])
                listOfFilenames = list(csv_['file_name'][1:-1:])
                listOfSpatialFreq = list(csv_['Spatial_Frequency'][1:-1:])
                listOfFileTypes = list(csv_['Type'][1:-1:])

                for i in range(len(listOfMechano_Humanness)):
                    if listOfFilenames[i] not in list(img_vs_hum.keys()):
                        img_vs_hum[listOfFilenames[i]] = [listOfMechano_Humanness[i]]
                    else:
                        img_vs_hum[listOfFilenames[i]].append(listOfMechano_Humanness[i])
                    img_vs_type[listOfFilenames[i]]= listOfFileTypes[i]
                    img_vs_spat[listOfFilenames[i]]= listOfSpatialFreq[i]

    listOfFilenames = list(img_vs_type.keys())
    listOfLikability = []
    listOfSpatialFreq = []
    listOfFileTypes = []
    listOfMechano_Humanness = []

    for i in  range(len(listOfFilenames)):
        listOfLikability.append(img_vs_lik[listOfFilenames[i]])
        listOfSpatialFreq.append(img_vs_spat[listOfFilenames[i]])
        listOfMechano_Humanness.append(img_vs_hum[listOfFilenames[i]])
        listOfFileTypes.append(img_vs_type[listOfFilenames[i]])

    dictt = {'File_Name':listOfFilenames,
        'Type':listOfFileTypes,
        'Spatial_Freq':listOfSpatialFreq,
        'Likability':listOfLikability, 
        'Mechano_Humanness':listOfMechano_Humanness}
 
    finalData =  pd.DataFrame(dictt)
    finalData.to_csv(curDir+"\\"+"BehavioralAnalysisData.csv")

    print("Successfully created a CSV file named 'BehavioralAnalysisData.csv'")
    print("")
    
if __name__ == "__main__":
    buildII()