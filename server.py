from flask import Flask, render_template,request,redirect

app=Flask(__name__)



@app.route('/',methods=['GET'])
def desplegarRegistroOrden():
    return render_template("index.html")



@app.route('/checkout',methods=['POST'])
def RegistrarOrden():
    nuevaOrden={
        "strawberry":request.form["strawberry"],
        "raspberry":request.form["raspberry"],
        "apple":request.form["apple"],
        "first":request.form["first_name"],
        "LastName":request.form["last_name"],
        "email":request.form["student_id"]
    }

    count= int(nuevaOrden["strawberry"]) + int(nuevaOrden["apple"]) + int(nuevaOrden["raspberry"])
    return render_template("checkout.html",nuevaOrden=nuevaOrden,count=count)

@app.route('/fruits',methods=['GET'])
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
