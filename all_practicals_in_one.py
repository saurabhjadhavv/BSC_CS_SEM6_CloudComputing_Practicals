# Q1.Create a simple rest service. \
    
    
# from flask import Flask, jsonify, request
# app = Flask(__name__)
# # Sample Data
# data = [
#     {'id': 1, 'Name': 'Anshu Tiwari'},
#     {'id': 2, 'Name': 'Saurabh Jadhav'},
#     {'id': 3, 'Name': 'Vishal More'},
#     {'id': 4, 'Name': 'Rohan Pandey'},
# ]
# # EndPoint to get all data
# @app.route('/data', methods=['GET'])
# def get_data():
#     return jsonify({'data': data})

# # EndPoint to get a specific user by ID
# @app.route('/data/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = next((user for user in data if user['id'] == user_id), None)
#     if user:
#         return jsonify({'user': user})
#     else:
#         return jsonify({'message': 'User not found'}), 404   
# @app.route('/data', methods=['POST'])
# def add_user():
#     new_user = {'id':len(data) + 1, 'Name':request.json['Name']}
#     data.append(new_user)
#     return jsonify({'message':'user added succesfully', 'user': new_user}), 201
# if __name__ == "__main__":
# app.run(debug=True)
# Q2. Define a simple service like converting RS into Dollar and call it from different platform like java and .NET.
# 	•	In this we have three file fist is our app.py which is or service which will convert RS into Dollar.
# 	•	Second file is java where we call or service that we created using python in java 
# 	•	Third file is c# for calling our service in .NET.


# App.py

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/convert', methods=['POST'])
# def convert_currency():
#     data = request.get_json()

#     if 'amount_inr' in data:
#         amount_inr = float(data['amount_inr'])
#         # Assuming 1 INR = 0.014 USD (for example)
#         amount_usd = amount_inr * 0.014

#         return jsonify({'amount_usd': amount_usd})
#     else:
#         return jsonify({'error': 'Amount in INR not provided'})
    
# if __name__ == ('__main__'):
#     app.run(debug=True)

# Client.java

# import java.net.URI;
# import java.net.http.HttpClient;
# import java.net.http.HttpRequest;
# import java.net.http.HttpResponse;

# public class client {

#     public static void main(String[] args) throws Exception {
#         HttpClient client = HttpClient.newHttpClient();
#         String apiUrl = "http://localhost:5000/convert";

#         String requestBody = "{\"amount_inr\" : 1000}";

#         HttpRequest request = HttpRequest.newBuilder()
#                 .uri(URI.create(apiUrl))
#                 .header("Content-Type", "application/json")
#                 .POST(HttpRequest.BodyPublishers.ofString(requestBody))
#                 .build();

#         HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
#         System.out.println(response.statusCode());
#         System.out.println(response.body());
#     }
# }

# Client.cs

# using System;
# using System.Net.Http;
# using System.Threading.Tasks;

# class Program
# {
#     static async Task Main(string[] args)
#     {
#         using (var client = new HttpClient())
#         {
#             var jsonContent = "{\"amount_inr\": 1000}";
#             var stringContent = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");

#             var response = await client.PostAsync("http://localhost:5000/convert", stringContent);
#             var responseContent = await response.Content.ReadAsStringAsync();

#             Console.WriteLine(responseContent);
#         }
#     }
# }


# # Q3.Develop application to consume Google’s search / Googles Map RESTful Web service.
# # <!DOCTYPE html>
# # <html lang="en">
# # <head>
# #     <meta charset="UTF-8">
# #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
# #     <title>Google Maps API Example</title>
# #     <style>
# #         #map {
# #             height: 400px;
# #             width: 100%;
# #         }
# #     </style>
# # </head>
# # <body>
# #     <h1>Google Maps API Example</h1>
# #     <div id="map"></div>
# #     <script>
# #         // Initialize and add the map
# #         function initMap() {
# #             // Specify latitude and longitude for the center of the map
# #             const center = { lat: 19.218330, lng: 72.978088 }; // San Francisco coordinates
# #             // Create a new map instance
# #             const map = new google.maps.Map(document.getElementById('map'), {
# #                 zoom: 12,
# #                 center: center
# #             });
# #             // Add a marker at the center of the map
# #             const marker = new google.maps.Marker({
# #                 position: center,
# #                 map: map,
# #                 title: 'San Francisco'
# #             });
# #         }
# #     </script>
# #     <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCBWCgEdqqLlvsSYxC8rnICxwIGUlJCHKs&callback=initMap" async defer></script>
# # </body>
# # </html>

# # Q4. Create a Simple SOAP service.
# # Refer this link :- https://youtu.be/bzOxHPTtoIE?si=LTKja-61jMAluDR4

# # Q5. Implement FOSS-Cloud Functionality VSI (Virtual Server Infrastructure) Infrastructure as a Service (IaaS), Storage.
# # Refer steps that you written in your journals.

