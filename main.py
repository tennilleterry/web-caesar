from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        
        <form action= "/encrypt" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input name="rot" type="text" value=0 />
                
            </div>
            
            
            <textarea type="text" name="text">{0}</textarea>
            <br />
            <input type="submit" value="Submit Query" />
        </form>

      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/")
def index():
    
#    return form.format(encryption='')
     return form.format("")
#   return form

@app.route("/encrypt", methods=['POST'])
def encrypt():
    
    rot = request.form['rot']
    text = request.form['text']
    rot = int(rot)
    phrase = rotate_string(text, rot)


    phrase = '<h1>'+ phrase +'</h1>'
#    return form.format(encryption=phrase)
#    return form.format(encryption=phrase)
    return form.format(phrase)
    
    
    

app.run()
