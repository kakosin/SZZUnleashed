Class {
	#name : #MooseSZZ,
	#superclass : #Object,
	#instVars : [
		'elementsWithLines'
	],
	#category : #'MGL843-SZZ'
}

{ #category : #'as yet unclassified' }
MooseSZZ >> elementsForLine: lineNumber [
	^ elementsWithLines select: [ :e | e sourceAnchor startLine <= lineNumber  ] 

]
