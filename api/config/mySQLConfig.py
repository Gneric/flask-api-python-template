HOST = ""
PORT = "3306"
USER = ""
PWD = ""
DB = ""
MULTIPLESTATEMENTS = True

mysql_procedures = {
    # DataCheck
    "checkUser": "CALL SP_UserCheck (%(user)s, %(pwd)s);",
}