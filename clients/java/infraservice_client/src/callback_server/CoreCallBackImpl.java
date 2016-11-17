package callback_server;

import javax.jws.WebService;

@WebService(endpointInterface = "callback_server.CoreCallBack")

public class CoreCallBackImpl implements CoreCallBack {
	public void deployCallback(int sessionID, String uri) {
		System.out.println("Session ID: " + sessionID + " Endpoint: " + uri);
	}
}
