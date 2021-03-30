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


# connecting to the GTM account, in the Google account provided - format: path="accounts/accountNumber"
account = GTMAccount(path="accounts/")

# making a list of the cotainers of the account
containers = account.list_containers()



#making an empty list, to hold unknown workspaces
unknownWorkspaces = []

#catching containers id, if a publish is done with error
errorPublishVersion = []

#contianers that already have a GA ID 
containerWithGaID = []

print("\nDu er ved at køre et script på containeren: " + account.name.upper() + ".")
print("\nSkriv KØR og tryk ENTER, hvis du vil køre spriptet.\n")
userInput1 = input()
print("\n")

if(userInput1 == "kør"):

    

    #iterating through the list of containers
    for container in containers:

       

            #dev purpose
            #print(container.name)

            #making a list of the workspaces in the container
            workspaces = container.list_workspaces()

            #iterating through the list of workspaces
            for workspace in workspaces:

                #if the workspace.name matches
                if workspace.name == "Default Workspace":

                    try:
                        variable = workspace.create_variable(
                        #TODO Insert GTM trigger object here
                        # For references: https://developers.google.com/tag-manager/api/v2/variable-dictionary-reference

                            {
    
                                "name": "GA ID",
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
                        )

                    except:
                        containerWithGaID.append(workspace.containerId)
                        pass
                else:
                    
                    unknownWorkspaces.append(workspace.containerId)

#print errors and unknown workspaces, for fixing later            
    print("\nFound unknown workspace in containers: ")
    print(unknownWorkspaces)
    print("\nFound GA ID variable in the following containers: ")
    print(containerWithGaID)
