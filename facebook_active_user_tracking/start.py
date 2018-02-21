from flask import Flask, render_template, Response
from pymongo import MongoClient
import json
from bson import json_util
from highcharts.highmaps.common import RawJavaScriptText
import time

application = Flask(__name__)

@application.route("/get_users")
def data():
	uri = "mongodb://toe:toe@localhost/test_data?authSource=facebook"
	client = MongoClient(uri)
	db = client.get_database('facebook')
	results = list(db.active_users.find())
	
	data = list()

	for result in results:
		active_time = time.mktime(result['active_time'].timetuple())
		active_time = (active_time* 1000)
		data.append({"x":active_time, "y":result['no_of_users']})

	js = json.dumps(data, default=json_util.default)
	resp = Response(js, status=200, mimetype='application/json')
	return resp

@application.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
