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

#get the account passed to the function, and returns the account as an object
def useAccount(nameOfAccountToUse):
 
    account = GTMAccount(path="accounts/" + str(nameOfAccountToUse))
    return account


def printConfirmation(nameOfAccount):

    message = print("\nDu er ved at køre et script på containeren: " + nameOfAccount.name.upper() + ". \nSkriv KØR og tryk ENTER, hvis du vil køre scriptet.\n")
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
def getTagAndDeleteIt(workspace, nameOfTag):

                try: 
                    tag = workspace.get_tag_by_name(nameOfTag, refresh=True)
                    tag.delete()
                except:
                    pass

#if a variable matches input parameter, delete that trigger
def getVariableAndDeleteIt(workspace, variableName):

                try: 
                    variable = workspace.get_variable_by_name(variableName, refresh=True)
                    variable.delete()
                except: 
                    pass

#if a trigger matches input parameter delete the trigger
def getTriggerAndDeleteIt(workspace, triggerName):

            try:
                    trigger = workspace.get_trigger_by_name(triggerName, refresh=True)
                    trigger.delete()
            except:
                pass    


def iterateContainers(containers):

    for container in containers:

        workspaces = container.list_workspaces()
        return workspaces



def interatingWorkspaces(workspaces):

    for workspace in workspaces:

        if workspace.name == "Default Workspace":

            return workspace

        else: 

            unknownWorkspaces.append(workspace)

            

              
#main function to execute
def runScript(nameOfAccountToUse, nameOfTagToDelete, nameOfTriggerToDelete, nameOfVariableToDelete):

    account = useAccount(nameOfAccountToUse)

    if accountNameIsValidated(account):

            # making a list of the cotainers of the account
            containers = account.list_containers()
        

            workspace =  interatingWorkspaces(iterateContainers(containers))

        
            getTagAndDeleteIt(workspace, nameOfTagToDelete) 

                                                                        
            getTriggerAndDeleteIt(workspace, nameOfTriggerToDelete) 
                    

            getVariableAndDeleteIt(workspace, nameOfVariableToDelete) 

                #print errors and unknown workspaces, for fixing later            
            print("\nFound unknown workspace in containers: ")
            print(unknownWorkspaces)

        
    else: 
        print("Bruger stoppede script")
        




    