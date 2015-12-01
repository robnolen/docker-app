import os
import uuid
import requests
from flask import Flask


app = Flask(__name__)
my_uuid = str(uuid.uuid1())

COLOR="#FFFFFF"

@app.route('/')
def hello():
    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="black">Hi, I'm GUID:<br/>
    {}</br>
    <br>
    <br>

    </center>
    
    </body>
    </html>
    """.format(COLOR,my_uuid)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
