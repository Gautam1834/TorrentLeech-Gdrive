from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1416857805:AAGCyWFfqvgZfie_Q0YfE7TgpUoXdl0AVKM"
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
client_id = 28dslkgjsdl-fill-your-details-apps.googleusercontent.com
client_secret = 6Tib48-fill-your-details-KuXXDX-eWgnRBYc
scope = drive
root_folder_id =
token = {"access_token":"ya29.a0AfH6SMBYJzZ3lSIxJTwzOFRE_Nev20-mGnfKyHzPycQGEUOBVxL1Z7ujHTi2L1nsoAtgglu5sQesBqdqFRGMxGnmYauPY_8YMD2GsodVl7TTW4jLgVu7sugtxJWJm7R8h6AHdeZ12_LgQpzuXc0A4e7DgUB8c7t8HDVX5_Y1s3g","token_type":"Bearer","refresh_token":"1//0glDR2jjkwytPCgYIARAAGBASNwF-L9Ir9_4SA_yvXll9JpCkKFijDctynIE82z7YGzN5xv0jBc763zBHfsviJdYPPAjuiYXHnWk","expiry":"2020-12-26T18:22:04.657595603Z"}
team_drive = 0ACORhP6TI89FUk9PVA"""
