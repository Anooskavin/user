from db_config import *
import random
@app.route("/",methods=["post","get"])
def login():
   cursor = mysql.connection.cursor()
   if request.method == 'POST':
      username = request.form['Uname']
      password = request.form['Pass']
      cursor.execute('select * from user_details where user_name =%s and password = %s', (username, password))
      account = cursor.fetchone()
      if account:
         return "<html><body> Success</body></html>"
      else:
         return redirect(url_for('forget_password'))

   return render_template("login.html")


@app.route("/forget_password",methods=["post","get"])
def forget_password():
   cursor = mysql.connection.cursor()
   if request.method == 'POST':
      #get answers
      q1 = request.form['q1']
      q2 = request.form['q2']
      q3 = request.form['q3']
      q4 = request.form['q4']
      q5 = request.form['q5']
      q=[]
      q.append(q1)
      q.append(q2)
      q.append(q3)
      q.append(q4)
      q.append(q5)
      #get id
      qu1 = request.form['qu1']
      qu2 = request.form['qu2']
      qu3 = request.form['qu3']
      qu4 = request.form['qu4']
      qu5 = request.form['qu5']
      qu=[]
      qu.append(qu1)
      qu.append(qu2)
      qu.append(qu3)
      qu.append(qu4)
      qu.append(qu5)

      cursor.execute('select * from questions')
      questions = cursor.fetchall()
      questions = [list(x) for x in questions]


      for i in range(0,5):
         # print(q1,qu1,"qu"+str(i))
         cursor.execute('select answer from questions where q_id = %s',[qu[i]])
         answers = cursor.fetchone()
         if(answers[0]==q[i]):
            continue
         else:
            return "<html><body>fails</body></html>"
      return "<html><body>Mail sent success</body></html>"










   cursor.execute('select * from questions')
   questions = cursor.fetchall()
   questions = [list(x) for x in questions]

   questions = random.sample(questions,5)



   return render_template("forget_password.html",questions=questions)








if __name__ == '__main__':
   app.run(debug=True)


