unofficial cnc_centroid_skinning - A wrapper for the CNC12 API language.
========================================================

# Introduction

I use products developed by centroidcnc for my CNC activities: https://www.centroidcnc.com/

centroidcnc has developed a controller card named ACORN: 
https://www.centroidcnc.com/centroid_diy/acorn_cnc_controller.html

and ACORN Mill and Lathe *CNC12* software for use with the Centroid Acorn CNC controller 
https://www.centroidcnc.com/centroid_diy/centroid_cnc_software_downloads.html
 
 
# The goal: A Wrapper for Python

In chapter **1.11** of CNC12's documentation: "CNC12 gives the user the ability to create a custom interface that can be 
applied in many different ways". 

This wrapper allows you to use this API in Python, with (almost) the same 
interface as C#. ( https://centroidcncforum.com/viewtopic.php?f=60&t=3397 )




# Release for ACORN 5.30  

The interface has evolved with 64-bit communication, which requires having Python on the same platform to 
communicate with CentroidAPI.dll. .NET has evolved as well, with greater security at the .NET and pythonnet level.

Several interfaces have been added to CentroidAPI, and the code doesn't incorporate all the evolutions, 
but it's very simple to add them.

I couldn't test everything, but the main features **seem** to work. 
The goal is to make it easy for everyone to use Python to send and receive data from the CNC12 program. 

I hope this wrapper allows enthusiasts like me to simply develop their applications with CNC12. 
Python is easy to use and allows rapid prototyping.

# To develop 

this method cannot be called, (enum MpuToPcSysVarBit & PcToMpuSysVarBit   are not published inside the CentroidApi.dll ):

* getPcSystemVariableBit


# Warning

**Be careful** when you send commands or update settings. 
Keep in mind that you can move (or even destroy) your material (which isn't the worst case...). There is no 
protection like in the 'acorn wizard' and you can send many bad values. Verify each time that the wrapper method is correct 
and responds as described in the documentation.  
This interface is not **really tested, don't trust it**. 

## Example use case: video probing   
 
With this wrapper, I have developed a 'video probing' system for internal use.
A camera is placed on the CNC head and detects the center of a hole (thanks to the opencv library https://pypi.org/project/opencv-python/).
This center is used as an origin and the coordinates are sent directly to the CNC12 software. The head moves immediately (thanks to *job.RunCommand()*). 
The second step is to move the head exactly above the center of this hole.
   
Writing this kind of application is quite simple in Python with the help of libraries and the cncSkinning API. 

*The image recognition library I used with the camera for assertions is not included in this library.* 

Please read the chapter: **'CNC Machine Tool Safety'** in the CNC Centroid documentation.  

## Installation

If you have pip, installation is straightforward:

    pip install cnc-centroid-skinning

This will automatically install dependencies as well as their dependencies.

# The documentation

The /CncSkinningDocumentation provided by CNC Centroid has the same packages with the same 
reference. There are some differences, however:

- The methods begin with lowercase. 
- The return code is not provided, but in case of a value different from 'SUCCESS', an ErrorCodeException is raised.
  
[documentation](https://htmlpreview.github.io/?https://github.com/fca1/cnc_centroid_skinning/blob/master/cnc_centroid_skinning/doc/cnc_centroid_skinning/index.html)

## Examples 

Verify the communication between this wrapper and CNC12 (Of course, your CNC12 software must already be launched, otherwise no communication is possible):

The function **detect_cnc(path_of_cnc12)** is written for that purpose. 

    >>> from cnc_centroid_skinning import detect_cnc
    >>> detect_cnc("c:\cnct")  
    'cnc_centroid_skinning communicates... OK' 
    >>>
    
### Ask for configuration
 
    >>> from cnc_centroid_skinning import CentroidApi
    >>> sk = CentroidApi("c:\cnct")                     # create the instance 
    >>> sk.isConstructed()                  
    True
    >>> sk.state.getAcornBoardRevision()
    4
    >>> sk.system.getSystemIdentifier()
    115202849
    >>> from cnc_centroid_skinning import Axes, Direction
    >>> sk.axis.getLabel(Axes.AXIS_1)
    'Z'
    >>> sk.axis.getTravelLimit(Axes.AXIS_1, Direction.PLUS)
    300

### Send a string message to the message window:

    >>> sk.message_window.addMessage('move in 5 seconds...')
    >>> sk.message_window.getMessages()[-1]
    'move in 5 seconds...'

or

    >>> sk.message_window.message = 'move in 5 seconds...'
    >>> sk.message_window.message
    'move in 5 seconds...'

### Run command (more than one way is possible) with a message window provided

**Verify the machine is clear to move the following distance: Z0 -> +Z50**
    
*Be careful with this command. If a command is already running, the next command is ignored
until the job is finished. 
You can see below a method to detect that the job is finished by polling the last message
'306 job finished', but it's not a really good way.*
 
    >>> sk.job.RunCommand("G4 P5.0\nG53 G0 Z0\nZ50", require_cycle_start=False)
    >>> while not sk.message_window.message.startswith('306'): time.sleep(0.3) # job finished
    >>> sk.job.RunCommand("G53 G0 Z0", require_cycle_start=False)

or     

    >>> sk.job.gcode = "G4 P5.0", "G53 G0 Z0", "Z50" 
    >>> while not sk.message_window.message.startswith('306'): time.sleep(0.3) # job finished
    >>>
  
### Use the French language for menus, prompts, etc.
(see 12.3.11 Parameter 9 – Display Language)

    >>> sk.param.getMachineParameterValue(9)   # 0 = english
    0
    >>> sk.param.setMachineParameter(9, 2)
    >>> sk.system.exitSoftware() # Restart is mandatory 

or 

    >>> sk.parameter[9] 
    0
    >>> sk.parameter[9] = 2  
    >>> sk.system.exitSoftware() # Restart is mandatory

### TODO list
- VCP is not tested
- Improve unit test behavior
- This is the first version of docstring; parameter values are not described
- ...