using System;
using System.Text;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace Subscriber
{
    class Program
    {
       static void Main(string[] args)
        {
            MqttClient client = new MqttClient("127.0.0.1");
            string clientId = Guid.NewGuid().ToString();
            client.Connect(clientId);
            client.MqttMsgPublishReceived += client_message;
            client.Subscribe(new string[] { "/classroom_A/temperature" }, new byte[] { 0 });
        }
        static void client_message(object sender, MqttMsgPublishEventArgs e)
        {
            String s = Encoding.UTF8.GetString(e.Message);
            Console.WriteLine("Received: " + s);
        }
    }
}
