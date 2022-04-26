from crypt import methods
from flask import Flask
from flask import render_template, redirect,request,url_for

app = Flask(__name__)

radius = 0
height = 0

top_area = 3.14 * (radius^2)
side_area = (2)*(3.14)*(height*radius)
total_area = top_area+side_area
total_area_sq_ft = total_area/(144)
material_cost = total_area_sq_ft*(25)
labor_cost = total_area_sq_ft*(15)
total_cost = material_cost+labor_cost


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle="About")


def calculate_total_area(total_cost):
    top_area = 3.14 * (radius^2)
    side_area = (2)*(3.14)*(height*radius)
    total_area = top_area+side_area
    total_area_sq_ft = total_area/(144)
    total_cost= total_area_sq_ft*(25)+total_area_sq_ft*(15)  
    return float(total_cost)

def calc_rad(radius):
    return float(radius)

def calc_height(height):
    return float(height)

@app.route('/estimate_info', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        #capture height & radius from form:
        form = request.form
        radius = form['radius']
        height = form['height']
        radius= calc_rad(radius)
        height=calc_height(height)
        if 'radius' in request.form:
            age=calculate_total_area(total_cost)
        if 'height' in request.form:
            age=calculate_total_area(total_cost)
        return render_template('estimate_info.html', pageTitle='Calculate Your estimate', age=age)
    return render_template('estimate_info.html', pageTitle='Calculate Your estimate')




if __name__ == '__main__':
    app.run(debug=True)