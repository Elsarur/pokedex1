import bcrypt

class EncriptionManager:
    def create_hash(self, text):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(text.encode("utf-8"),salt).decode("utf-8")
    
    def compare_hashes(self, text, hashpw):
        return bcrypt.checkpw(text.encode("utf-8"), hashpw.encode("utf-8"))