Metacello new
    baseline: 'Moose';
    repository: 'github://moosetechnology/Moose:v10.x.x/src';
    onWarningLog;
    load.

Smalltalk snapshot: true andQuit: true.