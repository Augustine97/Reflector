from flask import Flask, request , render_template



app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def welcome():
	name=''
	if request.method=="POST" and "Name" in request.form:
		name=request.form.get("Name")
		designation=request.form.get("Designation")
		highesteducation=request.form.get("HighestEducation")
		zodiacsign=request.form.get("ZodiacSign")
	return render_template("udemyflask.html", Name=name, Designation=designation, HighestEducation=highesteducation,  ZodiacSign=zodiacsign)



app.run(debug=True)