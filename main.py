from flask import Flask, render_template,request
import mysql.connector
import os
import smtplib
app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="indigocontest"
)

mycursor = mydb.cursor()



@app.route('/')
def home():
    sql1="SELECT start from flight"
    mycursor.execute(sql1)
    mdata = mycursor.fetchall()
    sql2="Select end from flight"
    mycursor.execute(sql2)
    mdata2 = mycursor.fetchall()
    print(mdata)
    return render_template("homepage.html",mdata=mdata,mdata2=mdata2)

@app.route('/status',methods=['GET', 'POST'])
def status():
    if request.method == 'POST':
        val=[]
        departure= request.form['d']
        arrival=request.form['a']
        flightid=request.form['fid']
        b_num=request.form['b_num']
        b_num=int(b_num)
        bnum=[b_num]
        sql1="SELECT fname from user where booking_number = %s"
        mycursor.execute(sql1,bnum)
        udata = mycursor.fetchall()

        sql2="SELECT status from status where flight_id = %s"
        flightid=int(flightid)
        flightid=[flightid]
        mycursor.execute(sql2,flightid)
        sdata = mycursor.fetchall()
        print(sdata)

        sql3="SELECT start,end,duration from flight where flight_id = %s"
        mycursor.execute(sql3,flightid)
        fdata = mycursor.fetchall()
        print(fdata[0][0])

        return render_template("status.html",udata=udata[0][0],sdata=sdata[0][0],fsdata=fdata[0][0],fedata=fdata[0][1],duration=fdata[0][2])
    return render_template("status.html",udata=udata[0][0],sdata=sdata[0][0],fsdata=fdata[0][0],fedata=fdata[0][1],duration=fdata[0][2])

@app.route('/notify',methods=['GET', 'POST'])
def notify():
    msg=""
    val=[]
    if request.method == 'POST':
        flightid=request.form['fid']
        status=request.form['status']
        flightid=int(flightid)
        val.append(status)
        val.append(flightid)
        print(val)
        sql1="update status set status= %s where flight_id = %s"
        print(sql1)
        mycursor.execute(sql1,val)
        mydb.commit()
        msg="Status updated succesfully and all passengers notified!"
        return render_template("changestatus.html",msg=msg)
    return render_template("changestatus.html",msg=msg)
    



if __name__ == '__main__':
   app.run()