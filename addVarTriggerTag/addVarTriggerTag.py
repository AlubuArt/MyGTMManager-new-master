from functionAddVarTriggerTag import *

nameOfAccountToUse = 

thisTrigger = ""


varObject = {          
                "name": "GAID111",
                "type": "gas",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "cookieDomain",
                        "value": "auto"
                     },
                    {
                        "type": "BOOLEAN",
                        "key": "doubleClick",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "setTrackerName",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "useDebugVersion",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "useHashAutoLink",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "decorateFormsAutoLink",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "enableLinkId",
                        "value": "false"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "enableEcommerce",
                        "value": "false"
                    },
                        {
                        "type": "TEMPLATE",
                        "key": "trackingId",
                        "value": "UA-000000-00"
                    }       
                ],

            } 
            

#remember to replace the "firingTriggerId" in the object, with "newTrigger" (unquoted)
tagObject = { 
            
                
                "name": "Accordion111",
                            "type": "ua",
                            "parameter": [
                                {
                                    "type": "BOOLEAN",
                                    "key": "nonInteraction",
                                    "value": "false"
                                },
                                {
                                    "type": "BOOLEAN",
                                    "key": "overrideGaSettings",
                                    "value": "false"
                                },
                                {
                                    "type": "TEMPLATE",
                                    "key": "eventCategory",
                                    "value": "Accordion Click"
                                },
                                {
                                    "type": "TEMPLATE",
                                    "key": "trackType",
                                    "value": "TRACK_EVENT"
                                },
                                {
                                    "type": "TEMPLATE",
                                    "key": "gaSettings",
                                    "value": "{{GAID11}}"
                                },
                                {
                                    "type": "TEMPLATE",
                                    "key": "eventAction",
                                    "value": "{{Click Text}}"
                                },
                                
                                {
                                    "type": "TEMPLATE",
                                    "key": "eventLabel",
                                    "value": "Page URL"
                                }
                            ],
                            
                            
                            "firingTriggerId": [
                                newTrigger
                            ],
                            "tagFiringOption": "ONCE_PER_EVENT",
                            "monitoringMetadata": {
                                "type": "MAP"
                            }
                                    
                                
            
}

triggerObject = {
                
                
                "name": "TestTrigger111",
                "type": "CLICK",
                

 }


runScript(nameOfAccountToUse, varObject, triggerObject, tagObject)