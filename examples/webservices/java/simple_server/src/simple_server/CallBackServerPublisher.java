package simple_server;

import javax.xml.ws.Endpoint;

public class CallBackServerPublisher {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Endpoint.publish("http://192.168.1.111:8080/callback", new CallBackServerImpl());
	}
}
