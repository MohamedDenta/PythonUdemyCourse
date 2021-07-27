import mysql.connector
try:
    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    cursor = con.cursor()

    word = input("Enter the word: ")
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}' ;".format(word))
    # cursor.execute("SELECT * FROM Dictionary LIMIT 5")
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    else:
        print("No word Found!")
except Exception as e:
    print(e.__str__())
