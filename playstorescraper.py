
import pymysql
con=pymysql.connect(host="localhost", user="root", passwd="",db="playstore_apps_db")
mycursor=con.cursor()
mycursor.execute("""

                SELECT app_url FROM apps_urls LIMIT 10

                """)
res=mycursor.fetchall()
for row in res:
    # print(type(row))
    mypackageName=''.join(row)

    print(mypackageName)
    
    
    details = server.details(mypackageName)

    playstore_id=details['docid']
    print("PlayStoreID: ",playstore_id)
    print(" ")

    App_name=details['title']
    print("Application Name : ",App_name)
    print(" ")

    dev_name=details['creator']
    print("Developer Name : ",dev_name)
    print(" ")

    description=details['descriptionHtml']
    print("Application Details : ",description)
    print(" ")

    img_id=details['image']
    img_url=img_id[1]
    logo_url=img_url['imageUrl']
    print("Img_url: ",logo_url)

    detls=details['details']
    print("")

    application_details=detls['appDetails']

    if 'versionString' in application_details:
        current_version=application_details['versionString']
        print("Current Version : ", current_version)
        print("")

    size=application_details['installationSize']
    print("installation Size : ", size)
    print("")

    app_permission=application_details['permission']
    print("Required Permissions : ", app_permission)
    print("")

    app_developerEmail=application_details['developerEmail']
    print("Developer Email : ", app_developerEmail)
    print("")

    if 'developerWebsite' in application_details:
        app_developerWebsite=application_details['developerWebsite']
        print("Developer Website : ", app_developerWebsite)
        print("")

    else:
        print("No Developer site")

    app_downloads=application_details['numDownloads']
    print("Total Downloads : ", app_downloads)
    print("")

    app_uploadDate=application_details['uploadDate']
    print("Last Updated : ", app_uploadDate)
    print("")




    if 'developerAddress' in application_details:
        app_developerAddress=application_details['developerAddress']
        print("Develope rAddress : ", app_developerAddress)
        print("")


    rating_details=details['aggregateRating']
    # print(rating_details)
    # print("")

    star_rating=rating_details['starRating']
    print("APP Rating: ", star_rating)
    print("")

    app_oneStarRatings=rating_details['oneStarRatings']
    print("ONESTAR Rating: ", app_oneStarRatings)
    print("")

    app_twoStarRatings=rating_details['twoStarRatings']
    print("TWO STAR Rating: ", app_twoStarRatings)
    print("")

    app_threeStarRatings=rating_details['threeStarRatings']
    print("THREE STAR Rating: ", app_threeStarRatings)
    print("")

    app_fourStarRatings=rating_details['fourStarRatings']
    print("FOUR STAR Rating: ", app_fourStarRatings)
    print("")

    app_fiveStarRatings=rating_details['fiveStarRatings']
    print("FIVE STAR Rating: ", app_fiveStarRatings)
    print("")

    app_commentCount=rating_details['commentCount']
    print("Total Comments: ", app_commentCount)
    print("")

    docid = mypackageName
    server.log(docid)
    print("\nAttempting to download {}\n".format(docid))
    fl = server.download(docid)
    with open(docid + ".apk", "wb") as apk_file:
        for chunk in fl.get("file").get("data"):
            apk_file.write(chunk)
        print("\nDownload successful\n")







# print(detls)
# type(detls)