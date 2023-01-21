#password manager
from tkinter import simpledialog
from database  import init_database

class VaultMethods:
    
    def __init__(self):
        self.db, self.cursor =  init_database()
    def popup_entry(self, heading):
        awswer = simpledialog.askstring("enter details", heading)
        return awswer
    
    def add_password(self, vault_screen):
        platform = self.popup_entry("Platform")
        userid = self.popup_entry("Username/email")
        password = self.popup_entry("Password")
        
        insert_cmd = """INSERT INTO vault(platform, userid, passworf)
                                    VALUES (?, ?, ?)"""
        
        self.cursor.execute(insert_cmd, (platform, usedid, password))
        self.db.commit()
        vault_screen
        