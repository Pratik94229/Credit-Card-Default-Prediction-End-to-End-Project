#Importing dependencies
from flask import Flask, request, render_template
from flask import Response
import os
# to allow cross-origin requests
from flask_cors import CORS, cross_origin 
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation

#import flask_monitoringdashboard as dashboard
from predictFromModel import prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

#Flask Application Setup
app = Flask(__name__)
#dashboard.bind(app)
CORS(app)

# The "/" route handles the GET request and renders the index.html template using the render_template function.
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


'''
1) It handles the POST request for making predictions.
2) If the request has JSON data, it retrieves the file path from the JSON payload and performs prediction and validation.

3)If the request has form data, it retrieves the file path from the form and performs the same validation and prediction steps.
The resulting prediction file path is returned as a response.
'''
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path = request.json['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)
        elif request.form is not None:
            path = request.form['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)

    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)


"""
1)It handles the POST request for training the model.
The "/train" route handles the POST request for training the model.
2)Then it retrieves the file path from the JSON payload, performs training validation using the train_validation class,
and trains the model using the trainModel class.

"""
@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():

    try:
        if request.json['filepath'] is not None:
            path = request.json['filepath']
            train_valObj = train_validation(path) #object initialization

            train_valObj.train_validation()#calling the training_validation function


            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table


    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")

#It runs the application 
port = int(os.getenv("PORT",5001))
if __name__ == "__main__":
    app.run(port=port,debug=True)
