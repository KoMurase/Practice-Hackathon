import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
public class basic01Server {
    public static void main(String[] args) {
        try{
            ServerSocket server = new ServerSocket(3838, 5);
            while(true){
                System.out.println("a");
                Socket socket = server.accept();
                PrintWriter output = new PrintWriter(socket.getOutputStream());
                output.println("this is server");
                output.close();
                socket.close();
            }
        } catch (Exception e){
            System.out.println(e);
        }
    }
}
