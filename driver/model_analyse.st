| analyzer modelPath metricsFolderPath |
modelPath := Smalltalk arguments at: 2.
metricsFolderPath := Smalltalk arguments at: 3.

analyzer := MetricsAnalyzerClass new.
analyzer metricsFolderPath:metricsFolderPath.
analyzer modelPath:modelPath.
analyzer analyzeModelClasses.

Smalltalk snapshot: false andQuit: true.