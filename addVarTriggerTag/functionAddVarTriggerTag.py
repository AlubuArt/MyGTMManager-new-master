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
unknownWorkspaces = []

errorCreatingTag = []

errorCreatingTrigger = []

errorCreatingVariable = []

newTrigger = 0




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


def createTag(workspace, tagObject, container):

    global newTrigger

    try:
        print(thisTrigger)
        #remember to replace the "firingTriggerId" in the object, with the "newTrigger".
        workspace.create_tag(tagObject)

    except:

        errorCreatingTag.append(container.name)
        
    

def createTrigger(workspace, triggerObject, container):
    
    try:
        global newTrigger
        
        trigger = workspace.create_trigger(triggerObject)

        newTrigger = trigger.triggerId
        
        

    except: 
        errorCreatingTrigger.append(container.name)
        pass

def createVar(workspace, varObject, container):

    try:

        variable = workspace.create_variable(varObject)
        

    except: 
        errorCreatingVariable.append(container.name)
        pass
        
    


def printErrors(unknownWorkspaces, errorCreatingTag, errorCreatingTrigger, errorCreatingVariable):
            print("\nFound unknown workspace in containers: ")
            print(unknownWorkspaces)
            print("\nError creating tag in container: ")
            print(errorCreatingTag)  
            print("\nError creating variable in container: ")
            print(errorCreatingVariable)  
            print("\nError creating trigger in container: ")
            print(errorCreatingTrigger)  


def runScript(nameOfAccountToUse, varObject, triggerObject, tagObject):

    account = useAccount(nameOfAccountToUse)

    if accountNameIsValidated(account):

            # making a list of the cotainers of the account
            containers = account.list_containers()
        
            for container in containers: 

                workspaces = container.list_workspaces()

                for workspace in workspaces:

                    if workspace.name == "Default Workspace":

                        createVar(workspace, varObject, container)

                        createTrigger(workspace, triggerObject, container)

                        createTag(workspace, tagObject, container)

     
                    else:
                
                        unknownWorkspaces.append(workspace.containerId)

            #print errors and unknown workspaces, for fixing later            
            printErrors(unknownWorkspaces, errorCreatingTag, errorCreatingTrigger, errorCreatingVariable)


        
    else: 
        print("Bruger stoppede script")



