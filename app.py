from flask import Flask, jsonify, render_template
import plotly.graph_objects as go


app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return jsonify({"message": "Hello, World! Welcome to Flask on localhost:8080!. Is this thing working?"})


@app.route('/pie-chart')
def pie_chart():
    # Data for the pie chart
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    values = [450, 300, 150, 100]
    
    # Create the pie chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    # Convert the plotly figure to JSON for rendering in the frontend
    return jsonify(fig.to_dict())

@app.route('/pie-chart-html')
def pie_chart_html():
    # Data for the pie chart
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Pizza']
    values = [450, 300, 150, 100, 5000]
    
    # Create the pie chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    # Convert the figure to HTML
    graph_html = fig.to_html(full_html=False)
    
    return render_template('chart.html', graph_html=graph_html)

# Another example route
@app.route('/api/data')
def api_data():
    return jsonify({"data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    # Run the Flask app on localhost at port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
