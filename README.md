# TestBot
Discord Bot

There are 2 commands right now:  
~react:  
Sends a text message that can be reacted to with custom emoji. Users that react will be assigned the roles that have the name of the emoji they react with. The roles have to be in the 'allowed_roles' list. If they remove the reaction, they will lose that role. The messages that are listened to are stored in a sqlite3 database 'active_messages'  
  
~CreateEmbed:  
Does not work yet, but will create a fancy looking embed without any hardcoding.
