import eel
import desktop
import main


app_name="html"
end_point="main.html"
size=(700,600)

@eel.expose
def run(place,job,keyword,csv_name):
    main.run(place,job,keyword,csv_name)

@eel.expose
def no_keyword_run(place,job,csv_name):
    main.no_keyword_run(place,job,csv_name)


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)