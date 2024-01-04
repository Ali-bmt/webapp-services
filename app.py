print('Hello world')
# import requests
# from flask import Flask, jsonify
# import os

# app = Flask(__name__)

# @app.route('/rick-morty-api')
# def get_azure_sql_data():
#     # Replace this with the actual URL of your API endpoint
#     api_endpoint = 'https://rickandmortyapi.com/api/character/1'

#     try:
#         # Make a request to the API endpoint with SSL verification disabled
#         api_response = requests.get(api_endpoint, verify=False)

#         # Raise an exception for bad status codes
#         api_response.raise_for_status()

#         # Get the JSON response
#         data = api_response.json()

#         # Process the data as needed

#         # Return a JSON response
#         return jsonify(data)
#     except requests.exceptions.RequestException as e:
#         # Handle errors
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
