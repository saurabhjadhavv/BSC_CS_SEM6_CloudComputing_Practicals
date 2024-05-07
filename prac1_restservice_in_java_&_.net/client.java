
import java.net.URI;
import java.net.http.*;

public class client {

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String apiUrl = "http://localhost:5000/convert";

        String requestBody = "{\"amount_inr\" : 500}";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(apiUrl))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        // System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}
