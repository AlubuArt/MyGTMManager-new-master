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
    gtm_manager.GoogleTagManagerScopes.DELETE_CONTAINERS
]


#making an empty list, to hold unknown workspaces
unknownWorkspaces = []

errorDeletingTag = []

errorDeletingTrigger = []

errorDeletingVariable = []

#get the account passed to the function, and returns the account as an object
def useAccount(nameOfAccountToUse):
 
    account = GTMAccount(path="accounts/" + str(nameOfAccountToUse))
    return account


def printConfirmation(nameOfAccount):

    
    message = print("\nDu er ved at køre et script på containeren: " + nameOfAccount.name.upper() +
     ". \nSkriv KØR og tryk ENTER, hvis du vil køre scriptet.\n")
    return message 


#prints the account that is being updated, and ask for a confirmation input from
#the user
def accountNameIsValidated(nameOfAccount):
    
    printConfirmation(nameOfAccount)
    userInput = input()

    if (userInput == "kør"):
        return True
    
    else: 
        return False

#if a tag matches input parameter, delete the trigger
def getTagAndDeleteIt(workspace, nameOfTag, container):

                try: 
                    tag = workspace.get_tag_by_name(nameOfTag, refresh=True)
                    tag.delete()
                except:
                    errorDeletingTag.append(container.name)
                    pass

#if a variable matches input parameter, delete that trigger
def getVariableAndDeleteIt(workspace, variableName, container):

                try: 
                    variable = workspace.get_variable_by_name(variableName, refresh=True)
                    variable.delete()
                except: 
                    errorDeletingVariable.append(container.name)
                    pass

#if a trigger matches input parameter delete the trigger
def getTriggerAndDeleteIt(workspace, triggerName, container):

                try:
                    trigger = workspace.get_trigger_by_name(triggerName, refresh=True)
                    trigger.delete()
                except:
                    errorDeletingTrigger.append(container.name)
                    pass  


def printErrors(unknownWorkspaces, errorDeletingTag, errorDeletingTrigger, errorDeletingVariable):
            print("\nFound unknown workspace in containers: ")
            print(unknownWorkspaces)
            print("\nError deleting tag in container: ")
            print(errorDeletingTag)  
            print("\nError deleting variable in container: ")
            print(errorDeletingVariable)  
            print("\nError deleting trigger in container: ")
            print(errorDeletingTrigger)  


def runScript(nameOfAccountToUse, nameOfTagToDelete, nameOfTriggerToDelete, nameOfVariableToDelete):

    account = useAccount(nameOfAccountToUse)

    if accountNameIsValidated(account):

            # making a list of the cotainers of the account
            containers = account.list_containers()
        
            for container in containers: 

                workspaces = container.list_workspaces()

                for workspace in workspaces:

                    if workspace.name == "Default Workspace":

                        

                        getTagAndDeleteIt(workspace, nameOfTagToDelete, container) 
                                                  
                        getTriggerAndDeleteIt(workspace, nameOfTriggerToDelete, container) 
                            
                        getVariableAndDeleteIt(workspace, nameOfVariableToDelete, container)
                        
                    
                    else:
                
                        unknownWorkspaces.append(workspace.containerId)

            #print errors and unknown workspaces, for fixing later            
            printErrors(unknownWorkspaces, errorDeletingTag, errorDeletingTrigger, errorDeletingVariable)


        
    else: 
        print("Bruger stoppede script")
        




    