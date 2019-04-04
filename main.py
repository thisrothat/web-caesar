from flask import Flask, request
from caesar import rotate_string
import caesar
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True



form = """
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
        <!-- create your form here -->      
        <! /-below is the path(index page)>
       
        <form action="/" method = "post">
        <label for="rot">Rotate by:  
        <input type="text" name="rot" value=0 /> 
        </label>
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit" value="Submit"/>
    </form>
    </body> 
    </html>
    """
    
#print (form)
#print (text)



@app.route("/", methods=['post'])
def encrypt():
    #encrypt the value of text parameter using rotate_string
    #return encrypted string in h1 tags
    #rotated = (rotate_string(form, rot))
    info=str(request.form["text"])
    rotx=int(request.form["rot"])
    secret=str(rotate_string(info,rotx))

    return form.format(secret)
    #print (form)
    #return form    
       

@app.route("/")
def index():
    #print (form)
    return form.format('')
app.run()