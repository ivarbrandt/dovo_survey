from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def dojo_survey():
    return render_template("dojo_survey.html")

@app.route('/result', methods = ['POST'])
def process_form():
    print("Submitted Info")
    print(request.form)
    name_from_form = request.form['name']
    locations_from_form = request.form['locations']
    lang_from_form = request.form['lang']
    textbox_from_form = request.form['textbox']
    return render_template("dojo_response.html", name_on_template=name_from_form, locations_on_template=locations_from_form, lang_on_template=lang_from_form, textbox_on_template=textbox_from_form )



if __name__=="__main__":
    app.run(debug = True)


