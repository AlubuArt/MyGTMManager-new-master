# IMPORTANT! 

# Importing gtm_manager from pakage and GTMaccount
import gtm_manager
from gtm_manager.account import GTMAccount
from gtm_manager.manager import GTMManager

# connecting to the Google OAuth credentials and secret ( stored in the same file? )
gtm_manager.CLIENT_SECRET_FILE = ""
gtm_manager.CREDENTIALS_FILE_NAME = "" 
# Adding AUTH Scopes (permissions to edit and publish)
gtm_manager.AUTH_SCOPES = [
gtm_manager.GoogleTagManagerScopes.EDIT_CONTAINERS,
gtm_manager.GoogleTagManagerScopes.PUBLISH,
gtm_manager.GoogleTagManagerScopes.EDIT_CONTAINERVERSIONS,
gtm_manager.GoogleTagManagerScopes.MANAGE_ACCOUNTS,
gtm_manager.GoogleTagManagerScopes.MANAGE_USERS,
]


# connecting to the GTM account, in the Google account provided
account = GTMAccount(path="accounts/")

print("\nDu er ved at køre et script på containeren: " + account.name.upper() + ".")
print("\nSkriv KØR og tryk ENTER, hvis du vil køre spriptet.\n")
userInput1 = input()
print("\n")

if userInput1 == "kør":
    # making a list of the cotainers of the account
    containers = account.list_containers()

    #making an empty list, to hold unknown workspaces
    unknownWorkspaces = []

    #catching containers id, if a publish is done with error
    errorPublishVersion = []

    #errorCreatingTrigger
    errorCreateTrigger = []

    #Error creating tag
    errorCreateTag = []



    #iterating through the list of containers
    
    
    for container in containers:

      

        #making a list of the workspaces in the container
        workspaces = container.list_workspaces()

        #iterating through the list of workspaces
        for workspace in workspaces:

            #if the workspace.name matches
            if workspace.name == "Default Workspace":

                
                #Enable built in variables, by adding them to the list
                try:
                    
                    built_in_variables =  workspace.create_build_ins(

                         ['clickElement', 'clickText']
                    )   


                except:
                    pass



                try:
                    trigger = workspace.create_trigger(       
                            {
                                "name": "Accordion Click Tracking",
                                "type": "CLICK",
                                "filter": [
                                    {
                                        "type": "CSS_SELECTOR",
                                        "parameter": [
                                            {
                                                "type": "TEMPLATE",
                                                "key": "arg0",
                                                "value": "{{Click Element}}"
                                            },
                                            {
                                                "type": "TEMPLATE",
                                                "key": "arg1",
                                                "value": ".accordion-header h3"
                                            }
                                        ]
                                    }
                                ]        
                            }   
                    )


                except:
                    
                    errorCreateTrigger.append(container.name)
                    pass

                try:
                    #each time a new trigger is added to the container it gets an new triggerID automatic. 
                    # We store the new triggerID in the variable  "new triggerId".
                    newTriggerId = trigger.triggerId
                    
                except:
                    pass

                #create a new tag
                try:

                    workspace.create_tag(

                        {
                        
                            "name": "Accordion Click Tracking",
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
                                    "value": "{{GA ID}}"
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
                                newTriggerId
                            ],
                            "tagFiringOption": "ONCE_PER_EVENT",
                            "monitoringMetadata": {
                                "type": "MAP"
                            }
                                    
                                }
                    )
                except:

                    errorCreateTag.append(container.name)
                    pass


      

            #If the container is unknown, append it to the list 
            else:
                
                unknownWorkspaces.append(workspace.name)



    #print errors and unknown workspaces, for fixing later            
    print("\nFound unknown workspace in containers: ")
    print(unknownWorkspaces)

    print("\nError creating trigger. Container already have a trigger with that name.")
    print(errorCreateTrigger)

    print("\nError creating tag. Either the container already have a container with that name, or the the trigger for the container was not created")
    print(errorCreateTag)


                
    
        

        