import flaskr

app = flaskr.create_app()
#  USE FLASK_ENV=development FLASK_APP=run flask
#  For Dev server
if __name__ == "__main__":
    app.run(debug=False)