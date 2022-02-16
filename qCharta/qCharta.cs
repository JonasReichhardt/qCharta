
using Serilog;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace qCharta
{
  internal class qCharta
  {
    private readonly Mapper _mapper;

    public qCharta(Mapper mapper)
    {
      _mapper = mapper;
    }

    public void Run(string path)
    {
      if (!Directory.Exists(path) || Directory.GetFiles(path).Length==0)
      {
        Log.Error("{path} does not exist or ist empty",path);
        return;
      }

      foreach(var filePath in Directory.GetFiles(path))
      {
        Log.Information("Mapping {filepath}",Path.GetFileName(filePath));
        _mapper.Map(filePath);
      }
      
    }
  }
}
