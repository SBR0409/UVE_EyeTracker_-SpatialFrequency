#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 10, 2023, at 23:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'trial_experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\karti\\OneDrive\\Desktop\\IP\\Humanoid images\\trial_experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial" ---
whole_image = visual.Rect(
    win=win, name='whole_image',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
forehead = visual.Rect(
    win=win, name='forehead',
    width=(0.25, 0.066)[0], height=(0.25, 0.066)[1],
    ori=0.0, pos=(0, 0.10), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=0.5, depth=-2.0, interpolate=True)
eyes = visual.Rect(
    win=win, name='eyes',
    width=(0.29, 0.075)[0], height=(0.29, 0.075)[1],
    ori=0.0, pos=(0, 0.018), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=0.5, depth=-3.0, interpolate=True)
nose = visual.Rect(
    win=win, name='nose',
    width=(0.2, 0.055)[0], height=(0.2, 0.055)[1],
    ori=0.0, pos=(0, -0.055), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=0.5, depth=-4.0, interpolate=True)
mouth = visual.Rect(
    win=win, name='mouth',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0, -0.13), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.4588, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=0.5, depth=-5.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('humanoid_images.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image.setImage(filepath)
    # keep track of which components have finished
    trialComponents = [whole_image, image, forehead, eyes, nose, mouth]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *whole_image* updates
        if whole_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whole_image.frameNStart = frameN  # exact frame index
            whole_image.tStart = t  # local t and not account for scr refresh
            whole_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whole_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'whole_image.started')
            whole_image.setAutoDraw(True)
        if whole_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whole_image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                whole_image.tStop = t  # not accounting for scr refresh
                whole_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'whole_image.stopped')
                whole_image.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            
            #    -----------------------------------------------------------------------------------------------------------------------------------------------------------
            fname = os.path.basename(file_name)
            fn = os.path.splitext(fname)[0]
            ss = win.getMovieFrame()
            ss.save(f"screenshots/{fn}.jpg")
        #    -------------------------------------------------------------------------------------------------------------------------------------------------------
        
            
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # *forehead* updates
        if forehead.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forehead.frameNStart = frameN  # exact frame index
            forehead.tStart = t  # local t and not account for scr refresh
            forehead.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forehead, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'forehead.started')
            forehead.setAutoDraw(True)
        if forehead.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > forehead.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                forehead.tStop = t  # not accounting for scr refresh
                forehead.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'forehead.stopped')
                forehead.setAutoDraw(False)
        
        # *eyes* updates
        if eyes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyes.frameNStart = frameN  # exact frame index
            eyes.tStart = t  # local t and not account for scr refresh
            eyes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eyes.started')
            eyes.setAutoDraw(True)
        if eyes.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyes.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                eyes.tStop = t  # not accounting for scr refresh
                eyes.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyes.stopped')
                eyes.setAutoDraw(False)
        
        # *nose* updates
        if nose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nose.frameNStart = frameN  # exact frame index
            nose.tStart = t  # local t and not account for scr refresh
            nose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nose, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nose.started')
            nose.setAutoDraw(True)
        if nose.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nose.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                nose.tStop = t  # not accounting for scr refresh
                nose.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nose.stopped')
                nose.setAutoDraw(False)
        
        # *mouth* updates
        if mouth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouth.frameNStart = frameN  # exact frame index
            mouth.tStart = t  # local t and not account for scr refresh
            mouth.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouth, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mouth.started')
            mouth.setAutoDraw(True)
        if mouth.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouth.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                mouth.tStop = t  # not accounting for scr refresh
                mouth.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouth.stopped')
                mouth.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
