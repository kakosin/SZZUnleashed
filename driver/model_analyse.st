| analyzer modelFilePath metricsFolderPath |
modelFilePath := Smalltalk arguments at: 1.
metricsFolderPath := Smalltalk arguments at: 2.

analyzer := MetricsAnalyzerClass new.
analyzer analyzeModel: modelFilePath metricsFolder: metricsFolderPath.
Smalltalk snapshot: false andQuit: true.