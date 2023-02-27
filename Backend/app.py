from flask import Flask, request, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics, CollectorRegistry
import pandas as pd
from vector import text_to_vector
from fill_data import fill_data
import pickle

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.counter('api_requests_total', 'Number of API requests')
metrics.histogram('prediction_latency', 'Prediction latency Bucket')
metrics.gauge('my_inprogress_requests', 'Description of gauge')
metrics.summary('my_prediction_latency', 'My prediction latency')

CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)


    

@app.route('/api/anime', methods=['POST'])
def create_anime():
    data = request.get_json()
    title = text_to_vector(data.get('title'))
    genre = data.get('genre').rsplit(',', 1)
    description = text_to_vector(data.get('description'))
    type = data.get('type').rsplit(',', 1)
    producer = data.get('producer').rsplit(',', 1)
    studio = data.get('studio').rsplit(',', 1)
    df = pd.read_csv('data.csv')
    donnee_entrer= type + producer + studio + genre
    
    df= fill_data(donnee_entrer,description,title,df)
    df = df.drop(['Rating', 'Unnamed: 0'], axis=1)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    y_pred = model.predict(df)
    print(y_pred)
    
    return jsonify({'prediction': str(y_pred[0])})

@app.route('/metrics')
def get_metrics():
    return metrics.generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)