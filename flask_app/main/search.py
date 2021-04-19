@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')