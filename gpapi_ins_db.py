import pymysql
from gpapi.googleplay import GooglePlayAPI, RequestError
import sys
import os
gsfId=3583722421807643001
authSubToken = '2AdCnRCY3edBQ9jUCG2KpLOsUN5DvYqTgw_3nhM4fXd-naoqwYZ3v4373BGMPugfy16qYw.'
server = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="hero2lte")
print("\nLogin with ac2dm token and gsfId saved\n")
server.login(None, None, gsfId, authSubToken)


con=pymysql.connect(host="localhost", user="root", passwd="",db="playstore_apps_db")
mycursor=con.cursor()
mycursor.execute("""

                SELECT app_url FROM apps_urls WHERE id=35

                """)
res=mycursor.fetchall()

for row in res:
    # print(type(row))
    mypackageName=''.join(row)

    print(mypackageName)
    
    
    details = server.details(mypackageName)

    app_playstore_id=details['docid']
    app_playstore_id=''.join(app_playstore_id)
    print("PlayStoreID: ",app_playstore_id)
    print(" ")

    App_name=details['title']
    App_name=''.join(App_name)
    print("Application Name : ",App_name)
    print(" ")

    if 'creator' in details:
        developer_name=details['creator']
        developer_name=''.join(developer_name)
        print("Developer Name : ",developer_name)
        print(" ")
    else:
        print("Developer Name Not Available ")
        developer_name='Not Found'
        print(" ")

    if 'descriptionHtml' in details:
        description=details['descriptionHtml']
        description=''.join(description)
        print(type(description))
        print("Application Details : ",description)
        print(" ")
    else:
        print("Description Not Available")
        description="No Description found"
        print(" ")

    img_id=details['image']
    img_url=img_id[1]
    logo_url=img_url['imageUrl']
    logo_url=''.join(logo_url)
    print(type(logo_url))
    print("Img_url: ",logo_url)

    detls=details['details']
    print("")

    application_details=detls['appDetails']

    if 'versionString' in application_details:
        current_version=application_details['versionString']
        current_version=''.join(current_version)
        print(type(current_version))
        print("Current Version : ", current_version)
        print("")
    else:
        print("Version Not Available")
        current_version="Not Found"
        print("")

    if 'installationSize' in application_details:
        size=application_details['installationSize']
        def convert_bytes(size):
            for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    return "%3.1f %s" % (size, x)
                size /= 1024.0

            return size
        new_size=convert_bytes(int(size))
        print("installation Size : ", new_size)
        print("")
    else:
        print("Application Size Not Avalibale")
        new_size="Not Found"
        print(" ")

    if 'permission' in application_details:
        app_permission=application_details['permission']
        app_permission=''.join(app_permission)
        print(type(app_permission))
        print("Required Permissions : ", app_permission)
        print("")
    else:
        print("No Permissions Found")
        app_permission="Not Found"
        print(" ")

    if 'developerEmail' in application_details:
        app_developerEmail=application_details['developerEmail']
        app_developerEmail=''.join(app_developerEmail)
        print("Developer Email : ", app_developerEmail)
        print("")
    else:
        print("No Developer Email Found")
        app_developerEmail="Not Found"
        print(" ")

    if 'developerWebsite' in application_details:
        app_developerWebsite=application_details['developerWebsite']
        app_developerWebsite=''.join(app_developerWebsite)
        print("Developer Website : ", app_developerWebsite)
        print("")

    else:
        print("Developer site Not Available")
        app_developerWebsite="Not found"
        print("")

    if 'numDownloads' in application_details:
        app_downloads=application_details['numDownloads']
        app_downloads=''.join(app_downloads)
        print(type(app_downloads))
        print("Total Downloads : ", app_downloads)
        print("")
    else:
        print("Total Downloads Not Found")
        app_downloads="Not found"
        print(" ")    

    if 'uploadDate' in application_details:
        app_uploadDate=application_details['uploadDate']
        app_uploadDate=''.join(app_uploadDate)
        print(type(app_uploadDate))
        print("Last Updated : ", app_uploadDate)
        print("")

    else:
        print("Last Update Date Not Available")
        app_uploadDate="Not found"
        print(" ")
    

    if 'appType' in application_details:
        app_category=application_details['appType']
        app_category=''.join(app_category)
        print("Category : ", app_category)
        print("")
    else:
        print("Category  App")
        app_category='App'
        print(" ")



    if 'developerAddress' in application_details:
        app_developerAddress=application_details['developerAddress']
        app_developerAddress=''.join(app_developerAddress)
        print("Develope rAddress : ", app_developerAddress)
        print("")
    else:
        print("Developer Address Not Available")
        app_developerAddress="Not found"
        print("")


    rating_details=details['aggregateRating']
    # print(rating_details)
    # print("")

    if 'starRating' in rating_details:
        star_rating=rating_details['starRating']
        star_rating=str(star_rating)
        print(type(star_rating))
        print("APP Rating: ", star_rating)
        print("")
    else:
        print("Star Rating Not Available")
        star_rating="Not found"
        print(" ")

    if 'oneStarRatings' in rating_details:
        app_oneStarRatings=rating_details['oneStarRatings']
        app_oneStarRatings=''.join(app_oneStarRatings)
        print("ONESTAR Rating: ", app_oneStarRatings)
        print("")
    else:
        print("One Star Rating Not Avaiable")
        app_oneStarRatings="Not found"
        print(" ")

    if 'twoStarRatings' in rating_details:
        app_twoStarRatings=rating_details['twoStarRatings']
        app_twoStarRatings=''.join(app_twoStarRatings)
        print("TWO STAR Rating: ", app_twoStarRatings)
        print("")
    else:
        print("Two Star Rating Not Available")
        app_twoStarRatings="Not found"
        print(" ")

    if 'threeStarRatings' in rating_details:
        app_threeStarRatings=rating_details['threeStarRatings']
        app_threeStarRatings=''.join(app_threeStarRatings)
        print("THREE STAR Rating: ", app_threeStarRatings)
        print("")
    else:
        print("Three Star Rating is Not Avaiable")
        app_threeStarRatings="Not found"
        print(" ")

    if 'fourStarRatings' in rating_details:
        app_fourStarRatings=rating_details['fourStarRatings']
        app_fourStarRatings=''.join(app_fourStarRatings)
        print("FOUR STAR Rating: ", app_fourStarRatings)
        print("")
    else:
        print("Four Star Rating Not Avaiable")
        app_fourStarRatings="Not found"
        print(" ")

    if 'fiveStarRatings' in rating_details:
        app_fiveStarRatings=rating_details['fiveStarRatings']
        app_fiveStarRatings=''.join(app_fiveStarRatings)
        print("FIVE STAR Rating: ", app_fiveStarRatings)
        print("")
    else:
        print("Five Star Rating is Not Available")
        app_fiveStarRatings="Not found"
        print(" ")

    if 'commentCount' in rating_details:
        app_commentCount=rating_details['commentCount']
        app_commentCount=''.join(app_commentCount)
        print(type(app_commentCount))
        print("Total Comments: ", app_commentCount)
        print("")
    else:
        print("Total Comments Count is Not Available")
        app_commentCount="Not found"
        print(" ")

    docid = mypackageName
    server.log(docid)
    print("\nAttempting to download {}\n".format(docid))
    fl = server.download(docid)
    file_name=docid + ".apk"
    file_path='/home/saifabbasi/GPAPI/playstore_apk'
    with open(os.path.join(file_path,file_name), "wb") as apk_file:
        for chunk in fl.get("file").get("data"):
            apk_file.write(chunk)
        print("\nDownload successful\n")
        apk_file_path=file_path+"/"+file_name
        import pathlib
        print(pathlib.Path(file_name).parent.absolute())
    appp_permission="hhhhh"
    # coon=pymysql.connect(host="localhost", user="root", passwd="",db="playstore_apps_db")
    # myycursor=coon.cursor()
    mycursor.execute("""INSERT INTO 
    playstore_apps_data(
        playstore_id,
        app_name,
        developer,
        category,
        img_url,
        description,
        version,
        size,
        permissions,
        dev_email,
        dev_website,
        dev_address,
        installs,
        last_updated_on,
        overall_rating,
        onestar_rating,
        twostar_rating,
        threestar_rating,
        fourstar_rating,
        fivestar_rating,
        total_comments,
        apk_file) 
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
    (app_playstore_id,
    App_name,
    developer_name,
    app_category,
    logo_url,
    description,
    current_version,
    new_size,
    appp_permission,
    app_developerEmail,
    app_developerWebsite,
    app_developerAddress,
    app_downloads,
    app_uploadDate,
    star_rating,
    app_oneStarRatings,
    app_twoStarRatings,
    app_threeStarRatings,
    app_fourStarRatings,
    app_fiveStarRatings,
    app_commentCount,
    apk_file_path))

    
    
                
    # insert_query_tuple = (app_playstore_id,App_name,developer_name,app_category,logo_url,description,current_version,new_size,app_permission,app_developerEmail,app_developerWebsite,app_developerAddress,app_downloads,app_uploadDate,star_rating,app_oneStarRatings,app_twoStarRatings,app_threeStarRatings,app_fourStarRatings,app_fiveStarRatings,app_commentCount,apk_file_path)

    # mycursor.execute(query,insert_query_tuple )

    con.commit()
    print("Row inserted")
con.close()

        # print("Location: ",Path(docid + ".apk"))







# print(detls)
# type(detls)

