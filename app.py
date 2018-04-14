from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from datetime import datetime
import hal
import threading
import time

app = Flask(__name__)
recipes = []
app.config['SECRET_KEY'] = 'dsfsdf'
maintainer = None
temp_to_maintain = 100.0
current_temp = 0
measure = True


def start_measure_temp():
    global current_temp
    global measure
    print("before measure")
    while measure:
        print("in measure")
        current_temp = hal.get_temp()
        time.sleep(1)
        print("after sleep")


def maintain_temp(accuracy=0.05):
    global temp_to_maintain
    while maintainer != None:
        cur_temp = hal.get_temp()
        if cur_temp < temp_to_maintain - (temp_to_maintain*accuracy):
            hal.switch_heating(True)
        elif cur_temp > temp_to_maintain + (temp_to_maintain*accuracy):
            hal.switch_heating(False)

        time.sleep(1)


def stop_maintainer():
    global maintainer
    maintainer = None


def run_maintainer():
    global maintainer
    if maintainer != None:
        return

    maintainer = threading.Thread(target=maintain_temp)
    maintainer.start()


def store_recipe(recipe_name):
    recipes.append(dict(
        recipe_name=recipe_name,
        user='username',
        date=datetime.utcnow()
    ))


@app.route('/')
def index():
    return render_template('index.html', temp=current_temp)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        store_recipe(recipe_name)
        flash('Stored recipe "{}"'.format(recipe_name))
        return redirect(url_for('index'))
    return render_template('add_recipe.html')


@app.route('/turnonheating', methods=['GET'])
def turnonheating():
    hal.switch_heating(True)
    return render_template('index.html', temp=current_temp)


@app.route('/turnoffheating', methods=['GET'])
def turnoffheating():
    hal.switch_heating(False)
    return render_template('index.html', temp=current_temp)


@app.route('/turnonpump', methods=['GET'])
def turnonpump():
    hal.switch_pump(True)
    return render_template('index.html', temp=current_temp)


@app.route('/turnoffpump', methods=['GET'])
def turnoffpump():
    hal.switch_pump(False)
    return render_template('index.html', temp=current_temp)


@app.route('/gettemp', methods=['GET'])
def gettemp():
    #t = hal.get_temp()
    return jsonify(temp=current_temp)


@app.route('/runmaintainer', methods=['GET'])
def runmaintainer():
    run_maintainer()
    return render_template('index.html', temp=current_temp)


@app.route('/stopmaintainer', methods=['GET'])
def stopmaintainer():
    stop_maintainer()
    return render_template('index.html', temp=current_temp)


@app.route('/settempdebug', methods=['POST'])
def settempdebug():
    hal.set_temp(float(request.form['temp']))
    return render_template('index.html', tempToMaintain=temp_to_maintain, tempToDebug=hal.get_temp())


@app.route('/settemptomaintain', methods=['POST'])
def settemptomaintain():
    global temp_to_maintain
    temp_to_maintain = float(request.form['temp'])
    return render_template('index.html', tempToMaintain=temp_to_maintain, tempToDebug=hal.get_temp())

def startmeasurer():
    measurer = threading.Thread(target=start_measure_temp)
    measurer.start()
    print("Started measurer")

startmeasurer()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
