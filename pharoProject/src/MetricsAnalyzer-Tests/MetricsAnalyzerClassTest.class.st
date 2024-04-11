Class {
	#name : #MetricsAnalyzerClassTest,
	#superclass : #TestCase,
	#category : #'MetricsAnalyzer-Tests'
}

{ #category : #tests }
MetricsAnalyzerClassTest >> testAnalyzeModelClassesCreatesCSV [
    | analyzer index directory csvFiles |

    analyzer := MetricsAnalyzerClass new.
    index := 1. 

    directory := FileSystem disk workingDirectory / 'metrics'.

    analyzer analyzeModelClasses: index.

    csvFiles := directory entries select: [:each | each extension = 'csv'].
    self assert: csvFiles notEmpty.
]

{ #category : #tests }
MetricsAnalyzerClassTest >> testCSVHeadersAreCorrect [
    | analyzer index directory csvFiles expectedHeaders |

    analyzer := MetricsAnalyzerClass new.
    index := 1.

    directory := FileSystem disk workingDirectory / 'metrics'.

    analyzer analyzeModelClasses: index.

    expectedHeaders := #('"Name"' '"ClassOrMethod"' '"LOC"' '"CC"').

    csvFiles := directory entries select: [:each | each extension = 'csv'].

	 csvFiles do: [:csvFile |
		| fileStream headers |
		fileStream := csvFile readStream.
      [headers := fileStream nextLine findTokens: ', '.
      self assert: headers asArray equals: expectedHeaders]
        ensure: [fileStream close].
    ].


]

{ #category : #tests }
MetricsAnalyzerClassTest >> testMooseModelAtReturnsCorrectModel [
    | analyzer index actualModel expectedModelName |

    analyzer := MetricsAnalyzerClass new.
    index := 1.
    expectedModelName := 'antvis__G2'.

    actualModel := analyzer mooseModelAt: index.

    self assert: (actualModel name) equals: expectedModelName.

]
