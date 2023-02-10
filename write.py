

def load_db_table(df,conn,table_name,key):
    min = df[key].min()
    max = df[key].max()
    
    df.to_sql(table_name,conn,if_exists="append",index=False)
    print(f"The data has been loaded on {table_name} within {min} and {max}")
    
    
if __name__ == '__main__' :
    
    import pandas as pd
    import os
    
    data = [
        {'user_id':1,'user_first_name':'Scott','user_last_name':'Tiger'},
        {'user_id':2,'user_first_name':'Donald','user_last_name':'Duck'}
        ]
        
    df = pd.DataFrame(data)
    
    configs = dict(os.environ.items())
    
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
        
    load_db_table(df,conn,'users','user_id')