import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def start(self):
        with self.conn:
            self.cur.execute("CREATE TABLE IF NOT EXISTS `users` (name VARCHAR(32), email TEXT, username VARCHAR(32), id INTEGER, IsAdmin INTEGER DEFAULT 0)")
            print(self.cur.execute("SELECT * FROM `users`").fetchall())
    
    def user_exists(self, user_id):
        with self.conn:
            result = self.cur.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
    
    def add_user(self, user_id, user_usrname, user_name, user_email):
        with self.conn:
            user_ident = self.cur.execute("SELECT * FROM `users` WHERE `id` = ?", (str(user_id),)).fetchall()
            user_un = self.cur.execute("SELECT * FROM `users` WHERE `username` = ?", (str(user_usrname),)).fetchall()
            user_nm = self.cur.execute("SELECT * FROM `users` WHERE `name` = ?", (str(user_name),)).fetchall()
            user_eml = self.cur.execute("SELECT * FROM `users` WHERE `email` = ?", (str(user_email),)).fetchall()

            if len(user_ident) > 0 or len(user_un) > 0:
                return "user_already_added"
            elif len(user_nm) > 0 or len(user_eml) > 0:
                return "user_data_already_added"
            else:
                self.cur.execute(
                    "INSERT INTO `users` (`name`, `email`, `username`, `id`) VALUES (?, ?, ?, ?)", (
                user_name,
                user_email,
                user_usrname,
                user_id,))
                print(self.cur.execute("SELECT * FROM `users`").fetchall())
                return "user_added"
    
    def get_all_users(self, user_id):
        if str(user_id) not in str(self.cur.execute("SELECT `id` FROM `users` WHERE `IsAdmin` = ?", (1,)).fetchmany(1)):
            return False
        else:
            return self.cur.execute("SELECT * FROM `users`").fetchall()       

    def get_user(self, user_id):
        return self.cur.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,)).fetchall()
