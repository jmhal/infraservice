package simple_server;

import javax.jws.WebService;

@WebService(endpointInterface = "simple_server.CallBackServer")

public class CallBackServerImpl implements CallBackServer {

	@Override
	public void callback(String profile_id, String endpoint) {
		System.out.println("Profile: " + profile_id + " Endpoint: " + endpoint);	
	}
}
