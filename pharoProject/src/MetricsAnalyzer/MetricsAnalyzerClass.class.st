Class {
	#name : #MetricsAnalyzerClass,
	#superclass : #Object,
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
MetricsAnalyzerClass >> analyzeModelClasses: anIndex [
    | tsModel allModelClasses |
    tsModel := self mooseModelAt: anIndex.
    allModelClasses := tsModel allModelClasses.

    allModelClasses do: [ :class |
        self analyzeClass: class.
    ].

]

{ #category : #accessing }
MetricsAnalyzerClass >> mooseModelAt: anIndex [
    ^MooseModel root at: anIndex

]

{ #category : #writing }
MetricsAnalyzerClass >> writeCsvData: csvData forClass: className [
    | csvFileName csvFilePath |
    csvFileName := className, '_metrics.csv'.
    csvFilePath := 'metrics/', csvFileName.

    csvFilePath asFileReference writeStreamDo: [ :writeStream |
        (NeoCSVWriter on: writeStream)
            fieldWriter: #quoted;
            nextPutAll: csvData.
    ].

]
