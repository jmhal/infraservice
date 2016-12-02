package br.ufc.mdcc.hpcshelf.backendservices.proxy;

import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.annotation.Resource;
import javax.jws.WebService;
import javax.xml.ws.WebServiceContext;
import javax.xml.ws.handler.MessageContext;

import br.ufc.mdcc.hpcshelf.backendservices.pyws.client.BackEndServicePyWSClient;

import com.sun.net.httpserver.HttpExchange;

@WebService(endpointInterface = "br.ufc.mdcc.hpcshelf.backendservices.proxy.BackEndServices")
public class BackEndServicesImpl implements BackEndServices {
	private static final Logger LOGGER = Logger
			.getLogger(BackEndServicesImpl.class.getName());
	private static ConsoleHandler handler = new ConsoleHandler();
	
	private BackEndServicePyWSClient localClient;

	@Resource
	WebServiceContext wsContext;

	public BackEndServicesImpl(String localServiceURL) {
		localClient = new BackEndServicePyWSClient(localServiceURL);
		LOGGER.setLevel(Level.FINE);
		handler.setLevel(Level.FINE);
		LOGGER.addHandler(handler);
	}

	@Override
	public String deployContractCallback(String profileId, String coreSessionId) {
		MessageContext msgx = wsContext.getMessageContext();
		HttpExchange exchange = (HttpExchange) msgx
				.get("com.sun.xml.internal.ws.http.exchange");
		String remote_ip = exchange.getRemoteAddress().getAddress()
				.getHostAddress();

		LOGGER.log(Level.FINE, "Deploy Profile ID:" + profileId
				+ " coreSessionID:" + coreSessionId + " Remote IP:" + remote_ip);

		// Call Local Python Web Service
		return localClient.deployContractCallback(profileId, coreSessionId, remote_ip);
		// return "OK";
	}

	@Override
	public String destroyPlatform(String coreSessionId) {
		LOGGER.log(Level.FINE, "Destroy coreSessionID:" + coreSessionId);

		// Call Local Python Web Service
		return localClient.destroyPlatform(coreSessionId);
		// return "OK";
		
	}
}
