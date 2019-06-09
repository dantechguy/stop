import json

def convertCode(assetsFolder):
  jsonUrl = '{0}/project.json'.format(assetsFolder)

  projectJson = ''

  with open(jsonUrl) as json_file:  
    projectJson = json.load(json_file)

  spritesJson = projectJson['targets']
  for spriteJson in spritesJson:
    spriteCode = convertSprite(spriteJson)


def convertSprite(spriteJson):
  costumesJson = spriteJson['costumes']
  costumeCode = convertSpriteCostumeCode(costumesJson)


  spriteName = spriteJson['name']
  initiateCode = 'sprite_{0} = stop.Sprite(project, costumes=costumes)'.format(spriteName)

  scriptCode = convertSpriteScriptCode(spriteJson)

  finalCode = '{0}\n{1}\n{2}'.format(costumeCode, initiateCode, scriptCode)


def convertSpriteCostumeCode(costumesJson):
  costumeArray = []
  for costumeJson in costumesJson:
    currentCostumeUrl = costumeJson['assetId']
    currentCostumeName = costumeJson['name']
    rotateCentreX = costumeJson['rotationCenterX']
    rotateCentreY = costumeJson['rotationCenterY']

    currentCostumeJson = {
      'file': currentCostumeUrl,
      'name': currentCostumeName,
      'rotateCentreX': rotateCentreX,
      'rotateCentreY': rotateCentreY
    }

    costumeArray.append(currentCostumeJson)

  finalCode = 'costumes = '.format(costumeArray)
  return finalCode


def convertSpriteScriptCode(spriteJson):
  finalCode = ''

  numberOfTopBlockTypes = {
    'green_flag': 0,
  }

  blocksJson = spriteJson['blocks']
  for blockJsonKey in blocksJson:
    blockJson = blocksJson[blockJsonKey]

    isTopLevel = blockJson['topLevel']
    isEventBlock = #- - - - - - - - - ADD EVENT BLOCK CHECK
    if isTopLevel:
      createScript(blockJson, spriteJson, numberOfTopBlockTypes)


def createScript(topBlockJson, spriteJson, numberOfTopBlockTypes):

  spriteName = spriteJson['name']
  topBlockType = convertOpCodeToFunction(topBlockJson['opcode'])
  topBlockTypeNumber = numberOfTopBlockTypes[topBlockType]

  functionName = '{0}_{1}{2}'.format(spriteName, topBlockType, topBlockTypeNumber)

  finalCode = generateSolidBlockCode(topBlockJson, spriteJson)



  finalCode = '''def {0}():
{1}

project.{2}({0})'''.format(functionName, finalCode, topBlockType)

  return finalCode


def convertOpCodeToFunction(opcode):
  conv = {
    'event_whenflagclicked': 'green_flag',

  }
  return conv[opcode]

# def sprite1_greenflag1():
#   sprite_sprite1.move_steps(10)

# project.green_flag(sprite1_greenflag1)


def generateSolidBlockCode(parentBlockJson, spriteJson, finalCode=''):
  currentBlockId = parentBlockJson['next']
  currentBlockJson = spriteJson[currentBlockId]
  currentBlockType = currentBlockJson['opcode']
  spriteVariableName = 'sprite_{0}'.format(spriteJson['name'])

  if currentBlockType == 'motion_movesteps':
    inputType = type(currentBlockJson['fields']['TO'][0]).__name__

    if inputType == 'list': # if number
      steps = currentBlockJson['inputs']['STEPS'][1][1]
    elif inputType == 'str': # if round block
      roundBlockId = 
      steps = generateRoundBlockCode(currentBlockJson, spriteJson)
    finalCode += '{0}.move_steps({1})'.format(spriteVariableName, steps)

  elif currentBlockType == 'motion_turnright':
    degrees = currentBlockJson['inputs']['DEGREES'][1][1]
    finalCode += '{0}.turn_right_degrees({1})'.format(spriteVariableName, degrees)

  elif currentBlockType == 'motion_turnleft':
    degrees = currentBlockJson['inputs']['DEGREES'][1][1]
    finalCode += '{0}.turn_left_degrees({1})'.format(spriteVariableName, degrees)





