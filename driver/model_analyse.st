| tsModel |
(Smalltalk arguments at: 2) asFileReference readStreamDo:
    [ :stream | tsModel := FamixTypeScriptModel new importFromJSONStream: stream. ].

allModelClasses := tsModel allModelClasses.

allModelClasses do: [ :class |
    | className numberOfLinesOfClass methods csvData csvFileName csvFilePath nameCollection locCollection ccCollection|
    className := class name.
    numberOfLinesOfClass := class numberOfLinesOfCode.
    
    (numberOfLinesOfClass >= 0) ifTrue: [
        Transcript
            show: 'Classe : ', className, ' - Nombre de lignes de code : ', numberOfLinesOfClass printString; cr.
        
        csvData := OrderedCollection new.
        csvData add: #(Name ClassOrMethod LOC CC).
			nameCollection := OrderedCollection new.
			nameCollection add: className.
			locCollection := OrderedCollection new.
			locCollection add: numberOfLinesOfClass.
        csvData add: nameCollection, #C, locCollection, #-.

        methods := class methods.
        
        methods ifNotNil: [
            methods do: [ :method |
                | methodName numberOfLines cyclomaticComplexity |
                methodName := method name.
                numberOfLines := method numberOfLinesOfCode.
                cyclomaticComplexity := method cyclomaticComplexity.
                
                (numberOfLines >= 0 and: [cyclomaticComplexity >= 0]) ifTrue: [
                    Transcript
                        show: '    Méthode : ', methodName, ' - Nombre de lignes de code : ', numberOfLines printString,
                        ' - Complexité cyclomatique : ', cyclomaticComplexity printString; cr.

							nameCollection := 	OrderedCollection new.
							nameCollection add: methodName.
							locCollection := OrderedCollection new.
							locCollection add: numberOfLines.
							ccCollection := OrderedCollection new.
							ccCollection add: cyclomaticComplexity.
        					csvData add: nameCollection, #M, locCollection, ccCollection.
                ].
            ].
        ].
        
        csvFileName := className, '_metrics.csv'.
        csvFilePath := (Smalltalk arguments at: 3), csvFileName.
        
        csvFilePath asFileReference
            writeStreamDo: [ :writeStream |
                (NeoCSVWriter on: writeStream) 
                    fieldWriter: #quoted;
                    nextPutAll: csvData.
            ].
    ].
].

Smalltalk snapshot: true andQuit: true.
