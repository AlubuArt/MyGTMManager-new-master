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

errorCreatingVariable = []



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



def createVariable(workspace, variableObject, container):

    try:
        workspace.create_variable(variableObject)

    except:
        errorCreatingVariable.append(container.name)
        pass



def printErrors(unknownWorkspaces, errorCreatingVariable):
    
    print("\nFound unknown workspace in containers: ")
    print(unknownWorkspaces)
    print("\nError creating variable in container: ")
    print(errorCreatingVariable)  

              
#main function to execute
def runScript(nameOfAccountToUse, variableObject ):

    account = useAccount(nameOfAccountToUse)

    if accountNameIsValidated(account):

            
            # making a list of the cotainers of the account
            containers = account.list_containers()
        
            for container in containers: 

                workspaces = container.list_workspaces()

                for workspace in workspaces:

                    if workspace.name == "Default Workspace":


                        createVariable(workspace, variableObject, container)
                    
                    else: 
                        
                        unknownWorkspaces.append(container.name)
                    
            
            printErrors(unknownWorkspaces, errorCreatingVariable)
            #print errors and unknown workspaces, for fixing later            
        

        
    else: 
        print("Bruger stoppede script")
        




    