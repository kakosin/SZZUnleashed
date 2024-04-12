| analyzer modelFilePath metricsFolderPath |
modelFilePath := Smalltalk arguments at: 2.
metricsFolderPath := Smalltalk arguments at: 3.

analyzer := MetricsAnalyzerClass new.
analyzer analyzeModel: modelFilePath metricsFolder: metricsFolderPath.
Smalltalk snapshot: false andQuit: true.