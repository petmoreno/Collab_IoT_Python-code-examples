/* Socket Server */

using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
namespace SocketServer
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            StartServer();
            Console.ReadKey();
        }
        public static void StartServer()
        {
            IPAddress ipaddress = IPAddress.Parse("127.0.0.1");
            IPEndPoint localEndPoint = new IPEndPoint(ipaddress, 10001);
            // creating tcp socket
            Socket listener = new Socket(ipaddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            listener.Bind(localEndPoint);
            listener.Listen(10);
            Console.WriteLine("Waiting for a connection...");
            Socket handler = listener.Accept();
            string data = null;
            byte[] bytes = null;
            while (true)
            {
                bytes = new byte[1024];
                int bytesRec = handler.Receive(bytes);
                data += Encoding.UTF8.GetString(bytes, 0, bytesRec);
                if (data.IndexOf("<EOF>") > -1)
                {
                    break;
                }
            }
            Console.WriteLine("Text received : {0}", data);
            byte[] msg = Encoding.UTF8.GetBytes(data);
            handler.Send(msg);
            handler.Shutdown(SocketShutdown.Both);
            handler.Close();
        }
    }
}