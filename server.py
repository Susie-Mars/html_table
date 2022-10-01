from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def student_list():
    student_info = [
        {'first_name' : 'Bobby', 'last_name' : 'McPoyle', 'full_name' : 'Bobby McPoyle'},
        {'first_name' : 'Rickety', 'last_name' : 'Cricket', 'full_name' : ' Rickety Cricket'},
        {'first_name' : 'Gayle', 'last_name' : 'the Snail', 'full_name' : 'Gayle the Snail'},
        {'first_name' : 'Frank', 'last_name' : 'the Snake', 'full_name' : 'Frank the Snake'},
    ]
    return render_template("index.html", students= student_info)



if __name__=="__main__":
    app.run(debug=True)