def generateRoundBlockCode(currentJsonBlock, spriteJson):
  finalCode = ''
  currentBlockId = parentBlockJson['next']
  currentBlockJson = spriteJson[currentBlockId]
  currentBlockType = currentBlockJson['opcode']
  spriteVariableName = 'sprite_{0}'.format(spriteJson['name'])


  if currentBlockType == 'motion_goto_menu':
    gotoInput = currentBlockJson['fields']['TO'][0]
    conversion = {
      '_random_': 'random_position',
    }
    return conversion[gotoInput]

  elif currentBlockType == 'motion_xposition':
    return '{0}.x'.format(spriteVariableName)

  elif currentBlockType == 'motion_yposition':
    return '{0}.y'.format(spriteVariableName)

  elif currentBlockType == 'motion_direction':
    return '{0}.direction'.format(spriteVariableName)

  elif currentBlockType == 'looks_costumenumbername':
    costumeInput = currentBlockJson['fields']['NUMBER_NAME'][0]
    conv = {
      'number': 'costume_number',
      'name': 'costume_name'
    }
    method = conv[costumeInput]
    return '{0}.{1}'.format(spriteVariableName, method)

  elif currentBlockType == 'looks_backdropnumbername':
    costumeInput = currentBlockJson['fields']['NUMBER_NAME'][0]
    conv = {
      'number': 'backdrop_number',
      'name': 'backdrop_name'
    }
    method = conv[costumeInput]
    return 'project.{1}'.format(method)

  elif currentBlockType == 'looks_size':
    return '{0}.size'.format(spriteVariableName)

  elif currentBlockType == 'sensing_distanceto':
    distanceInputId = currentBlockJson['inputs']['DISTANCETOMENU'][1]
    distanceInputJson = spriteJson[distanceInputId]
    generatedInput = generateRoundBlockCode(currentBlockJson, spriteJson)
    return '{0}.distance_to({1})'.format(spriteVariableName, generatedInput)

  elif currentBlockType == 'sensing_distancetomenu':
    distanceInput = currentBlockJson['fields']['DISTANCETOMENU'][0]
    conv = {
      '_mouse_': 'mouse_pointer'
    }
    return conv[costumeInput]

  elif currentBlockType == 'sensing_answer':
    return '{0}.answer'.format(spriteVariableName)

  elif currentBlockType == 'sensing_keypressed':
    keyInput = currentBlockJson['fields']['DISTANCETOMENU'][0]
    generatedInput = 
    return 'project.key_pressed({0})'.format()



# convertCode('C:/Users/danie/Documents/code/python/scratch2python/convertion stuff/.temp/assets')













