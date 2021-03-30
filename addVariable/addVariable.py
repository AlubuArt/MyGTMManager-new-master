from functionsAddVariable import *



#Indsæt ID´et til kontoen
nameOfAccountToUse = 

#Indsæt gtm objektet i json format. Se dokumentationen. Husk at udfyld variablens navn i 
variableObject = { 
                                "name": "variableName",
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
                                ]
                }

runScript(nameOfAccountToUse, variableObject)


                   