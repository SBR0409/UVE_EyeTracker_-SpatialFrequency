# plots gaze positions over the images...

from gazeCollector import gaze_collection as gc
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def gazePlots(path_, prefix = "", psz = 15, opacity = 0.08, folderr = "gazePlots"):

    img_gaze = gc()
    for image in sorted(os.listdir(path_)):
        fig, ax = plt.subplots()
        im = image.split(".")[0]
        imager = mpimg.imread(path_+"\\"+image)

        ysz = imager.shape[0]
        xsz = imager.shape[1]

        x = [xsz*(i+1)/2 for i in img_gaze[0][im]]
        y = [ysz*(1-i)/2 for i in img_gaze[1][im]]
        img = plt.imread(path_+"\\"+image)
        plt.scatter(x, y, color="red", s=psz, alpha=opacity)
        ax.imshow(img)
        plt.savefig("behaviour_analysis\\"+ folderr +"\\"+prefix+image)
        plt.close()

if __name__ == "__main__":
    gazePlots("behaviour_analysis\\roi_images\\screenshots_HUMAN", "roi_")
    gazePlots("behaviour_analysis\\roi_images\\screenshots_HUMANOID", "roi_")
    gazePlots("behaviour_analysis\\roi_images\\screenshots_ROBOTS", "roi_")
    print("Successfully constructed the gaze plots in gazePlots folder.")