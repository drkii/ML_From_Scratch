from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/send', methods=['GET','POST'])

def send():
    if request.method =='POST':
        img_file=request.files['img_file']
        img_file.save=('./uploads/' + img_file.filename)
        return render_template('index.html')
    else:
        return redirect(url_for('index'))

if __name__=='__main__':
    app.debug = True
    app.run()
