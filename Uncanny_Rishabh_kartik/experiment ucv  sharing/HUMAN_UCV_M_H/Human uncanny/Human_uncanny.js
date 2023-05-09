/********************** 
 * Human_Uncanny Test *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Human_uncanny';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(recordingRoutineBegin());
flowScheduler.add(recordingRoutineEachFrame());
flowScheduler.add(recordingRoutineEnd());
const human_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(human_trialsLoopBegin(human_trialsLoopScheduler));
flowScheduler.add(human_trialsLoopScheduler);
flowScheduler.add(human_trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Human.csv', 'path': 'Human.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var recordingClock;
var Fixation_crossClock;
var Fixation;
var Human_StimuliClock;
var Human_image;
var Mechano_Human_likenessClock;
var M_H_likeness_slider;
var instruct_Mechano_humannnes;
var ratingText_2;
var image_2;
var mouse_2;
var LikeabilityClock;
var Likebility_slider_3;
var ratingText;
var image;
var mouse;
var ISIClock;
var ISI_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "recording"
  recordingClock = new util.Clock();
  // Initialize components for Routine "Fixation_cross"
  Fixation_crossClock = new util.Clock();
  Fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('red'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Human_Stimuli"
  Human_StimuliClock = new util.Clock();
  Human_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Human_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "Mechano_Human_likeness"
  Mechano_Human_likenessClock = new util.Clock();
  M_H_likeness_slider = new visual.Slider({
    win: psychoJS.window, name: 'M_H_likeness_slider',
    startValue: 0.0,
    size: [1.0, 0.1], pos: [0, (- 0.1)], ori: 0.0, units: 'height',
    labels: ["Mechanical", "Human"], fontSize: 0.05, ticks: [0, 100],
    granularity: 0.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  instruct_Mechano_humannnes = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_Mechano_humannnes',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  ratingText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ratingText_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'Button_Image.png', mask : undefined,
    ori : 0.0, pos : [0.49, (- 0.43)], size : [0.33, 0.106],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "Likeability"
  LikeabilityClock = new util.Clock();
  Likebility_slider_3 = new visual.Slider({
    win: psychoJS.window, name: 'Likebility_slider_3',
    startValue: 0.0,
    size: [1.0, 0.1], pos: [0, (- 0.1)], ori: 0.0, units: 'height',
    labels: ["Mechanical", "Human"], fontSize: 0.05, ticks: [(- 100), 100],
    granularity: 0.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  ratingText = new visual.TextStim({
    win: psychoJS.window,
    name: 'ratingText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'Button_Image.png', mask : undefined,
    ori : 0.0, pos : [0.49, (- 0.43)], size : [0.33, 0.106],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISI_2 = new core.MinimalStim({
    name: "ISI_2", 
    win: psychoJS.window,
    autoDraw: false, 
    autoLog: true, 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var recordingComponents;
function recordingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'recording' ---
    t = 0;
    recordingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    recordingComponents = [];
    
    for (const thisComponent of recordingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function recordingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'recording' ---
    // get current time
    t = recordingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recordingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recordingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'recording' ---
    for (const thisComponent of recordingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var human_trials;
function human_trialsLoopBegin(human_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    human_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Human.csv',
      seed: undefined, name: 'human_trials'
    });
    psychoJS.experiment.addLoop(human_trials); // add the loop to the experiment
    currentLoop = human_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisHuman_trial of human_trials) {
      snapshot = human_trials.getSnapshot();
      human_trialsLoopScheduler.add(importConditions(snapshot));
      human_trialsLoopScheduler.add(Fixation_crossRoutineBegin(snapshot));
      human_trialsLoopScheduler.add(Fixation_crossRoutineEachFrame());
      human_trialsLoopScheduler.add(Fixation_crossRoutineEnd(snapshot));
      human_trialsLoopScheduler.add(Human_StimuliRoutineBegin(snapshot));
      human_trialsLoopScheduler.add(Human_StimuliRoutineEachFrame());
      human_trialsLoopScheduler.add(Human_StimuliRoutineEnd(snapshot));
      human_trialsLoopScheduler.add(Mechano_Human_likenessRoutineBegin(snapshot));
      human_trialsLoopScheduler.add(Mechano_Human_likenessRoutineEachFrame());
      human_trialsLoopScheduler.add(Mechano_Human_likenessRoutineEnd(snapshot));
      human_trialsLoopScheduler.add(LikeabilityRoutineBegin(snapshot));
      human_trialsLoopScheduler.add(LikeabilityRoutineEachFrame());
      human_trialsLoopScheduler.add(LikeabilityRoutineEnd(snapshot));
      human_trialsLoopScheduler.add(ISIRoutineBegin(snapshot));
      human_trialsLoopScheduler.add(ISIRoutineEachFrame());
      human_trialsLoopScheduler.add(ISIRoutineEnd(snapshot));
      human_trialsLoopScheduler.add(human_trialsLoopEndIteration(human_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function human_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(human_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function human_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Fixation_crossComponents;
function Fixation_crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fixation_cross' ---
    t = 0;
    Fixation_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Fixation_crossComponents = [];
    Fixation_crossComponents.push(Fixation);
    
    for (const thisComponent of Fixation_crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Fixation_crossRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fixation_cross' ---
    // get current time
    t = Fixation_crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation* updates
    if (t >= 0.0 && Fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation.tStart = t;  // (not accounting for frame time here)
      Fixation.frameNStart = frameN;  // exact frame index
      
      Fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Fixation_crossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Fixation_crossRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fixation_cross' ---
    for (const thisComponent of Fixation_crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Human_StimuliComponents;
function Human_StimuliRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Human_Stimuli' ---
    t = 0;
    Human_StimuliClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    Human_image.setImage(filepath);
    // keep track of which components have finished
    Human_StimuliComponents = [];
    Human_StimuliComponents.push(Human_image);
    
    for (const thisComponent of Human_StimuliComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Human_StimuliRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Human_Stimuli' ---
    // get current time
    t = Human_StimuliClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Human_image* updates
    if (t >= 0.0 && Human_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Human_image.tStart = t;  // (not accounting for frame time here)
      Human_image.frameNStart = frameN;  // exact frame index
      
      Human_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Human_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Human_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Human_StimuliComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Human_StimuliRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Human_Stimuli' ---
    for (const thisComponent of Human_StimuliComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var thisPos;
var gotValidClick;
var Mechano_Human_likenessComponents;
function Mechano_Human_likenessRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Mechano_Human_likeness' ---
    t = 0;
    Mechano_Human_likenessClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    thisPos = 0;
    
    M_H_likeness_slider.reset()
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Mechano_Human_likenessComponents = [];
    Mechano_Human_likenessComponents.push(M_H_likeness_slider);
    Mechano_Human_likenessComponents.push(instruct_Mechano_humannnes);
    Mechano_Human_likenessComponents.push(ratingText_2);
    Mechano_Human_likenessComponents.push(image_2);
    Mechano_Human_likenessComponents.push(mouse_2);
    
    for (const thisComponent of Mechano_Human_likenessComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function Mechano_Human_likenessRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Mechano_Human_likeness' ---
    // get current time
    t = Mechano_Human_likenessClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2
    if (typeof slider._markerPos !== 'undefined') {
        thisPos = slider._markerPos;
        }
    
    
    // *M_H_likeness_slider* updates
    if (t >= 0.0 && M_H_likeness_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      M_H_likeness_slider.tStart = t;  // (not accounting for frame time here)
      M_H_likeness_slider.frameNStart = frameN;  // exact frame index
      
      M_H_likeness_slider.setAutoDraw(true);
    }

    
    // *instruct_Mechano_humannnes* updates
    if (t >= 0.0 && instruct_Mechano_humannnes.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_Mechano_humannnes.tStart = t;  // (not accounting for frame time here)
      instruct_Mechano_humannnes.frameNStart = frameN;  // exact frame index
      
      instruct_Mechano_humannnes.setAutoDraw(true);
    }

    
    if (instruct_Mechano_humannnes.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instruct_Mechano_humannnes.setText(("Current rating : " + formatted_thisPos_2.toString()), false);
    }
    
    // *ratingText_2* updates
    if (t >= 0.0 && ratingText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingText_2.tStart = t;  // (not accounting for frame time here)
      ratingText_2.frameNStart = frameN;  // exact frame index
      
      ratingText_2.setAutoDraw(true);
    }

    
    if (ratingText_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      ratingText_2.setText(("Current rating : " + formatted_thisPos_2.toString()), false);
    }
    
    // *image_2* updates
    if ((M_H_likeness_slider.rating) && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    // *mouse_2* updates
    if ((M_H_likeness_slider.rating) && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Mechano_Human_likenessComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Mechano_Human_likenessRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Mechano_Human_likeness' ---
    for (const thisComponent of Mechano_Human_likenessComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('M_H_likeness_slider.response', M_H_likeness_slider.getRating());
    psychoJS.experiment.addData('M_H_likeness_slider.rt', M_H_likeness_slider.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "Mechano_Human_likeness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var LikeabilityComponents;
function LikeabilityRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Likeability' ---
    t = 0;
    LikeabilityClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    thisPos = 0;
    
    Likebility_slider_3.reset()
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    LikeabilityComponents = [];
    LikeabilityComponents.push(Likebility_slider_3);
    LikeabilityComponents.push(ratingText);
    LikeabilityComponents.push(image);
    LikeabilityComponents.push(mouse);
    
    for (const thisComponent of LikeabilityComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _mouseXYs;
function LikeabilityRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Likeability' ---
    // get current time
    t = LikeabilityClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    if (typeof slider._markerPos !== 'undefined') {
        thisPos = slider._markerPos;
        }
    
    
    // *Likebility_slider_3* updates
    if (t >= 0.0 && Likebility_slider_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Likebility_slider_3.tStart = t;  // (not accounting for frame time here)
      Likebility_slider_3.frameNStart = frameN;  // exact frame index
      
      Likebility_slider_3.setAutoDraw(true);
    }

    
    // *ratingText* updates
    if (t >= 0.0 && ratingText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingText.tStart = t;  // (not accounting for frame time here)
      ratingText.frameNStart = frameN;  // exact frame index
      
      ratingText.setAutoDraw(true);
    }

    
    if (ratingText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      ratingText.setText(("Current rating : " + formatted_thisPos_4.toString()), false);
    }
    
    // *image* updates
    if ((Likebility_slider_3.rating) && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // *mouse* updates
    if ((Likebility_slider_3.rating) && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LikeabilityComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LikeabilityRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Likeability' ---
    for (const thisComponent of LikeabilityComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Likebility_slider_3.response', Likebility_slider_3.getRating());
    psychoJS.experiment.addData('Likebility_slider_3.rt', Likebility_slider_3.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // the Routine "Likeability" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ISI' ---
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(ISI_2);
    
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ISI' ---
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (t >= 0.0 && ISI_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_2.tStart = t;  // (not accounting for frame time here)
      ISI_2.frameNStart = frameN;  // exact frame index
      
      ISI.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ISI' ---
    for (const thisComponent of ISIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
