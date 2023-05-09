# Instructions for running the code

**Steps to be followed after HDF5 conversion to CSV:**

Pre 1: Add the csv files to respective experiments (by making a participant folder in data subfolder)

Pre 2: Copy the two csv files created by extracting the HDF5 into LH, LR, MH, MR accordingly in Behavioral Analysis folder (rename the files according to participant number, i.e. P1.csv and P1-monocular_data.csv)


1. Run ratingCollector.py to get a csv of Likeability and MH ratings (sorted by participant #)
      - Upon execution, this message is printed:  
      ```
      Successfully created a CSV file named 'BehavioralAnalysisData.csv'
      ```
      
2. Run gazeCollector.py to get a csv of total Gaze Point Positions for each image.
      - Upon execution, this message is printed:  
      ```
      Successfully created GazeCollection.csv      
      ```
3. Run gazePlotter.py to get gaze plots for each image saved into the gazePlots folder.
      - Upon execution, this message is printed:  
      ```
      Successfully constructed the gaze plots in gazePlots folder.     
      ```
4. Run human.py for ROI Gaze summary bar plot for human stimuli

5. Run humanoid.py for ROI Gaze summary bar plot for humanoid stimuli

6. Run robotic.py for ROI Gaze summary bar plot for robotic stimuli

7. Run getBehaviorAnalysisData.py to get ROI Gaze summary for Human and Mechanical Images (with subplots for each Likeability and MH rating bracket).
      - Upon execution, this message is printed:  
      ```
      Successfuly created HumanROI.png and MachineROI.png      
      ```
*Note: Some files are imported and used in other codes(which are executed). Change to these files will affect many others as well.*
