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

# making a list of the cotainers of the account
containers = account.list_containers()


#print a list of all containers, with ID, Name and path
print(containers)




            
    
        

        