# solid
"blocks":{  
            ")zm^g|Fe4T=_%?1[w+:n":{  
               "opcode":"motion_goto",
               "next":".tOoo/~(]V+v5.!2^pNB",
               "parent":"6#_MtOvW*M_gz#I}2#7,",
               "inputs":{  
                  "TO":[  
                     1,
                     "%,z6B=v9B0INMRi;`F6-"
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "%,z6B=v9B0INMRi;`F6-":{  
               "opcode":"motion_goto_menu",
               "next":null,
               "parent":")zm^g|Fe4T=_%?1[w+:n",
               "inputs":{  

               },
               "fields":{  
                  "TO":[  
                     "_mouse_",
                     null
                  ]
               },
               "shadow":true,
               "topLevel":false
            },
            ".tOoo/~(]V+v5.!2^pNB":{  
               "opcode":"motion_gotoxy",
               "next":"ZNvAi3-Mnt|}%,LrcarR",
               "parent":")zm^g|Fe4T=_%?1[w+:n",
               "inputs":{  
                  "X":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ],
                  "Y":[  
                     1,
                     [  
                        4,
                        "9"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "@Rbh5gJMsoZ94C/4;)Td":{  
               "opcode":"motion_glideto",
               "next":"lA[3Kl_I}qLZlrox!e)^",
               "parent":"ZNvAi3-Mnt|}%,LrcarR",
               "inputs":{  
                  "SECS":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ],
                  "TO":[  
                     1,
                     "$iS8lH_LZl[JSu6m#j?G"
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "$iS8lH_LZl[JSu6m#j?G":{  
               "opcode":"motion_glideto_menu",
               "next":null,
               "parent":"@Rbh5gJMsoZ94C/4;)Td",
               "inputs":{  

               },
               "fields":{  
                  "TO":[  
                     "_mouse_",
                     null
                  ]
               },
               "shadow":true,
               "topLevel":false
            },
            "lA[3Kl_I}qLZlrox!e)^":{  
               "opcode":"motion_glidesecstoxy",
               "next":"MyG;4ZxU)#l@L|lIiwgX",
               "parent":"@Rbh5gJMsoZ94C/4;)Td",
               "inputs":{  
                  "SECS":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ],
                  "X":[  
                     1,
                     [  
                        4,
                        "9"
                     ]
                  ],
                  "Y":[  
                     1,
                     [  
                        4,
                        "11"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "MyG;4ZxU)#l@L|lIiwgX":{  
               "opcode":"motion_pointindirection",
               "next":"_TfA=$sZOgIQZ{,oHQuy",
               "parent":"lA[3Kl_I}qLZlrox!e)^",
               "inputs":{  
                  "DIRECTION":[  
                     1,
                     [  
                        8,
                        "7"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "6#_MtOvW*M_gz#I}2#7,":{  
               "opcode":"motion_goto",
               "next":")zm^g|Fe4T=_%?1[w+:n",
               "parent":"YbVqg8l!}HV}9=^iXi.Q",
               "inputs":{  
                  "TO":[  
                     1,
                     "7UmS9bJO{UpV.]~()8j+"
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "7UmS9bJO{UpV.]~()8j+":{  
               "opcode":"motion_goto_menu",
               "next":null,
               "parent":"6#_MtOvW*M_gz#I}2#7,",
               "inputs":{  

               },
               "fields":{  
                  "TO":[  
                     "_random_",
                     null
                  ]
               },
               "shadow":true,
               "topLevel":false
            },
            "ZNvAi3-Mnt|}%,LrcarR":{  
               "opcode":"motion_glideto",
               "next":"@Rbh5gJMsoZ94C/4;)Td",
               "parent":".tOoo/~(]V+v5.!2^pNB",
               "inputs":{  
                  "SECS":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ],
                  "TO":[  
                     1,
                     "s_1P$y/*[UR,P%lES=yL"
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "s_1P$y/*[UR,P%lES=yL":{  
               "opcode":"motion_glideto_menu",
               "next":null,
               "parent":"ZNvAi3-Mnt|}%,LrcarR",
               "inputs":{  

               },
               "fields":{  
                  "TO":[  
                     "_random_",
                     null
                  ]
               },
               "shadow":true,
               "topLevel":false
            },
            "_TfA=$sZOgIQZ{,oHQuy":{  
               "opcode":"motion_pointtowards",
               "next":"l*R|96utsd0S_=[nNa(%",
               "parent":"MyG;4ZxU)#l@L|lIiwgX",
               "inputs":{  
                  "TOWARDS":[  
                     1,
                     ")(~+qPJxwcoc6ilFliq2"
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            ")(~+qPJxwcoc6ilFliq2":{  
               "opcode":"motion_pointtowards_menu",
               "next":null,
               "parent":"_TfA=$sZOgIQZ{,oHQuy",
               "inputs":{  

               },
               "fields":{  
                  "TOWARDS":[  
                     "_mouse_",
                     null
                  ]
               },
               "shadow":true,
               "topLevel":false
            },
            "l*R|96utsd0S_=[nNa(%":{  
               "opcode":"motion_changexby",
               "next":"EJkT:~X(H^;NY^k|!yiz",
               "parent":"_TfA=$sZOgIQZ{,oHQuy",
               "inputs":{  
                  "DX":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "EJkT:~X(H^;NY^k|!yiz":{  
               "opcode":"motion_setx",
               "next":"`BPUvW6#d8[j?vo#XBRZ",
               "parent":"l*R|96utsd0S_=[nNa(%",
               "inputs":{  
                  "X":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "`BPUvW6#d8[j?vo#XBRZ":{  
               "opcode":"motion_changeyby",
               "next":"TH/tRmvZCI5I7Sw@^{oL",
               "parent":"EJkT:~X(H^;NY^k|!yiz",
               "inputs":{  
                  "DY":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "TH/tRmvZCI5I7Sw@^{oL":{  
               "opcode":"motion_sety",
               "next":"T08fOdx5.L@t%DaS[}.x",
               "parent":"`BPUvW6#d8[j?vo#XBRZ",
               "inputs":{  
                  "Y":[  
                     1,
                     [  
                        4,
                        "7"
                     ]
                  ]
               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "T08fOdx5.L@t%DaS[}.x":{  
               "opcode":"motion_ifonedgebounce",
               "next":"Dj;Z^emNQqcL:o;A|}e8",
               "parent":"TH/tRmvZCI5I7Sw@^{oL",
               "inputs":{  

               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":false
            },
            "Dj;Z^emNQqcL:o;A|}e8":{  
               "opcode":"motion_setrotationstyle",
               "next":null,
               "parent":"T08fOdx5.L@t%DaS[}.x",
               "inputs":{  

               },
               "fields":{  
                  "STYLE":[  
                     "left-right",
                     null
                  ]
               },
               "shadow":false,
               "topLevel":false
            },
            "UQS6K=!g2F)%c-YL82z$":{  
               "opcode":"motion_xposition",
               "next":null,
               "parent":null,
               "inputs":{  

               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":true,
               "x":77,
               "y":899
            },
            "vBpr9YCi3lge+o1Sw}P(":{  
               "opcode":"motion_yposition",
               "next":null,
               "parent":null,
               "inputs":{  

               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":true,
               "x":100,
               "y":1000
            },
            "Z[fz6wk@e]V,g[;)r3FI":{  
               "opcode":"motion_direction",
               "next":null,
               "parent":null,
               "inputs":{  

               },
               "fields":{  

               },
               "shadow":false,
               "topLevel":true,
               "x":146,
               "y":1088
            }
         }















{  
"isStage":false,
"name":"Sprite1",
"variables":{  

},
"lists":{  

},
"broadcasts":{  

},
"blocks":{  
  "K+n8bbDr8I8okU%]h?a^":{  
     "opcode":"event_whenflagclicked",
     "next":"$1=}jPuBboC7$Y-{-2kS",
     "parent":null,
     "inputs":{  

     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":true,
     "x":162,
     "y":38
  },
  "$1=}jPuBboC7$Y-{-2kS":{  
     "opcode":"control_wait",
     "next":"1yUg_;:KcW8G:y/x#G)?",
     "parent":"K+n8bbDr8I8okU%]h?a^",
     "inputs":{  
        "DURATION":[  
           1,
           [  
              5,
              "1"
           ]
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  },
  "1yUg_;:KcW8G:y/x#G)?":{  
     "opcode":"control_repeat",
     "next":"T?u%pz!{1t8fKwY(-moZ",
     "parent":"$1=}jPuBboC7$Y-{-2kS",
     "inputs":{  
        "TIMES":[  
           1,
           [  
              6,
              "10"
           ]
        ],
        "SUBSTACK":[  
           2,
           ".NjN;dJtewb:@v13c0|6"
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  },
  ".NjN;dJtewb:@v13c0|6":{  
     "opcode":"motion_turnright",
     "next":null,
     "parent":"1yUg_;:KcW8G:y/x#G)?",
     "inputs":{  
        "DEGREES":[  
           1,
           [  
              4,
              "15"
           ]
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  },
  "T?u%pz!{1t8fKwY(-moZ":{  
     "opcode":"control_forever",
     "next":null,
     "parent":"1yUg_;:KcW8G:y/x#G)?",
     "inputs":{  
        "SUBSTACK":[  
           2,
           "cOz8xv=Yq$|G84:w$WPO"
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  },
  "cOz8xv=Yq$|G84:w$WPO":{  
     "opcode":"motion_movesteps",
     "next":"Qpgkj?]%6eZ-``6U|sel",
     "parent":"T?u%pz!{1t8fKwY(-moZ",
     "inputs":{  
        "STEPS":[  
           1,
           [  
              4,
              "10"
           ]
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  },
  "Qpgkj?]%6eZ-``6U|sel":{  
     "opcode":"motion_turnleft",
     "next":null,
     "parent":"cOz8xv=Yq$|G84:w$WPO",
     "inputs":{  
        "DEGREES":[  
           1,
           [  
              4,
              "15"
           ]
        ]
     },
     "fields":{  

     },
     "shadow":false,
     "topLevel":false
  }
},
"comments":{  

},
"currentCostume":0,
"costumes":[  
  {  
     "assetId":"b7853f557e4426412e64bb3da6531a99",
     "name":"costume1",
     "bitmapResolution":1,
     "md5ext":"b7853f557e4426412e64bb3da6531a99.svg",
     "dataFormat":"svg",
     "rotationCenterX":48,
     "rotationCenterY":50
  },
  {  
     "assetId":"e6ddc55a6ddd9cc9d84fe0b4c21e016f",
     "name":"costume2",
     "bitmapResolution":1,
     "md5ext":"e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg",
     "dataFormat":"svg",
     "rotationCenterX":46,
     "rotationCenterY":53
  }
],
"sounds":[  
  {  
     "assetId":"83c36d806dc92327b9e7049a565c6bff",
     "name":"Meow",
     "dataFormat":"wav",
     "format":"",
     "rate":48000,
     "sampleCount":40681,
     "md5ext":"83c36d806dc92327b9e7049a565c6bff.wav"
  }
],
"volume":100,
"layerOrder":1,
"visible":true,
"x":0,
"y":0,
"size":100,
"direction":90,
"draggable":false,
"rotationStyle":"all around"
}