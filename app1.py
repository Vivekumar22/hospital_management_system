from flask import *;
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client['STUDENT']
studentdetails=db.DETAILS#collection name :DETAILS

app=Flask(__name__)

@app.route("/crudexample")
def sample10():
    return render_template('login.html')

@app.route("/success",methods=('GET','POST'))
def onsubmit():
    fname = request.form.get('fn')
    lname = request.form.get('ln')
    rollno= request.form.get('regno')
    mobile= request.form.get('mb')

    #Insert Single Document
    a={"First Name":fname,"Last Name":lname,"Reg no":rollno,"Mobile Number":mobile}
    studentdetails.insert_one(a)
    # Multiple Single Document
    b= [{"First Name": fname, "Last Name": lname, "Reg no": rollno, "Mobile Number": mobile},{"concept":"DB_Conn"}]
    studentdetails.insert_one(a)
    studentdetails.insert_many(b)
    return "Document Succcessfully Inserted"


if __name__=="__main__":
    app.run()

