Class {
	#name : #MetricsAnalyzerClass,
	#superclass : #Object,
	#instVars : [
		'modelPath',
		'metricsFolderPath'
	],
	#category : #MetricsAnalyzer
}

{ #category : #abstract }
MetricsAnalyzerClass >> analyzeClass: aClass [
    | className numberOfLinesOfClass methods csvData |
    className := aClass name.
    numberOfLinesOfClass := aClass numberOfLinesOfCode.

    (numberOfLinesOfClass >= 0) ifTrue: [
        csvData := OrderedCollection new.
        csvData add: #(Name ClassOrMethod LOC CC).

        methods := aClass methods.
        methods ifNotNil: [
            methods do: [ :method |
                | methodName numberOfLines cyclomaticComplexity nameCollection locCollection ccCollection |
                methodName := method name.
                numberOfLines := method numberOfLinesOfCode.
                cyclomaticComplexity := method cyclomaticComplexity.

                (numberOfLines >= 0 and: [cyclomaticComplexity >= 0]) ifTrue: [
                    nameCollection := OrderedCollection new.
                    nameCollection add: methodName.
                    locCollection := OrderedCollection new.
                    locCollection add: numberOfLines.
                    ccCollection := OrderedCollection new.
                    ccCollection add: cyclomaticComplexity.
                    csvData add: nameCollection, #M, locCollection, ccCollection.
                ].
            ].
        ].
        self writeCsvData: csvData forClass: className.
    ].

]

{ #category : #'accessing - arguments' }
MetricsAnalyzerClass >> analyzeModelClasses [
    | tsModel allModelClasses |
	 modelPath asFileReference readStreamDo:
    [ :stream | tsModel := FamixTypeScriptModel new importFromJSONStream: stream. ].
    allModelClasses := tsModel allModelClasses.

    allModelClasses do: [ :class |
        self analyzeClass: class.
    ].

]

{ #category : #accessing }
MetricsAnalyzerClass >> metricsFolderPath [

	^ metricsFolderPath
]

{ #category : #accessing }
MetricsAnalyzerClass >> metricsFolderPath: anObject [

	metricsFolderPath := anObject
]

{ #category : #accessing }
MetricsAnalyzerClass >> modelPath [

	^ modelPath
]

{ #category : #accessing }
MetricsAnalyzerClass >> modelPath: anObject [

	modelPath := anObject
]

{ #category : #accessing }
MetricsAnalyzerClass >> mooseModelAt: anIndex [
    ^MooseModel root at: anIndex

]

{ #category : #writing }
MetricsAnalyzerClass >> writeCsvData: csvData forClass: className [
    | csvFileName csvFilePath |
    csvFileName := className, '_metrics.csv'.
    csvFilePath := metricsFolderPath, csvFileName.

    csvFilePath asFileReference writeStreamDo: [ :writeStream |
        (NeoCSVWriter on: writeStream)
            fieldWriter: #quoted;
            nextPutAll: csvData.
    ].

]
