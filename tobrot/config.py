from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1416857805:AAFLtkmxY8mu5WYOpH8XMdr3wEGDkDhSDnI"
    APP_ID = 1516830
    API_HASH = "f564dcc5409a7e41f4b329d2ddd11d3e"
    OWNER_ID = 1030989359
    AUTH_CHANNEL = [-1001206349958,-1001329850797,-1001371735106]
    DESTINATION_FOLDER = "" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
root_folder_id = 1aGOksKRmuX43Lsvmu3wqkeUy86SCq_mS
token = {"access_token":"ya29.a0AfH6SMBOrTgYoEPlUMOdttNLDRTVNbk_kM9hzCtbk4GIT1-jnTIC6sPudhR42daUPvST_K9pqNG2lRumD-WxSW2d8fFYifg9vaiWz17HsN8adbR8CnGuqB8tF9wI_HZ3NlrgC0quOmAJ8tlpVLmbsKUVv_81CyxCFGkACrrC3a4","token_type":"Bearer","refresh_token":"1//0gzXZO4vNFmS_CgYIARAAGBASNwF-L9IrV2B_tB4OjVYubyt5qaF7RZejhjoh6xG8Es1lGBZ4Fv8ZjPbqWWPpnh4zmLF6pLznYSI","expiry":"2021-02-13T07:20:37.03105952Z"}
team_drive = 0ACORhP6TI89FUk9PVA"""
