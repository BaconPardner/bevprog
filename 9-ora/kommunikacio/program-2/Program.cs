class Weather
{
  public string Time { get; set; }
  public double TemperatureMax { get; set; }
  public double TemperatureMin { get; set; }
  public string Sunrise { get; set; }
  public string Sunset { get; set; }
  public double Precipitation { get; set; }

  public Weather(string time, string tempMax, string tempMin, string sunrise, string sunset, string prec)
  {
    Time = time;
    TemperatureMax = double.Parse(tempMax);
    TemperatureMin = double.Parse(tempMin);
    Sunrise = sunrise;
    Sunset = sunset;
    Precipitation = double.Parse(prec);
  }

}

internal class Program
{
  private static void Main(string[] args)
  {
    var weather = File.ReadLines("../weather.txt").ToArray();
    var weatherList = new List<Weather>();

    for (int i = 0; i < 7; i++)
    {
      weatherList.Add(new Weather
      (
        weather[i + 1],
        weather[i + 9],
        weather[i + 17],
        weather[i + 25],
        weather[i + 33],
        weather[i + 41]
      ));
    }

    var coldest = weatherList
      .Min(x => x.TemperatureMin);

    var coldestDay = weatherList
      .Where(x => x.TemperatureMin == coldest)
      .Select(x => $"Coldest day: {x.Time}\ttemperature: {x.TemperatureMin}")
      .First();

    Console.WriteLine(coldestDay);
  }
}
