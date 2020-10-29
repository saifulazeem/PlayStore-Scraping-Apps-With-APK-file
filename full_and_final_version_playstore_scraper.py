import pymysql
from gpapi.googleplay import GooglePlayAPI, RequestError
from google_play_scraper import app
import sys
import os
import re

gsfId=3583722421807643001
authSubToken = '2AdCnRCY3edBQ9jUCG2KpLOsUN5DvYqTgw_3nhM4fXd-naoqwYZ3v4373BGMPugfy16qYw.'
server = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="hero2lte")
print("\nLogin with ac2dm token and gsfId saved\n")
server.login(None, None, gsfId, authSubToken)


con=pymysql.connect(host="localhost", user="thetoolstation_playstore", passwd="thetoolstation_playstore",db="thetoolstation_playstore",charset="utf8mb4", use_unicode=True)
# con.set_charset("utf8mb4")
# con.charset("utf8mb4")

mycursor=con.cursor()
mycursor.execute("""

                SELECT app_url FROM apps_urls WHERE id>=11 AND id<=500 AND status=0

                """)
res=mycursor.fetchall()

for row in res:
    # print(type(row))
    mypackageName=''.join(row)

    print(mypackageName)
    
    try:
        details = server.details(mypackageName)
    
        app_playstore_id=details['docid']
        app_playstore_id=''.join(app_playstore_id)
        print("PlayStoreID: ",app_playstore_id)
        print(" ")
    
        App_name=details['title']
        App_name=''.join(App_name)
        print("Application Name : ",App_name)
        # App_name=pymsql.escape_string(App_name)
        App_name=str(App_name)
        
        
        
        
        
        #====================Start Cleaning app name String==========================
        rxx = re.compile('\W+')
        App_name= rxx.sub(' ', App_name).strip()
        # App_name= App_name.replace(' ','-')
        print("Application Name : ",App_name)
        #====================Start Making Tags========================================
        App_namee=App_name.lower()
        App_namee=App_namee.replace(' ','-')
        app_tag1=App_namee+'-for-pc'
        app_tag2=App_namee+'-apk-for-pc'
        app_tag3=App_namee
        app_tag4=App_namee+'-windows'
        app_tag5=App_namee+'-mac-os-x'
        
        final_app_tags=app_tag1+','+app_tag2+','+app_tag3+','+app_tag4+','+app_tag5
       
        
        #******************** End Making Tags****************************************
        
        #********************End Cleaning app name String ******************************
        print(" ")
        
        #======================Start Creating Slug=======================================
        app_slug_id=app_playstore_id.replace('.','-')
        app_slug_name=App_name.replace(' ','-')
        app_slug_name=app_slug_name.lower()
        # app_slug=app_slug_id+'/'+app_slug_name+'-PC/'
        # app_slug=app_slug_id+'-'+app_slug_name+'-PC'
        app_slug=app_slug_name+'-pc'
        #**********************End Creating Slug*****************************************
    
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
            # print("Application Details : ",description)
            description=str(description)
            #====================Start Cleaning Description String==========================
            rxx = re.compile('\W+')
            description= rxx.sub(' ', description).strip()
            description= description.replace('br','')
            print("Application Details : ", description)
            #********************End Cleaning Description String ******************************
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
            #======================Start Creating Slug=======================================
            app_v_slug_id=app_playstore_id.replace('.','-')
            app_v_slug_name=App_name.replace(' ','-')
            app_v_slug_name=app_v_slug_name.lower()
            app_ver=current_version.replace('.','-')
            app_ver=app_ver.lower()
    
            # app_v_slug=app_slug_id+'/'+app_slug_name+'-PC/download-'+app_ver+'/'
            # app_v_slug=app_slug_id+'-'+app_slug_name+'-PC-download-'+app_ver+
            app_v_slug=app_v_slug_name+'/download-'+app_ver
            #**********************End Creating Slug*****************************************
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
            # print("Develope rAddress : ", app_developerAddress)
            #=====================Start Cleaning Developer Address String===================
            rx = re.compile('\W+')
            app_developerAddress= rx.sub(' ', app_developerAddress).strip()
            app_developerAddress= app_developerAddress.replace('br','')
            print("Develope rAddress : ", app_developerAddress)
            #********************End Cleaning Developer Address String***********************
    
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
    
        #=========================Googlepaystore Scraper=================================
        result = app(
        mypackageName,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
        )
    
        if 'genre' in result:
            app_cat=result['genre']
            app_cat=str(app_cat)
            print('Specific Category  : ',app_cat)
            print(type(app_cat))
            print("")
        else:
            app_cat="N/A"
            print(app_cat)
            print("")
        
        if 'androidVersionText' in result:
            app_req_android=result['androidVersionText']
            app_req_android=str(app_req_android)
            print('Required Android  : ',app_req_android)
            print(type(app_req_android))
            print("")
        else:
            app_req_android="N/A"
            print(app_req_android)
            print("")
        if 'description' in result:
            htm_dec=result['description']
            htm_dec=str(htm_dec)
            # htm_dec_pattern=re.compile('"["
            # u"\U0001F600-\U0001F64F"  # emoticons
            # u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            # u"\U0001F680-\U0001F6FF"  # transport & map symbols
            # u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            #                   "]+", flags=re.UNICODE')
            # htm_dec=htm_dec_pattern.sub(r'', htm_dec)
            import emoji
            def give_emoji_free_text(text):
                return emoji.get_emoji_regexp().sub(r'', text.decode('utf8'))
            htm_dec=give_emoji_free_text(htm_dec.encode('utf8'))
            htm_dec=htm_dec.replace("-","")
            htm_dec=htm_dec.replace("■"," ")
            htm_dec=htm_dec.replace("・"," ")
            htm_dec=htm_dec.replace("*","")
            htm_dec=htm_dec.replace("•","")
            htm_dec=htm_dec.replace("★","")
            htm_dec=htm_dec.replace("✓","")
            htm_dec=htm_dec.replace("<br>","")
            htm_dec=htm_dec.replace("</strong>","")
            htm_dec=htm_dec.replace("<strong>","")
            htm_dec=htm_dec.replace("<b>","")
            htm_dec=htm_dec.replace("</b>","")
            htm_dec=htm_dec.replace("<i>","")
            htm_dec=htm_dec.replace("</i>","")
            htm_dec=htm_dec.replace("<font>","")
            htm_dec=htm_dec.replace("</font>","")
            htm_dec=htm_dec.replace("<p>","")
            htm_dec=htm_dec.replace("</p>","")
            htm_dec=htm_dec.replace("◆","")

            
           

            print('HTML Clean Description : ',htm_dec)
            print("")
        else:
            htm_dec="N/A"
            print(htm_dec)
            print("")
        #*********************Googleplaystore Scraper*****************************
        
        docid = mypackageName
        server.log(docid)
        print("\nAttempting to download {}\n".format(docid))
        try:
            fl = server.download(docid)
            file_name=docid +current_version+".apk"
            file_path='/home/thetoolstation/public_html/cgi-bin/playstore_apk'
            with open(os.path.join(file_path,file_name), "wb") as apk_file:
                for chunk in fl.get("file").get("data"):
                    apk_file.write(chunk)
                print("\nDownload successful\n")
                apk_file_path=file_path+"/"+file_name
                apk=1
                import pathlib
                print(pathlib.Path(file_name).parent.absolute())
        except:
            print("Apk file not Available")
            apkk_file_path="Apk file not Available"
            apk=0
        
        if apk==1:
        
            #============Start Inserting Scraped Data into DB================================
            mycursor.execute("""INSERT INTO 
            playstore_apps_data(
                playstore_id,
                app_name,
                slug,
                developer,
                category,
                img_url,
                description,
                version,
                required_android,
                size,
                permissions,
                dev_email,
                dev_website,
                dev_address,
                installs,
                specific_cat,
                last_updated_on,
                overall_rating,
                onestar_rating,
                twostar_rating,
                threestar_rating,
                fourstar_rating,
                fivestar_rating,
                total_comments,
                app_tags,
                apk_file) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (app_playstore_id,
            App_name,
            app_slug,
            developer_name,
            app_category,
            logo_url,
            htm_dec,
            current_version,
            app_req_android,
            new_size,
            app_permission,
            app_developerEmail,
            app_developerWebsite,
            app_developerAddress,
            app_downloads,
            app_cat,
            app_uploadDate,
            star_rating,
            app_oneStarRatings,
            app_twoStarRatings,
            app_threeStarRatings,
            app_fourStarRatings,
            app_fiveStarRatings,
            app_commentCount,
            final_app_tags,
            apk_file_path))
    
    
            con.commit()
            print("Row inserted")
            #********************End Insertion of Data into playstore_app_data**************************
              #============================Star Insering valuse into version table====================
            mycursor.execute("""INSERT INTO 
            apps_versions(
                playstore_id,
                previous_versions,
                version_slug,
                version_size,
                last_updated_on,
                version_apk_file) 
            VALUES(%s,%s,%s,%s,%s,%s)""",
            (app_playstore_id,
            current_version,
            app_v_slug,
            new_size,
            app_uploadDate,
            apk_file_path))
    
    
            con.commit()
            print("Row inserted in Version table")
    
            #**************EnD Qurey*******************************************
        else:
            
            #============Start Inserting Scraped Data into DB================================
            mycursor.execute("""INSERT INTO 
            playstore_apps_data(
                playstore_id,
                app_name,
                slug,
                developer,
                category,
                img_url,
                description,
                version,
                required_android,
                size,
                permissions,
                dev_email,
                dev_website,
                dev_address,
                installs,
                specific_cat,
                last_updated_on,
                overall_rating,
                onestar_rating,
                twostar_rating,
                threestar_rating,
                fourstar_rating,
                fivestar_rating,
                total_comments,
                app_tags
                ) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (app_playstore_id,
            App_name,
            app_slug,
            developer_name,
            app_category,
            logo_url,
            htm_dec,
            current_version,
            app_req_android,
            new_size,
            app_permission,
            app_developerEmail,
            app_developerWebsite,
            app_developerAddress,
            app_downloads,
            app_cat,
            app_uploadDate,
            star_rating,
            app_oneStarRatings,
            app_twoStarRatings,
            app_threeStarRatings,
            app_fourStarRatings,
            app_fiveStarRatings,
            app_commentCount,
            final_app_tags
            ))
    
    
            con.commit()
            print("Row inserted Without Apk")
            #********************End Insertion of Data into playstore_app_data**************************
              #============================Star Insering valuse into version table====================
            mycursor.execute("""INSERT INTO 
            apps_versions(
                playstore_id,
                previous_versions,
                version_slug,
                version_size,
                last_updated_on
                ) 
            VALUES(%s,%s,%s,%s,%s)""",
            (app_playstore_id,
            current_version,
            app_v_slug,
            new_size,
            app_uploadDate
            ))
    
    
            con.commit()
            print("Row inserted in Version table")
    
            #**************EnD Qurey*******************************************

        #=====================Start Update Url Table====================
        mycursor.execute(""" UPDATE apps_urls SET status=%s WHERE app_url=%s """,(1,mypackageName))
        con.commit()
        print("")
        print("Publish status Updated")
        #*********************End Update Url Tabel Query***************
        
    except:
        print("URl IS Dead Now")

con.close()

        # print("Location: ",Path(docid + ".apk"))







# print(detls)
# type(detls)
