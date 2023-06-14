from pymongo import MongoClient

def get_db_handle(db_name):
    
    client = MongoClient("mongodb+srv://TESTFARMATST:3czzys7FtN6XysKr@testfarmatst.crr3uq1.mongodb.net/?retryWrites=true&w=majority")
    
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        db = client[db_name]
        
        return db
        
    except Exception as e:
        
        print(e)
        
        return None

    




