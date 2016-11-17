package callback_server;

import javax.xml.ws.Endpoint;

public class CoreCallBackPublisher {

	public static void main(String[] args) {
		Endpoint.publish("http://" + args[0] + ":8080/axis2/services/CoreServices", new CoreCallBackImpl());
	}
}
