#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 16, 2023, at 22:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
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
from psychopy.hardware import emotiv



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'trial uncanny'  # from the Builder filename that created this script
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
    originPath='E:\\Visual_Cognition\\Uncanny_Rishabh_kartik\\experiment ucv  sharing\\ROBOT_UCV_M_H\\Robotic_final\\Robotic_uncanny_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
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

# Setup eyetracking
ioConfig['eyetracker.hw.pupil_labs.pupil_core.EyeTracker'] = {
    'name': 'tracker',
    'runtime_settings': {
        'pupillometry_only': False,
        'surface_name': 'psychopy_iohub_surface',
        'gaze_confidence_threshold': 0.6,
        'pupil_remote': {
            'ip_address': '127.0.0.1',
            'port': 50020.0,
            'timeout_ms': 1000.0,
        },
        'pupil_capture_recording': {
            'enabled': True,
            'location': '',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='trial uncanny', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Proceed" ---
instruction = visual.TextStim(win=win, name='instruction',
    text='PRESS SPACE BAR TO PROCEED TO EXPERIMENT ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "eye_tracker_rt" ---
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)

# --- Initialize components for Routine "Fixation_cross" ---
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Robotic_Stimuli" ---
Robotic__Stimuli = visual.ImageStim(
    win=win,
    name='Robotic__Stimuli', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
roi = visual.ROI(win, name='roi', device=eyetracker,
    debug=False,
    shape='triangle',
    pos=(0, 0), size=(0.5, 0.5), anchor='center', ori=0.0)

# --- Initialize components for Routine "Mechano_Human_likeness" ---
M_H_likeness_slider = visual.Slider(win=win, name='M_H_likeness_slider',
    startValue=0.00, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=["Mechanical","Human"], ticks=(0, 100), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
instruct_Mechano_humannnes = visual.TextStim(win=win, name='instruct_Mechano_humannnes',
    text='Rate the Mechano-Humannes ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ratingText = visual.TextStim(win=win, name='ratingText',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Button_Image.png', mask=None, anchor='center',
    ori=0.0, pos=(0.49, -0.43), size=(0.33, 0.106),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "ISI" ---
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# --- Initialize components for Routine "eye_tracker_rt_stop" ---
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='FIVE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Proceed" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ProceedComponents = [instruction, key_resp]
for thisComponent in ProceedComponents:
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

# --- Run Routine "Proceed" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction.started')
        instruction.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProceedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Proceed" ---
for thisComponent in ProceedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Proceed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "eye_tracker_rt" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
eye_tracker_rtComponents = [etRecord]
for thisComponent in eye_tracker_rtComponents:
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

# --- Run Routine "eye_tracker_rt" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *etRecord* updates
    if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etRecord.frameNStart = frameN  # exact frame index
        etRecord.tStart = t  # local t and not account for scr refresh
        etRecord.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('etRecord.started', t)
        etRecord.status = STARTED
    if etRecord.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord.tStop = t  # not accounting for scr refresh
            etRecord.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord.stopped', t)
            etRecord.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eye_tracker_rtComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "eye_tracker_rt" ---
for thisComponent in eye_tracker_rtComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord.status != FINISHED:
    etRecord.status = FINISHED
# the Routine "eye_tracker_rt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
robotic_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Robotic_stimuli File.csv'),
    seed=None, name='robotic_trials')
thisExp.addLoop(robotic_trials)  # add the loop to the experiment
thisRobotic_trial = robotic_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRobotic_trial.rgb)
if thisRobotic_trial != None:
    for paramName in thisRobotic_trial:
        exec('{} = thisRobotic_trial[paramName]'.format(paramName))

for thisRobotic_trial in robotic_trials:
    currentLoop = robotic_trials
    # abbreviate parameter names if possible (e.g. rgb = thisRobotic_trial.rgb)
    if thisRobotic_trial != None:
        for paramName in thisRobotic_trial:
            exec('{} = thisRobotic_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Fixation_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Fixation_crossComponents = [Fixation]
    for thisComponent in Fixation_crossComponents:
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
    
    # --- Run Routine "Fixation_cross" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_cross" ---
    for thisComponent in Fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Robotic_Stimuli" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Robotic__Stimuli.setImage(filepath)
    # clear any previous roi data
    roi.reset()
    # keep track of which components have finished
    Robotic_StimuliComponents = [Robotic__Stimuli, roi]
    for thisComponent in Robotic_StimuliComponents:
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
    
    # --- Run Routine "Robotic_Stimuli" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Robotic__Stimuli* updates
        if Robotic__Stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Robotic__Stimuli.frameNStart = frameN  # exact frame index
            Robotic__Stimuli.tStart = t  # local t and not account for scr refresh
            Robotic__Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Robotic__Stimuli, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Robotic__Stimuli.started')
            Robotic__Stimuli.setAutoDraw(True)
        if Robotic__Stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Robotic__Stimuli.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Robotic__Stimuli.tStop = t  # not accounting for scr refresh
                Robotic__Stimuli.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Robotic__Stimuli.stopped')
                Robotic__Stimuli.setAutoDraw(False)
        if roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            roi.frameNStart = frameN  # exact frame index
            roi.tStart = t  # local t and not account for scr refresh
            roi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(roi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'roi.started')
            roi.status = STARTED
        if roi.status == STARTED:
            # check whether roi has been looked in
            if roi.isLookedIn:
                if not roi.wasLookedIn:
                    roi.timesOn.append(roi.clock.getTime()) # store time of first look
                    roi.timesOff.append(roi.clock.getTime()) # store time looked until
                else:
                    roi.timesOff[-1] = roi.clock.getTime() # update time looked until
                roi.wasLookedIn = True  # if roi is still looked at next frame, it is not a new look
            else:
                if roi.wasLookedIn:
                    roi.timesOff[-1] = roi.clock.getTime() # update time looked until
                roi.wasLookedIn = False  # if roi is looked at next frame, it is a new look
        else:
            roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
            roi.wasLookedIn = False  # if roi is looked at next frame, it is a new look
        if roi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > roi.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                roi.tStop = t  # not accounting for scr refresh
                roi.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'roi.stopped')
                roi.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Robotic_StimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Robotic_Stimuli" ---
    for thisComponent in Robotic_StimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    robotic_trials.addData('roi.numLooks', roi.numLooks)
    if roi.numLooks:
       robotic_trials.addData('roi.timesOn', roi.timesOn)
       robotic_trials.addData('roi.timesOff', roi.timesOff)
    else:
       robotic_trials.addData('roi.timesOn', "")
       robotic_trials.addData('roi.timesOff', "")
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Mechano_Human_likeness" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    thisPos = 0
    M_H_likeness_slider.reset()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Mechano_Human_likenessComponents = [M_H_likeness_slider, instruct_Mechano_humannnes, ratingText, image, mouse]
    for thisComponent in Mechano_Human_likenessComponents:
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
    
    # --- Run Routine "Mechano_Human_likeness" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        
        thisPos = M_H_likeness_slider.getMarkerPos()
        formatted_thisPos=np.round(thisPos,1)
        
        #formatted_thisPos=str.format('{0:.3f}', thisPos)
        
        
        # *M_H_likeness_slider* updates
        if M_H_likeness_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            M_H_likeness_slider.frameNStart = frameN  # exact frame index
            M_H_likeness_slider.tStart = t  # local t and not account for scr refresh
            M_H_likeness_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(M_H_likeness_slider, 'tStartRefresh')  # time at next scr refresh
            M_H_likeness_slider.setAutoDraw(True)
        
        # *instruct_Mechano_humannnes* updates
        if instruct_Mechano_humannnes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_Mechano_humannnes.frameNStart = frameN  # exact frame index
            instruct_Mechano_humannnes.tStart = t  # local t and not account for scr refresh
            instruct_Mechano_humannnes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_Mechano_humannnes, 'tStartRefresh')  # time at next scr refresh
            instruct_Mechano_humannnes.setAutoDraw(True)
        
        # *ratingText* updates
        if ratingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ratingText.frameNStart = frameN  # exact frame index
            ratingText.tStart = t  # local t and not account for scr refresh
            ratingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingText, 'tStartRefresh')  # time at next scr refresh
            ratingText.setAutoDraw(True)
        if ratingText.status == STARTED:  # only update if drawing
            ratingText.setText('Current rating : ' + str(formatted_thisPos)
, log=False)
        
        # *image* updates
        if image.status == NOT_STARTED and M_H_likeness_slider.rating:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and M_H_likeness_slider.rating:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(image)
                        clickableList = image
                    except:
                        clickableList = [image]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Mechano_Human_likenessComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Mechano_Human_likeness" ---
    for thisComponent in Mechano_Human_likenessComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    robotic_trials.addData('M_H_likeness_slider.response', M_H_likeness_slider.getRating())
    robotic_trials.addData('M_H_likeness_slider.rt', M_H_likeness_slider.getRT())
    # store data for robotic_trials (TrialHandler)
    # the Routine "Mechano_Human_likeness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISI_2]
    for thisComponent in ISIComponents:
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
    
    # --- Run Routine "ISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ISI_2.started', t)
            ISI_2.start(0.5)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
            ISI_2.tStop = ISI_2.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'robotic_trials'


# --- Prepare to start Routine "eye_tracker_rt_stop" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
eye_tracker_rt_stopComponents = [etRecord_2]
for thisComponent in eye_tracker_rt_stopComponents:
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

# --- Run Routine "eye_tracker_rt_stop" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *etRecord_2* updates
    if etRecord_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etRecord_2.frameNStart = frameN  # exact frame index
        etRecord_2.tStart = t  # local t and not account for scr refresh
        etRecord_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etRecord_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('etRecord_2.started', t)
        etRecord_2.status = STARTED
    if etRecord_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord_2.tStop = t  # not accounting for scr refresh
            etRecord_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord_2.stopped', t)
            etRecord_2.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eye_tracker_rt_stopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "eye_tracker_rt_stop" ---
for thisComponent in eye_tracker_rt_stopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord_2.status != FINISHED:
    etRecord_2.status = FINISHED

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
