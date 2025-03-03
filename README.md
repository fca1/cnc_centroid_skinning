unofficial cnc_centroid_skinning - A wrapper to the CNC12 API language.
========================================================

# Introduction.

I use for my cnc activities, the products developped by centroidcnc : https://www.centroidcnc.com/

centroidcnc has developped a controller card named ACORN :
https://www.centroidcnc.com/centroid_diy/acorn_cnc_controller.html

and ACORN Mill and Lathe *CNC12* software for use with the Centroid Acorn CNC controller
https://www.centroidcnc.com/centroid_diy/centroid_cnc_software_downloads.html

# The goal: A Wrapper for python

In chapter **1.11** of CNC12's documentation: "CNC12 gives the user the ability to create a custom interface that can be
applied in many different ways".

This wrapper allows to use this API in python language, with (almost) the same
interface as c#.  ( https://centroidcncforum.com/viewtopic.php?f=60&t=3397 )

## Example of use case: a video probing

With this wrapper, I have developed for internal use, a 'video probing'.
A camera is placed on the head of cnc, and detects the center on a hole( thanks to opencv
library https://pypi.org/project/opencv-python/ ).
This center is used as origin and the coordinate are sent directly to the CNC12 software. The head moves immediatly (
thanks to  *job.RunCommand()*).
the second step is to move the head exactly above the center of this hole.

Write this kind of application is quite simply in python language with help of library and the cncSkinning api.

*Image Recognition library I used with camera for assertions is not included in this library.*

# First release

I hope this wrapper allows enthusiasts like me, to simply develop their applications with CNC12.
Python is easy to use and allows rapid prototyping.

The software version of CNC12 is V5.24, pythonnet has changed with net3.0, the python engine must be
with 64 bits platform. The DLL given by CNC CENTROID has changed of name and the platform is also to 64 bits.

This new version seems ok, many functions are not inplemented, but the enhancement is easy.

# Warning

Be careful when you go to send commands, or update settings.
Keep in mind that you can move (see destroy) your material (it's not the worst...). There is no
protection like on the 'acorn wizard' and you can send many bad values. verify each time if the wrapper method is
correct
and respond like described in the documentation.  
This interface is not **really tested, don't trust it**.

# Wrappers methods with a problem:

* Tool : GetToolLibrary()
* State : GetCurrentMachinePosition()
* State: GetCurrentLocalPosition()

Please, read the chapter : **'CNC Machine Tool Safety'**  in the documentation of CNC centroid.

## Installation

If you have pip, installation is straightforward

    pip install cnc-centroid-skinning

This will automatically install dependencies as well as their dependencies.

# The documentation.

The /CncSkinningDocumentation given by Cnc Centroid has the same packages with the same
reference. There are some differences, however:

- The methods begin with a lowercase.
- The return code is not given, but in case of a value different of 'SUCCESS' , an ErrorCodeException is raised.

[documentation](https://htmlpreview.github.io/?https://github.com/fca1/cnc_centroid_skinning/blob/master/cnc_centroid_skinning/doc/cnc_centroid_skinning/index.html)

## Examples

Verify the communication betwwen this wrapper and CNC12 (Of course, your CNC12 software is already launched, else no
communication is possible):

the function **detect_cnc(path_of_cnc12) ** is written for that.

    >>> from cnc_centroid_skinning import detect_cnc
    >>> detect_cnc("c:\cnct")  
    'cnc_centroid_skinning communicates... OK' 
    >>>

### Ask configuration

    >>> from cnc_centroid_skinning import CncSkinning
    >>> sk = CncSkinning("c:\cnct")                     # create the instance 
    >>> sk.isConstructed()                  
    True
    >>> sk.state.getAcornBoardRevision()
    4
    >>> sk.system.getSystemIdentifier()
    115202849
    >>> from cnc_centroid_skinning  import Axes,Direction
    >>> sk.axis.getLabel(Axes.AXIS_1)
    'Z'
    >>> sk.axis.getTravelLimit(Axes.AXIS_1,Direction.PLUS)
    300

### Send a string message to the window message:

    >>> sk.message_window.addMessage('move in 5 seconds...')
    >>> sk.message_window.getMessages()[-1]
    'move in 5 seconds...'

or

    >>> sk.message_window.message = 'move in 5 seconds...'
    >>> sk.message_window.message
    'move in 5 seconds...'

### Run command (more than one way is possible) with a message window given.

**Verify machine is clear to move the following distance: Z0 -> +Z50**

*Be carrefully with this order, if a command is already running, the next command is ignored
until the job is finished.
You can see below a method to detect than the job is finished by poll the last messagen
'306 job finished', but it's not a real good way.*

    >>>  sk.job.RunCommand("G4 P5.0\nG53 G0 Z0\nZ50",require_cycle_start=False)
    >>>  while not sk.message_window.message.startswith('306'): time.sleep(0.3) # job finished
    >>>  sk.job.RunCommand("G53 G0 Z0",require_cycle_start=False)

or

    >>>  sk.job.gcode ="G4 P5.0", "G53 G0 Z0","Z50" 
    >>> while not sk.message_window.message.startswith('306'): time.sleep(0.3) # job finished
    >>>

### Use the FRENCH language for menus, prompt....

(see 12.3.11 Parameter 9 – Display Language)

    >>> sk.param.getMachineParameterValue(9)   # 0 = english
    0
    >>> sk.param.setMachineParameter(9,2)
    >>> sk.system.exitSoftware() # Restart is mandatory 

or

    >>> sk.parameter[9] 
    0
    >>> sk.parameter[9] = 2  
    >>> sk.system.exitSoftware() # Restart is mandatory

### todo list

- Vcp is not tested
- Improve unittest's behavior
- Complete the unitTest
- ...
