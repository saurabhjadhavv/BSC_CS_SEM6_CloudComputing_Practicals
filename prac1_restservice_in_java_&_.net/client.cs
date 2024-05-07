using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using (var client = new HttpClient())
        {
            var jsonContent = "{\"amount_inr\": 1000}";
            var stringContent = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");

            var response = await client.PostAsync("http://localhost:5000/convert", stringContent);
            var responseContent = await response.Content.ReadAsStringAsync();

            Console.WriteLine(responseContent);
        }
    }
}
