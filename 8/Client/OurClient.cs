using System.Net.Sockets;
using System.Text;

namespace Client
{
    class OurClient
    {
        private TcpClient client;
        private StreamWriter sWriter;
        private StreamReader sReader;
        public OurClient()
        {
            client = new TcpClient ("127.0.0.1", 5555); // (ip адрес , Порт приёма)
            sWriter = new  StreamWriter(client.GetStream(), Encoding.UTF8);
            sReader = new  StreamReader(client.GetStream(), Encoding.UTF8);
            HandleCommunication();
        }
        void HandleCommunication()  // создаём постоянно рабочий сервер
        {
            while (true)
            {
                Console.Write(" > ");
                string message = Console.ReadLine();
                sWriter.WriteLine(message);
                sWriter.Flush();
                // Принимаем ответ от сервера
                string answerServer = sReader.ReadLine();
                Console.WriteLine($"Сервер ответил -> {answerServer}");
            }
        }
    }
}