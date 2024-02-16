(Smalltalk arguments at: 2) asFileReference readStreamDo:
    [ :stream | model := FamixTypeScriptModel new importFromJSONStream: stream. model install ].

Smalltalk snapshot: true andQuit: true.
