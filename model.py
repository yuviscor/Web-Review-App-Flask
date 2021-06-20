
import sqlite3





def create():
    connection = sqlite3.connect("feedback.db", check_same_thread=True)


    cursor = connection.cursor()
    cursor.execute(

      """  CREATE TABLE IF NOT EXISTS feedback(

       PK INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR(20),
       dealer VARCHAR(20),
       rating INTEGER,
       message TEXT
     
       
        );
    
        """)
    connection.commit()

    cursor.close()
    connection.close()
                    
def add(name,dealer,rating,message):
    connection = sqlite3.connect("feedback.db", check_same_thread=True)


    cursor = connection.cursor()
    cursor.execute(

        """  INSERT INTO feedback(name,dealer,rating,message)
          VALUES('{name}','{dealer}','{rating}','{message}');
    
    """.format(name=name,dealer=dealer,rating = rating,message=message)
    )
    connection.commit()


    cursor.close()
    connection.close()

     








