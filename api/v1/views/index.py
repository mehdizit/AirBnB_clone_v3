from api.v1.views import app_views

@app_app.route('/status')
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})
    
