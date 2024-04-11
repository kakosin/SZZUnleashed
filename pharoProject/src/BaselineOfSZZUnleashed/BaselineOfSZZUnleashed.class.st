Class {
	#name : #BaselineOfSZZUnleashed,
	#superclass : #BaselineOf,
	#category : #BaselineOfSZZUnleashed
}

{ #category : #baselines }
BaselineOfSZZUnleashed >> baseline: spec [
	<baseline>
	spec for: #common do: [ 
		self definePackages: spec.
		self defineDependencies: spec.
		self defineGroups: spec
	].
]

{ #category : #baselines }
BaselineOfSZZUnleashed >> defineDependencies: spec [ 
	spec package: 'MetricsAnalyzer-Tests' with: [ spec requires: #('MetricsAnalyzer') ].
]

{ #category : #baselines }
BaselineOfSZZUnleashed >> definePackages: spec [
	spec package: 'MetricsAnalyzer'.
	spec package: 'MetricsAnalyzer-Tests'.
]

{ #category : #baselines }
BaselineOfSZZUnleashed >> defineGroups: spec [
	spec group: 'default' with: #('MetricsAnalyzer' 'MetricsAnalyzer-Tests').
	"Vous pouvez ajouter d'autres groupes si nécessaire"
]
