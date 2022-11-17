using Newtonsoft.Json.Linq;
// class Weather
// {
//   public string Time { get; set; }
//   public float Temperature { get; set; }
//   public string Sunrise { get; set; }
//   public string Sunset { get; set; }
//   public float Precipitation { get; set; }
//   public float Windspeed { get; set; }
// }

internal class Program
{
  private static void Main(string[] args)
  {
    string fileURL = "../weather.json";
    string rawWeatherData = File.ReadAllText(fileURL);

    var weather = JObject.Parse(rawWeatherData);
    var foo = weather["daily"];

    weather["daily"].Select(x => x).ToList().ForEach(x => Console.WriteLine(x));
  }
}
