using System;
using System.Text;
using System.Threading;
using uPLibrary.Networking.M2Mqtt;

namespace Publisher
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rnd = new Random();
            MqttClient client = new MqttClient("127.0.0.1");
            string clientId = Guid.NewGuid().ToString();
            client.Connect(clientId);

            while (true)
            { 
                int r = rnd.Next(18, 22);
                string str = r.ToString();
                Console.WriteLine("Sended: " + str);
                Console.WriteLine("Acknowledged: " + client.Publish("/classroom_A/temperature", Encoding.UTF8.GetBytes(str), 1, false));
                
                Thread.Sleep(2000);

            }
        }
    }
}
