from azureml.core.model import Model
import joblib
import json
import numpy

def init():
    global model
    model_path = Model.get_model_path(model_name='decisionTreemodel.pkl')
    model = joblib.load(model_path)

def run(raw_data, request_headers):
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = model.predict(data)
    
    return {"result": result.tolist()}

init()
test_row = '{"data":[[1, 3, 5, 4, 2, 5], [4, 2, 3, 4, 1, 3], [2, 1, 3, 4, 5, 4], [5, 4, 3, 4, 1, 3], [5, 5, 5, 5, 5, 5]]}'
request_header = {}
prediction = run(test_row, request_header)
print("Test result: ", prediction)