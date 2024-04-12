| analyzer modelFilePath metricsFolderPath |
modelFilePath := Smalltalk arguments at: 2.
metricsFolderPath := Smalltalk arguments at: 3.

analyzer := MetricsAnalyzerClass new.
analyzer metricsFolderPath:metricsFolderPath.
analyzer analyzeModelClasses: 1.
Smalltalk snapshot: false andQuit: true.