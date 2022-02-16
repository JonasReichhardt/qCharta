using Microsoft.Extensions.DependencyInjection;
using Serilog;

namespace qCharta
{
  public class Program
  {
    static void Main(string[] args)
    {
      var services = new ServiceCollection();
      ConfigureServices(services);
      
      using (ServiceProvider serviceProvider = services.BuildServiceProvider())
      {
        qCharta app = serviceProvider.GetRequiredService<qCharta>();
        
        app.Run(args[0]);
      }
    }

    private static void ConfigureServices(ServiceCollection services)
    {
      services.AddSingleton<qCharta>()
      .AddSingleton<Mapper>();
      Log.Logger = new LoggerConfiguration()
                .MinimumLevel.Debug()
                .WriteTo.Console()
                .CreateLogger();
    }
  }
}